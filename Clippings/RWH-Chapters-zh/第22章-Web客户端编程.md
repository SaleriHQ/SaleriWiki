---
title: "第二十二章：扩展示例：Web 客户端编程"
source: "http://book.realworldhaskell.org/"
author: "Bryan O'Sullivan, Don Stewart, John Goerzen"
translator: "Claude"
created: 2026-04-11
type: clipping
category: haskell
description: "Real World Haskell 中文翻译版"
tags:
  - clippings
  - haskell
  - book
  - rwh
  - translated
---

## 第二十二章：扩展示例：Web 客户端编程

到目前为止，你已经看到了如何与数据库交互、解析内容和处理错误。让我们更进一步，在混合中加入一个 Web 客户端库。我们将在本章中开发一个真实的应用：一个播客下载器，或称为 podcatcher。

podcatcher 的想法很简单。它接收一个要处理的 URL 列表。下载每个这些 URL 会产生一个 XML 文件，格式为 RSS。在这个 XML 文件中，我们会找到音频文件 URL 的引用来下载。

podcatchers 通常让用户通过将 RSS URL 添加到他们的配置中来订阅播客。然后，用户可以定期运行更新操作。podcatcher 将下载 RSS 文档，检查其中的音频文件引用，并下载尚未为该用户下载的任何音频文件。

用户通常将 RSS 文档称为播客或播客订阅源，并将每个单独的音频文件称为一集。

为了实现这一点，我们需要有以下几样东西：

- 一个用于下载文件的 HTTP 客户端库
- 一个 XML 解析器
- 一种指定和持久存储我们感兴趣的播客的方式
- 一种持久存储我们已下载的播客剧集的方式

最后两项可以通过我们使用 HDBC 设置的数据库来满足。前两项可以通过我们将在本章中介绍的其他库模块来满足。

本章中的代码是专门为本书编写的，但基于为 hpodder 编写的代码，hpodder 是一个用 Haskell 编写的现有 podcatcher。hpodder 有比这里展示的示例多得多的功能，这使得它太长太复杂，无法在本书中涵盖。如果你有兴趣研究 hpodder，它的源代码可在 http://software.complete.org/hpodder 免费获取。

我们将把本章的代码分成几部分来编写。每个部分将是自己的 Haskell 模块。你将能够通过 ghci 单独玩每个部分。最后，我们将编写将所有内容绑定到一个完整应用的最终代码。我们将从我们需要使用的基本类型开始。

## 基本类型

首先要做的是了解对应用重要的基本信息。这通常是关于用户感兴趣的播客的信息，加上关于我们已看到和处理过的剧集的信息。如果需要，以后很容易更改这些内容，但因为我们几乎在所有地方都会导入它，我们会先定义它：

```haskell
-- file: ch22/PodTypes.hs
module PodTypes where
data Podcast =
    Podcast {castId :: Integer, -- ^ 此播客的数字 ID
             castURL :: String  -- ^ 它的订阅源 URL
            }
    deriving (Eq, Show, Read)
data Episode =
    Episode {epId :: Integer,     -- ^ 此剧集的数字 ID
             epCast :: Podcast,   -- ^ 它来自的播客的 ID
             epURL :: String,     -- ^ 此剧集的下载 URL
             epDone :: Bool       -- ^ 我们是否已完成此剧集
            }
    deriving (Eq, Show, Read)
```

我们将把这些信息存储在数据库中。为播客和剧集都有唯一标识符，可以轻松找到属于特定播客的剧集，加载特定播客或剧集的信息，或处理未来情况（如更改播客的 URL）。

## 数据库

接下来，我们将编写使数据库中的持久存储成为可能的代码。我们主要感兴趣的是在我们于 PodTypes.hs 中定义的 Haskell 结构和我们磁盘上的数据库之间移动数据。此外，用户第一次运行程序时，用户将需要创建他将用于存储数据的数据库表。

我们将使用 HDBC（见第 21 章）与 Sqlite 数据库交互。Sqlite 是轻量级且自包含的，这使其非常适合这个项目。有关安装 HDBC 和 Sqlite 的信息，请参阅第 494 页的"安装 HDBC 和驱动程序"：

