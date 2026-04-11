---
title: "第二十三章：使用 gtk2hs 进行 GUI 编程"
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

## 第二十三章：使用 gtk2hs 进行 GUI 编程

在本书中，我们一直在开发简单的基于文本的工具。虽然这些通常是理想的界面，但有时需要图形用户界面（GUI）。Haskell 有几种 GUI 工具包可用。在本章中，我们将看看其中之一：gtk2hs。*

## 安装 gtk2hs

在我们深入使用 gtk2hs 之前，你需要安装它。在大多数 Linux、BSD 或其他 POSIX 平台上，你会找到现成的 gtk2hs 包。你通常需要安装 GTK+ 开发环境、Glade 和 gtk2hs。具体步骤因发行版而异。

Windows 和 Mac 开发者应查阅 http://www.haskell.org/gtk2hs/download/ 上的 gtk2hs 下载站点。首先从那里下载 gtk2hs。然后你还需要 Glade 版本 3。Mac 开发者可以在 http://www.macports.org/ 找到它，而 Windows 开发者应查阅 http://sourceforge.net/projects/gladewin32。

## GTK+ 栈概述

在查看代码之前，让我们花点时间思考一下我们将使用的系统架构。首先，我们有 GTK+。GTK+ 是一个跨平台的 GUI 构建工具包，用 C 实现。它在 Windows、Mac、Linux、BSD 等上运行。它也是 GNOME 桌面环境下的工具包。

接下来是 Glade。Glade 是一个用户界面设计器，让你以图形方式布局应用的窗口和对话框。Glade 将界面保存在 XML 文件中，你的应用将在运行时加载它们。

* 还存在几个替代方案。除了 gtk2hs，wxHaskell 也是一个突出的跨平台 GUI 工具包。

这个难题的最后一块是 gtk2hs。这是 GTK+、Glade 和几个相关库的 Haskell 绑定。它是可用于 GTK+ 的众多语言绑定之一。

## 使用 Glade 设计用户界面

在本章中，我们将为我们在第 22 章首次开发的播客下载器开发一个 GUI。我们的第一个任务是在 Glade 中设计用户界面。一旦完成了这一点，我们将编写 Haskell 代码将其与应用集成。

因为这是一本 Haskell 书，而不是 GUI 设计书，我们将快速浏览这些早期部分。有关使用 Glade 进行界面设计的更多信息，你可能希望参考以下资源：

Glade 主页
包含 Glade 的文档；见 http://glade.gnome.org/。

GTK+ 主页
包含有关不同小部件的信息。参阅文档部分，然后是稳定的 GTK 文档区域；见 http://www.gtk.org/。

gtk2hs 主页
也有一个有用的文档部分，包含 gtk2hs 的 API 参考和 Glade 教程；见 http://www.haskell.org/gtk2hs/documentation/。

## Glade 概念

Glade 是一个用户界面设计工具。它让我们使用图形界面来设计我们的图形界面。我们可以通过一堆调用 GTK+ 函数的调用来构建窗口组件，但通常用 Glade 来做这件事更容易。

我们在 GTK+ 中处理的基本"东西"是小部件（widget）。小部件代表 GUI 的任何部分，可能包含其他小部件。一些小部件示例包括窗口、对话框、按钮和按钮内的文本。

Glade 就是一个小部件布局工具。我们设置一整棵小部件树，顶层窗口在树的顶部。你可以用与 HTML 有点类似的术语来考虑 Glade 和小部件：你可以用类似表格的布局排列小部件，设置填充规则，并以分层方式构建整个描述。

Glade 将小部件描述保存到 XML 文件中。我们的程序在运行时加载此 XML 文件。我们通过请求 Glade 运行时库加载具有特定名称的小部件来加载小部件。

图 23-1 显示了使用 Glade 设计应用主屏幕的组件的工作示例的屏幕截图。