```haskell
-- file: ch22/PodDB.hs
module PodDB where
import Database.HDBC
import Database.HDBC.Sqlite3
import PodTypes
import Control.Monad(when)
import Data.List(sort)
-- | 初始化数据库并返回数据库连接
connect :: FilePath -> IO Connection
connect fp =
    do dbh <- connectSqlite3 fp
       prepDB dbh
       return dbh
{- | 为我们的数据准备数据库。
我们创建两个表，并让数据库引擎验证一些数据一致性：
* castid 和 epid 都是唯一的 PRIMARY KEY，绝不能重复
* castURL 也是唯一的
* 在 episodes 表中，对于给定的播客（epcast），
  每个给定的 URL 或剧集 ID 只能有一个实例
-}
prepDB :: IConnection conn => conn -> IO ()
prepDB dbh =
    do tables <- getTables dbh
       when (not ("podcasts" `elem` tables)) $
           do run dbh "CREATE TABLE podcasts (\
                       \castid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                       \castURL TEXT NOT NULL UNIQUE)" []
              return ()
       when (not ("episodes" `elem` tables)) $
           do run dbh "CREATE TABLE episodes (\
                       \epid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                       \epcastid INTEGER NOT NULL,\
                       \epurl TEXT NOT NULL,\
                       \epdone INTEGER NOT NULL,\
                       \UNIQUE(epcastid, epurl),\
                       \UNIQUE(epcastid, epid))" []
              return ()
       commit dbh
{- | 将新播客添加到数据库。忽略传入播客上的 castid，
并返回填充了 castid 的新对象。
尝试添加已存在的播客是错误的。 -}
addPodcast :: IConnection conn => conn -> Podcast -> IO Podcast
addPodcast dbh podcast =
    handleSql errorHandler $
      do -- 将 castURL 插入表中。数据库
         -- 将自动分配一个 cast ID。
         run dbh "INSERT INTO podcasts (castURL) VALUES (?)"
             [toSql (castURL podcast)]
         -- 找出我们刚添加的 URL 的 castID。
         r <- quickQuery' dbh "SELECT castid FROM podcasts WHERE castURL = ?"
              [toSql (castURL podcast)]
         case r of
           [[x]] -> return $ podcast {castId = fromSql x}
           y -> fail $ "addPodcast: unexpected result: " ++ show y
    where errorHandler e =
              do fail $ "Error adding podcast; does this URL already exist?\n"
                     ++ show e
{- | 将新剧集添加到数据库。
由于这是通过自动化完成的，而不是通过用户请求，
我们将简单地忽略添加重复剧集的请求。这样，当我们
处理订阅源时，遇到的每个 URL 都可以被传递给这个函数，
而不必先在数据库中查找它。
此外，我们通常不会关心新的 ID，所以不费心去获取它。 -}
addEpisode :: IConnection conn => conn -> Episode -> IO ()
addEpisode dbh ep =
    run dbh "INSERT OR IGNORE INTO episodes (epCastId, epURL, epDone) \
                \VALUES (?, ?, ?)"
                [toSql (castId . epCast $ ep), toSql (epURL ep),
                 toSql (epDone ep)]
    >> return ()

{- | 修改现有播客。通过 ID 查找给定播客，
并修改数据库记录以匹配传入的 Podcast。 -}
updatePodcast :: IConnection conn => conn -> Podcast -> IO ()
updatePodcast dbh podcast =
    run dbh "UPDATE podcasts SET castURL = ? WHERE castId = ?"
            [toSql (castURL podcast), toSql (castId podcast)]
    >> return ()
{- | 修改现有剧集。通过 ID 查找它并修改数据库记录以匹配给定剧集。 -}
updateEpisode :: IConnection conn => conn -> Episode -> IO ()
updateEpisode dbh episode =
    run dbh "UPDATE episodes SET epCastId = ?, epURL = ?, epDone = ? \
             \WHERE epId = ?"
             [toSql (castId . epCast $ episode),
              toSql (epURL episode),
              toSql (epDone episode),
              toSql (epId episode)]
    >> return ()
{- | 删除播客。首先删除可能存在的该播客的任何剧集。 -}
removePodcast :: IConnection conn => conn -> Podcast -> IO ()
removePodcast dbh podcast =
    do run dbh "DELETE FROM episodes WHERE epcastid = ?"
         [toSql (castId podcast)]
       run dbh "DELETE FROM podcasts WHERE castid = ?"
         [toSql (castId podcast)]
       return ()
{- | 获取所有播客的列表。 -}
getPodcasts :: IConnection conn => conn -> IO [Podcast]
getPodcasts dbh =
    do res <- quickQuery' dbh
              "SELECT castid, casturl FROM podcasts ORDER BY castid" []
       return (map convPodcastRow res)
{- | 获取特定播客。如果 ID 不匹配则返回 Nothing，
如果匹配则返回 Just Podcast。 -}
getPodcast :: IConnection conn => conn -> Integer -> IO (Maybe Podcast)
getPodcast dbh wantedId =
    do res <- quickQuery' dbh
              "SELECT castid, casturl FROM podcasts WHERE castid = ?"
              [toSql wantedId]
       case res of
         [x] -> return (Just (convPodcastRow x))
         [] -> return Nothing
         x -> fail $ "Really bad error; more than one podcast with ID"
{- | 将 SELECT 的结果转换为 Podcast 记录 -}
convPodcastRow :: [SqlValue] -> Podcast
convPodcastRow [svId, svURL] =
    Podcast {castId = fromSql svId,
             castURL = fromSql svURL}
convPodcastRow x = error $ "Can't convert podcast row " ++ show x
{- | 获取特定播客的所有剧集。 -}
getPodcastEpisodes :: IConnection conn => conn -> Podcast -> IO [Episode]
getPodcastEpisodes dbh pc =
    do r <- quickQuery' dbh
            "SELECT epId, epURL, epDone FROM episodes WHERE epCastId = ?"
            [toSql (castId pc)]
       return (map convEpisodeRow r)
    where convEpisodeRow [svId, svURL, svDone] =
              Episode {epId = fromSql svId, epURL = fromSql svURL,
                       epDone = fromSql svDone, epCast = pc}
```