在本书可下载的资料中，你可以找到完整的 Glade XML 文件作为 podresources.glade。你可以加载此文件并在 Glade 中编辑它（如果你愿意）。

## 事件驱动编程

GTK+，像许多 GUI 工具包一样，是一个事件驱动的工具包。这意味着不是显示一个对话框并等待用户点击按钮，恰恰相反，我们告诉 gtk2hs 如果某个按钮被点击要调用什么函数，但不在对话框中等待点击。

这与用于控制台程序的传统模型不同。仔细想想，这几乎是必须的。GUI 程序可能打开多个窗口，编写代码坐在那里等待特定打开窗口组合中的输入可能是一个复杂的命题。

事件驱动编程与 Haskell 配合得很好。正如我们在本书中反复讨论的，函数式语言在传递函数方面蓬勃发展。所以我们将传递函数给 gtk2hs，这些函数在某些事件发生时被调用。这些被称为回调函数。

GTK+ 程序的核心是主循环。这是程序的一部分，等待来自用户的操作或来自程序的命令并执行它们。

GTK+ 主循环完全由 GTK+ 处理。对我们来说，它看起来像一个我们执行的 IO 操作，在 GUI 被处理之前不会返回。

由于主循环负责从处理鼠标点击到在窗口被露出时重绘窗口的所有事情，它必须始终可用。我们不能只是在主循环内运行长时间运行的任务——比如下载播客剧集——这会使 GUI 无响应，并且点击取消按钮等操作将无法及时处理。

因此，我们将使用多线程来处理这些长时间运行的任务。有关多线程的更多信息，请参阅第 24 章。现在，只需知道我们将使用 forkIO 为长时间运行的任务（如下载播客订阅源和剧集）创建新线程。对于非常快速的任务，比如向数据库添加新播客，我们不会费心使用单独的线程，因为它执行得如此之快以至于用户永远不会注意到。

## 初始化 GUI

我们的第一步将涉及为我们程序初始化 GUI。出于我们将在本章后面的"使用 Cabal"第 528 页解释的原因，我们将有一个名为 PodLocalMain.hs 的小文件，它加载 PodMain 并将路径传递给 podresources.glade，这是 Glade 保存的 XML 文件，给出了关于我们 GUI 小部件的信息：

```haskell
-- file: ch23/PodLocalMain.hs
module Main where
import qualified PodMainGUI
main = PodMainGUI.main "podresources.glade"
```

现在，让我们看看 PodMainGUI.hs。这个文件是我们必须从第 22 章中的示例修改的唯一 Haskell 源文件，以使其作为 GUI 工作。让我们从查看新的 PodMainGUI.hs 文件的开头开始——我们为了清晰起见将其从 PodMain.hs 重新命名：

```haskell
-- file: ch23/PodMainGUI.hs
module PodMainGUI where
import PodDownload
import PodDB
import PodTypes
import System.Environment
import Database.HDBC
import Network.Socket(withSocketsDo)
-- GUI 库
import Graphics.UI.Gtk hiding (disconnect)
import Graphics.UI.Gtk.Glade
```

PodMainGUI.hs 的第一部分与我们的非 GUI 版本类似。但是，我们导入了三个额外的组件。首先是 Graphics.UI.Gtk，它提供了我们将使用的大部分 GTK+ 函数。这个模块和 Database.HDBC 都提供了一个名为 disconnect 的函数。因为我们将使用 HDBC 版本，而不是 GTK+ 版本，所以我们不从 Graphics.UI.Gtk 导入那个函数。

Graphics.UI.Gtk.Glade 包含加载和使用 Glade 文件所需的函数。

我们还导入 Control.Concurrent，它具有多线程编程所需的基础知识。一旦我们进入程序的核心，我们将从这里使用几个函数。接下来，让我们定义一个类型来存储有关 GUI 的信息：

```haskell
-- file: ch23/PodMainGUI.hs
-- | 我们主要的 GUI 类型
data GUI = GUI {
      mainWin :: Window,
      mwAddBt :: Button,
      mwUpdateBt :: Button,
      mwDownloadBt :: Button,
      mwFetchBt :: Button,
      mwExitBt :: Button,
      statusWin :: Dialog,
      swOKBt :: Button,
      swCancelBt :: Button,
      swLabel :: Label,
      addWin :: Dialog,
      awOKBt :: Button,
      awCancelBt :: Button,
      awEntry :: Entry}
```

我们的新 GUI 类型存储我们将在整个程序中关心的所有小部件。大型程序可能不希望有这样单一的类型。对于这个小型示例，这是有意义的，因为它可以轻松地在不同函数之间传递，并且我们会知道我们始终有所需的信息可用。

在这个记录中，我们有用于 Window（顶级窗口）、Dialog（对话框窗口）、Button（可点击按钮）、Label（一段文本）和 Entry（用户输入文本的地方）的字段。现在让我们看看我们的 main 函数：

```haskell
-- file: ch23/PodMainGUI.hs
main :: FilePath -> IO ()
main gladepath = withSocketsDo $ handleSqlError $
    do initGUI                  -- 初始化 GTK+ 引擎
       -- 经常地，我们尝试运行其他线程。
       timeoutAddFull (yield >> return True)
                      priorityDefaultIdle 100
       -- 从 Glade 文件加载 GUI
       gui <- loadGlade gladepath
       -- 连接到数据库
       dbh <- connect "pod.db"
       -- 设置我们的事件
       connectGui gui dbh
       -- 运行 GTK+ 主循环；在 GUI 完成后退出
       mainGUI

       -- 最后断开与数据库的连接
       disconnect dbh
```

请记住，这个 main 函数的类型与通常的略有不同，因为它是由 PodLocalMain.hs 中的 main 调用的。我们首先调用 initGUI，它初始化 GTK+ 系统。接下来，我们调用 timeoutAddFull。这个调用仅对多线程 GTK+ 程序是必需的。它告诉 GTK+ 主循环经常暂停以给其他线程运行的机会。

之后，我们调用 loadGlade 函数（见以下代码）从 Glade XML 文件加载小部件。接下来，我们连接到数据库并调用 connectGui 函数来设置我们的回调函数。然后，我们启动 GTK+ 主循环。我们期望它可能需要分钟、小时，甚至几天 mainGUI 才会返回。当它返回时，意味着用户已关闭主窗口或点击了退出按钮。之后，我们断开与数据库的连接并关闭程序。现在，让我们看看我们的 loadGlade 函数：

```haskell
-- file: ch23/PodMainGUI.hs
loadGlade gladepath =
    do -- 从 glade 路径加载 XML。
       -- 注意：如果失败，会在控制台（而非图形）抛出运行时错误！
       Just xml <- xmlNew gladepath
       -- 加载主窗口
       mw <- xmlGetWidget xml castToWindow "mainWindow"
       -- 加载所有按钮
       [mwAdd, mwUpdate, mwDownload, mwFetch, mwExit, swOK, swCancel,
        auOK, auCancel] <-
           mapM (xmlGetWidget xml castToButton)
           ["addButton", "updateButton", "downloadButton",
            "fetchButton", "exitButton", "okButton", "cancelButton",
            "auOK", "auCancel"]

       sw <- xmlGetWidget xml castToDialog "statusDialog"
       swl <- xmlGetWidget xml castToLabel "statusLabel"
       au <- xmlGetWidget xml castToDialog "addDialog"
       aue <- xmlGetWidget xml castToEntry "auEntry"
       return $ GUI mw mwAdd mwUpdate mwDownload mwFetch mwExit
              sw swOK swCancel swl au auOK auCancel aue
```

这个函数首先调用 xmlNew，它加载 Glade XML 文件。它在错误时返回 Nothing。这里我们使用模式匹配来提取成功时的结果值。如果失败，将显示控制台（非图形）异常；本章末尾的练习之一解决了这个问题。