在 PodDB 模块中，我们定义了连接数据库、为其创建所需表、向其中添加数据、查询和删除数据的函数。以下是一个 ghci 会话的示例，演示与数据库的交互。它将在当前工作目录中创建一个名为 poddbtest.db 的数据库文件，并添加一个播客和一集：

```ghci
ghci> :load PodDB.hs
[1 of 2] Compiling PodTypes         ( PodTypes.hs, interpreted )
[2 of 2] Compiling PodDB            ( PodDB.hs, interpreted )
Ok, modules loaded: PodDB, PodTypes.
ghci> dbh <- connect "poddbtest.db"
ghci> :type dbh
dbh :: Connection
ghci> getTables dbh
["episodes","podcasts","sqlite_sequence"]
ghci> let url = "http://feeds.thisamericanlife.org/talpodcast"
ghci> pc <- addPodcast dbh (Podcast {castId=0, castURL=url})
Podcast {castId = 1, castURL = "http://feeds.thisamericanlife.org/talpodcast"}
ghci> getPodcasts dbh
[Podcast {castId = 1, castURL = "http://feeds.thisamericanlife.org/talpodcast"}]
ghci> addEpisode dbh (Episode {epId = 0, epCast = pc, epURL =
"http://www.example.com/foo.mp3", epDone = False})
ghci> getPodcastEpisodes dbh pc
[Episode {epId = 1, epCast = Podcast {castId = 1, castURL =
"http://feeds.thisamericanlife.org/talpodcast"}, epURL = "http://www.example.com/foo.mp3",
epDone = False}]
ghci> commit dbh
ghci> disconnect dbh
```

## 解析器