现在我们有了 Glade 的 XML 文件加载，你将看到一堆对 xmlGetWidget 的调用。这个 Glade 函数用于加载小部件的 XML 定义并返回该小部件的 GTK+ 小部件类型。我们必须向该函数传递一个值，指示我们期望的 GTK+ 类型——如果这些不匹配，我们会得到运行时错误。

我们首先为主窗口创建一个小部件。它从名为"mainWindow"的 XML 小部件定义加载，并存储在 mw 变量中。然后我们使用模式匹配和 mapM 来加载所有按钮。然后，我们有两个对话框、一个标签和一个条目要加载。最后，我们使用所有这些来构建 GUI 类型并返回它。

接下来，我们需要将回调函数设置为事件处理器：

```haskell
-- file: ch23/PodMainGUI.hs
connectGui gui dbh =
    do -- 当关闭按钮被点击时，通过调用 GTK mainQuit 函数
       -- 终止 GUI 循环
       onDestroy (mainWin gui) mainQuit

       -- 主窗口按钮
       onClicked (mwAddBt gui) (guiAdd gui dbh)
       onClicked (mwUpdateBt gui) (guiUpdate gui dbh)
       onClicked (mwDownloadBt gui) (guiDownload gui dbh)
       onClicked (mwFetchBt gui) (guiFetch gui dbh)
       onClicked (mwExitBt gui) mainQuit
       -- 我们把状态窗口按钮留到后面
```

我们从调用 onDestroy 开始 connectGui 函数。这意味着当有人点击操作系统的关闭按钮时（通常在 Windows 或 Linux 上的标题栏中是一个 X，在 Mac OS X 上是一个红圈），我们在主窗口上调用 mainQuit 函数。mainQuit 关闭所有 GUI 窗口并终止 GTK+ 主循环。

接下来，我们调用 onClicked 来为我们五个不同的按钮点击注册事件处理器。对于按钮，如果用户通过键盘选择按钮，这些处理器也会被调用。点击这些按钮将调用我们的函数，如 guiAdd，并传递 GUI 记录以及数据库句柄。

此时，我们已经完整定义了 GUI podcatcher 的主窗口。它看起来像图 23-2 中的屏幕截图。

## 添加播客窗口

现在我们介绍了主窗口，让我们从添加播客窗口开始讨论我们应用呈现的其他窗口。当用户点击添加新播客的按钮时，我们需要弹出一个对话框来提示输入播客的 URL。我们已在 Glade 中定义了这个对话框，所以我们只需要设置它：

```haskell
-- file: ch23/PodMainGUI.hs
guiAdd gui dbh =
    do -- 初始化添加 URL 窗口
       entrySetText (awEntry gui) ""
       onClicked (awCancelBt gui) (widgetHide (addWin gui))
       onClicked (awOKBt gui) procOK

       -- 显示添加 URL 窗口
       windowPresent (addWin gui)
    where procOK =
              do url <- entryGetText (awEntry gui)
                 widgetHide (addWin gui) -- 移除对话框
                 add dbh url             -- 添加到数据库
```

我们首先调用 entrySetText 将条目框（用户输入 URL 的地方）的内容设置为空字符串。这是因为相同的小部件在程序的生命周期中被重复使用，我们不希望用户上次输入的 URL 保留在那里。接下来，我们设置对话框中两个按钮的动作。如果用户点击取消按钮，我们只需通过对其调用 widgetHide 将对话框从屏幕上移除。如果用户点击确定按钮，我们调用 procOK。

procOK 首先从条目小部件中检索提供的 URL。然后，它使用 widgetHide 来摆脱对话框。最后，它调用 add 将 URL 添加到数据库。这个 add 与我们在非 GUI 版本程序中拥有的函数完全相同。