现在我们有了数据库组件，我们需要代码来解析播客订阅源。这些是包含各种信息的 XML 文件。以下是一个示例 XML 文件，向你展示它们的样子：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss xmlns:itunes="http://www.itunes.com/DTDs/Podcast-1.0.dtd" version="2.0">
  <channel>
    <title>Haskell Radio</title>
    <link>http://www.example.com/radio/</link>
    <description>Description of this podcast</description>
    <item>
      <title>Episode 2: Lambdas</title>
      <link>http://www.example.com/radio/lambdas</link>
      <enclosure url="http://www.example.com/radio/lambdas.mp3"
       type="audio/mpeg" length="10485760"/>
    </item>
    <item>
      <title>Episode 1: Parsec</title>
      <link>http://www.example.com/radio/parsec</link>
      <enclosure url="http://www.example.com/radio/parsec.mp3"
       type="audio/mpeg" length="10485150"/>
    </item>
  </channel>
</rss>
```

在这些文件中，我们主要对两样东西感兴趣：播客标题和 enclosure URL。我们使用 HaXml 工具包（http://www.cs.york.ac.uk/fp/HaXml/）来解析 XML 文件。以下是这个组件的源代码：

```haskell
-- file: ch22/PodParser.hs
module PodParser where
import PodTypes
import Text.XML.HaXml
import Text.XML.HaXml.Parse
import Text.XML.HaXml.Html.Generate(showattr)
import Data.Char
import Data.List
data PodItem = PodItem {itemtitle :: String,
                  enclosureurl :: String
                  }
          deriving (Eq, Show, Read)
data Feed = Feed {channeltitle :: String,
                  items :: [PodItem]}
            deriving (Eq, Show, Read)
{- | 给定一个播客和一个 PodItem，生成一个 Episode -}
item2ep :: Podcast -> PodItem -> Episode
item2ep pc item =
    Episode {epId = 0,
             epCast = pc,
             epURL = enclosureurl item,
             epDone = False}
{- | 从给定字符串解析数据，并使用给定名称用于错误消息。 -}
parse :: String -> String -> Feed
parse content name =
    Feed {channeltitle = getTitle doc,
          items = getEnclosures doc}
    where parseResult = xmlParse name (stripUnicodeBOM content)
          doc = getContent parseResult
          getContent :: Document -> Content
          getContent (Document _ _ e _) = CElem e

          {- | 一些 Unicode 文档以二进制序列开头；
             在处理之前将其剥离。 -}
          stripUnicodeBOM :: String -> String
          stripUnicodeBOM ('\xef':'\xbb':'\xbf':x) = x
          stripUnicodeBOM x = x
{- | 拉出文档的 channel 部分。
注意 HaXml 将 CFilter 定义为：
> type CFilter = Content -> [Content]
-}
channel :: CFilter
channel = tag "rss" /> tag "channel"
getTitle :: Content -> String
getTitle doc =
    contentToStringDefault "Untitled Podcast"
        (channel /> tag "title" /> txt $ doc)
getEnclosures :: Content -> [PodItem]
getEnclosures doc =
    concatMap procPodItem $ getPodItems doc
    where procPodItem :: Content -> [PodItem]
          procPodItem item = concatMap (procEnclosure title) enclosure
              where title = contentToStringDefault "Untitled Episode"
                               (keep /> tag "title" /> txt $ item)
                    enclosure = (keep /> tag "enclosure") item
          getPodItems :: CFilter
          getPodItems = channel /> tag "item"
          procEnclosure :: String -> Content -> [PodItem]
          procEnclosure title enclosure =
              map makePodItem (showattr "url" enclosure)
              where makePodItem :: Content -> PodItem
                    makePodItem x = PodItem {itemtitle = title,
                                       enclosureurl = contentToString [x]}
{- | 将 [Content] 转换为可打印的 String，
如果传入的 [Content] 是 []，则使用默认值，表示没有匹配。 -}
contentToStringDefault :: String -> [Content] -> String
contentToStringDefault msg [] = msg
contentToStringDefault _ x = contentToString x
{- | 将 [Content] 转换为可打印的字符串，注意对其进行解转义。
没有解转义的实现很简单：
> contentToString = concatMap (show . content)
因为 HaXml 的解转义仅在 Elements 上工作，
我们必须确保我们拥有的任何 Content 都包装在 Element 中，
然后使用 txt 拉出内部。 -}
contentToString :: [Content] -> String
contentToString =
    concatMap procContent
    where procContent x =
              verbatim $ keep /> txt $ CElem (unesc (fakeElem x))
          fakeElem :: Content -> Element
          fakeElem x = Elem "fake" [] [x]
          unesc :: Element -> Element
          unesc = xmlUnEscape stdXmlEscaper