我们在 guiAdd 中做的最后一件事是实际显示弹出窗口。那是通过调用 windowPresent 完成的，它是 widgetHide 的反面。

请注意，guiAdd 函数几乎立即返回。它只是设置小部件并导致显示框；在任何时候都不会阻塞等待输入。图 23-3 显示了对话框的样子。

## 长时间运行的任务

当我们考虑主窗口中可用的按钮时，其中三个对应于可能需要一段时间才能完成的任务：update、download 和 fetch。当这些操作进行时，我们想用 GUI 做两件事：向用户提供操作状态，以及在操作进行中取消操作的能力。

由于所有这三个都是非常相似的操作，提供一种通用方式来处理这种交互是有意义的。我们在 Glade 文件中定义了一个单一的状态窗口小部件，将被所有这三个操作使用。在我们的 Haskell 源代码中，我们将定义一个通用的 statusWindow 函数，所有这三个操作也将使用它。

statusWindow 接受四个参数：GUI 信息、数据库信息、给出窗口标题的 String，以及将执行操作的函数。这个函数本身将接收一个可以调用来报告其进度的函数。以下是代码：

```haskell
-- file: ch23/PodMainGUI.hs
statusWindow :: IConnection conn =>
                GUI
             -> conn
             -> String
             -> ((String -> IO ()) -> IO ())
             -> IO ()
statusWindow gui dbh title func =
    do -- 清除状态文本
       labelSetText (swLabel gui) ""

       -- 禁用确定按钮，启用取消按钮
       widgetSetSensitivity (swOKBt gui) False
       widgetSetSensitivity (swCancelBt gui) True
       -- 设置标题
       windowSetTitle (statusWin gui) title

       -- 启动操作
       childThread <- forkIO childTasks
       -- 定义点击取消时发生的情况
       onClicked (swCancelBt gui) (cancelChild childThread)

       -- 显示窗口
       windowPresent (statusWin gui)
    where childTasks =
              do updateLabel "Starting thread..."
                 func updateLabel
                 -- 在子任务完成后，启用 OK
                 -- 并禁用取消
                 enableOK

          enableOK =
              do widgetSetSensitivity (swCancelBt gui) False
                 widgetSetSensitivity (swOKBt gui) True
                 onClicked (swOKBt gui) (widgetHide (statusWin gui))
                 return ()
          updateLabel text =
              labelSetText (swLabel gui) text
          cancelChild childThread =
              do killThread childThread
                 yield
                 updateLabel "Action has been cancelled."
                 enableOK
```

这个函数首先清除上次运行的状态标签文本。接下来，我们禁用（灰显）确定按钮并启用取消按钮。当操作进行时，点击确定没有多大意义。当它完成时，点击取消也没有多大意义。

接下来，我们设置窗口的标题。标题是系统显示在窗口标题栏中的部分。最后，我们启动新线程（由 childTasks 表示）并保存其线程 ID。然后，我们定义如果用户点击取消会发生什么——我们调用 cancelChild，传递线程 ID。最后，我们调用 windowPresent 来显示状态窗口。

在 childTasks 中，我们显示一条消息说我们正在启动线程。然后我们调用实际的工作函数，传递 updateLabel 作为用于显示状态消息的函数。请注意，程序的命令行版本可以在此处传递 putStrLn。

最后，在工作函数退出后，我们调用 enableOK。这个函数禁用取消按钮，启用确定按钮，并定义点击确定按钮会导致状态窗口消失。

updateLabel 简单地调用标签小部件上的 labelSetText 来用显示的文本更新它。最后，cancelChild 终止正在处理任务的线程，更新标签，并启用确定按钮。

我们现在有了定义三个 GUI 函数的基础设施。它们看起来像这样：