```

让我们看看这段代码。首先，我们声明两种类型：PodItem 和 Feed。我们将把 XML 文档转换为 Feed，它包含项目。我们还提供了一个将 PodItem 转换为 PodTypes.hs 中定义的 Episode 的函数。

接下来是解析。parse 函数接受一个表示 XML 内容的 String 和一个表示用于错误消息的名称的 String，然后返回一个 Feed。

HaXml 被设计为将数据从一种类型"过滤"转换为另一种类型的过滤器。它可以是 XML 到 XML 的简单直接转换，或 XML 到 Haskell 数据的转换，或 Haskell 数据到 XML 的转换。HaXml 有一个名为 CFilter 的数据类型，定义如下：

```haskell
type CFilter = Content -> [Content]
```

也就是说，CFilter 接受一个 XML 文档片段并返回 0 个或更多片段。CFilter 可能被要求找到指定标签的所有子标签、具有某个名称的所有标签、包含在 XML 文档某部分中的字面文本，或许多其他事情中的任何一种。还有一个操作符 (/>) 用于链接 CFilter 函数。我们感兴趣的所有数据都出现在 <channel> 标签内，所以我们首先要获取它。我们定义一个简单的 CFilter：

```haskell
channel = tag "rss" /> tag "channel"
```

当我们将文档传递给 channel 时，它会在顶层搜索名为 rss 的标签。然后，在其中查找 channel 标签。

程序的其余部分遵循这个基本方法。txt 从标签中提取字面文本，通过使用 CFilter 函数，我们可以获取文档的任何部分。

## 下载

我们程序的下一部分是下载数据的模块。我们需要下载两种不同类型的数据：一个播客的内容和每集的音频。在前一种情况下，我们会解析数据并更新数据库。对于后者，我们会将数据写入磁盘文件。

我们将从 HTTP 服务器下载数据，因此我们将使用 Haskell HTTP 库（http://www.haskell.org/http/）。对于下载播客订阅源，我们会下载文档、解析它并更新数据库。对于剧集音频，我们会下载文件、将其写入磁盘，并在数据库中将其标记为已下载。以下是代码：

```haskell
-- file: ch22/PodDownload.hs
module PodDownload where
import PodTypes
import PodDB
import PodParser
import Network.HTTP
import System.IO
import Database.HDBC
import Data.Maybe
import Network.URI
{- | 下载一个 URL。如果出错则返回 (Left errorMessage)，
如果成功则返回 (Right doc)。 -}
downloadURL :: String -> IO (Either String String)
downloadURL url =
    do resp <- simpleHTTP request
       case resp of
         Left x -> return $ Left ("Error connecting: " ++ show x)
         Right r ->
             case rspCode r of
               (2,_,_) -> return $ Right (rspBody r)
               (3,_,_) -> -- HTTP 重定向
                 case findHeader HdrLocation r of
                   Nothing -> return $ Left (show r)
                   Just url -> downloadURL url
               _ -> return $ Left (show r)
    where request = Request {rqURI = uri,
                             rqMethod = GET,
                             rqHeaders = [],
                             rqBody = ""}
          uri = fromJust $ parseURI url
{- | 从订阅源更新数据库中的播客。 -}
updatePodcastFromFeed :: IConnection conn => conn -> Podcast -> IO ()
updatePodcastFromFeed dbh pc =
    do resp <- downloadURL (castURL pc)
       case resp of
         Left x -> putStrLn x
         Right doc -> updateDB doc
    where updateDB doc =
              do mapM_ (addEpisode dbh) episodes
                 commit dbh
              where feed = parse doc (castURL pc)
                    episodes = map (item2ep pc) (items feed)
{- | 下载一集，返回表示其放置到的文件名的 String，
出错时返回 Nothing。 -}
getEpisode :: IConnection conn => conn -> Episode -> IO (Maybe String)
getEpisode dbh ep =
    do resp <- downloadURL (epURL ep)
       case resp of
         Left x -> do putStrLn x
                      return Nothing
         Right doc ->
             do file <- openBinaryFile filename WriteMode
                hPutStr file doc
                hClose file
                updateEpisode dbh (ep {epDone = True})
                commit dbh
                return (Just filename)
          -- 此函数应根据文件类型应用扩展名
    where filename = "pod." ++ (show . castId . epCast $ ep) ++ "." ++
                     (show (epId ep)) ++ ".mp3"
```

此模块定义了三个函数：downloadURL，它简单下载 URL 并将其作为 String 返回；updatePodcastFromFeed，它下载 XML 订阅源文件、解析它并更新数据库；以及 getEpisode，它下载给定剧集并在数据库中将其标记为完成。

这里使用的 HTTP 库不会惰性读取 HTTP 结果。因此，在下载大型文件（如播客）时可能会消耗大量 RAM。还有其他库没有此限制。我们使用这个是因为它稳定、易于安装且使用相当简单。对于认真的 HTTP 需求，我们建议使用可从 Hackage 获取的 mini-http。

## 主程序

最后，我们需要一个将所有内容绑定在一起的主程序。以下是我们的主模块：

```haskell
-- file: ch22/PodMain.hs
module Main where
import PodDownload
import PodDB
import PodTypes
import System.Environment
import Database.HDBC
import Network.Socket(withSocketsDo)
main = withSocketsDo $ handleSqlError $
    do args <- getArgs
       dbh <- connect "pod.db"
       case args of
         ["add", url] -> add dbh url
         ["update"] -> update dbh
         ["download"] -> download dbh
         ["fetch"] -> do update dbh
                         download dbh
         _ -> syntaxError
       disconnect dbh
add dbh url =
    do addPodcast dbh pc
       commit dbh
    where pc = Podcast {castId = 0, castURL = url}
update dbh =
    do pclist <- getPodcasts dbh
       mapM_ procPodcast pclist
    where procPodcast pc =
              do putStrLn $ "Updating from " ++ (castURL pc)
                 updatePodcastFromFeed dbh pc
download dbh =
    do pclist <- getPodcasts dbh
       mapM_ procPodcast pclist
    where procPodcast pc =
              do putStrLn $ "Considering " ++ (castURL pc)
                 episodelist <- getPodcastEpisodes dbh pc
                 let dleps = filter (\ep -> epDone ep == False)
                             episodelist
                 mapM_ procEpisode dleps
          procEpisode ep =
              do putStrLn $ "Downloading " ++ (epURL ep)
                 getEpisode dbh ep
syntaxError = putStrLn
  "Usage: pod command [args]\n\
  \\n\
  \pod add url      Adds a new podcast with the given URL\n\
  \pod download     Downloads all pending episodes\n\
  \pod fetch        Updates, then downloads\n\
  \pod update       Downloads podcast feeds, looks for new episodes\n"
```

我们有一个非常简单的命令行解析器，带有一个指示命令行语法错误的函数，以及处理不同命令行参数的小函数。

你可以用如下命令编译这个程序：

```bash
ghc --make -O2 -o pod -package HTTP -package HaXml -package network \
    -package HDBC -package HDBC-sqlite3 PodMain.hs
```

或者，你可以使用第 131 页"创建包"中记录 Cabal 文件来构建这个项目：

```cabal
-- ch23/pod.cabal
Name: pod
Version: 1.0.0
Build-type: Simple
Build-Depends: HTTP, HaXml, network, HDBC, HDBC-sqlite3, base
Executable: pod
Main-Is: PodMain.hs
GHC-Options: -O2
```

此外，你需要一个简单的 Setup.hs 文件：

```haskell
import Distribution.Simple
main = defaultMain
```

现在，要使用 Cabal 构建，你只需运行以下命令：

```bash
runghc Setup.hs configure
runghc Setup.hs build
```

你会在 dist 目录中找到你的输出。要在系统范围内安装程序，请运行 runghc Setup.hs install。