```haskell
-- file: ch23/PodMainGUI.hs
guiUpdate :: IConnection conn => GUI -> conn -> IO ()
guiUpdate gui dbh =
    statusWindow gui dbh "Pod: Update" (update dbh)
guiDownload gui dbh =
    statusWindow gui dbh "Pod: Download" (download dbh)
guiFetch gui dbh =
    statusWindow gui dbh "Pod: Fetch"
                     (\logf -> update dbh logf >> download dbh logf)
```

为了简洁，我们只为第一个提供了类型，但所有三个都有相同的类型，Haskell 可以通过类型推断来计算它们。注意我们的 guiFetch 实现。我们没有两次调用 statusWindow，而是将其动作中的函数组合在一起。

最后一块拼图由三个执行我们工作的函数组成。add 未修改自命令行章节。update 和 download 仅被修改为接受日志函数，而不是为状态更新调用 putStrLn。

```haskell
-- file: ch23/PodMainGUI.hs
add dbh url =
    do addPodcast dbh pc
       commit dbh
    where pc = Podcast {castId = 0, castURL = url}
update :: IConnection conn => conn -> (String -> IO ()) -> IO ()
update dbh logf =
    do pclist <- getPodcasts dbh
       mapM_ procPodcast pclist
       logf "Update complete."
    where procPodcast pc =
              do logf $ "Updating from " ++ (castURL pc)
                 updatePodcastFromFeed dbh pc
download dbh logf =
    do pclist <- getPodcasts dbh
       mapM_ procPodcast pclist
       logf "Download complete."
    where procPodcast pc =
              do logf $ "Considering " ++ (castURL pc)
                 episodelist <- getPodcastEpisodes dbh pc
                 let dleps = filter (\ep -> epDone ep == False)
                             episodelist
                 mapM_ procEpisode dleps
          procEpisode ep =
              do logf $ "Downloading " ++ (epURL ep)
                 getEpisode dbh ep
```

图 23-4 显示了运行更新后的最终结果的样子。

## 使用 Cabal

我们在第 515 页的"主程序"中为命令行版本提供了一个用于构建此项目的 Cabal 文件。我们需要对其进行一些调整以使其与 GUI 版本一起工作。首先，需要将 gtk2hs 包添加到构建依赖项列表中。还有 Glade XML 文件的问题。

早些时候，我们编写了一个 PodLocalMain.hs 文件，它简单假设此文件名为 podresources.glade 并存储在当前工作目录中。对于真实的系统范围安装，我们不能做这样的假设。此外，不同的系统可能将文件放置在不同位置。

Cabal 提供了一种解决这个问题的方法。它自动生成一个导出函数的模块，可以查询环境。我们必须在 Cabal 描述文件中添加一个 Data-files 行。此文件命名将作为系统范围安装一部分的所有数据文件。然后，Cabal 将导出一个 Paths_pod 模块（"pod"部分来自 Cabal 文件中的 Name 行），我们可以在运行时查询其位置。

这是我们的新 Cabal 描述文件：

```cabal
-- ch24/pod.cabal
Name: pod
Version: 1.0.0
Build-type: Simple
Build-Depends: HTTP, HaXml, network, HDBC, HDBC-sqlite3, base,
               gtk, glade
Data-files: podresources.glade
Executable: pod
Main-Is: PodCabalMain.hs
GHC-Options: -O2
```

并且，与之配套的 PodCabalMain.hs：

```haskell
-- file: ch23/PodCabalMain.hs
module Main where
import qualified PodMainGUI
import Paths_pod(getDataFileName)
main =
    do gladefn <- getDataFileName "podresources.glade"
       PodMainGUI.main gladefn
```

## 练习

1. 如果对 xmlNew 的调用返回 Nothing，则显示有帮助的 GUI 错误消息。
2. 修改 podcatcher，使其能够从单一代码库运行 GUI 或命令行界面。提示：将公共代码移出 PodMainGUI.hs，然后有两个不同的 Main 模块——一个用于 GUI，一个用于命令行。
3. 为什么 guiFetch 组合工作函数而不是两次调用 statusWindow？
