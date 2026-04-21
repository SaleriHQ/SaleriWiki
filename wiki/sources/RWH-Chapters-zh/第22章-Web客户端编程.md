---
title: "RWH 第22章-Web客户端编程"
source: "Clippings/RWH-Chapters-zh/第22章-Web客户端编程.md"
author: "Bryan O'Sullivan, Don Stewart, John Goerzen"
translator: "Claude"
created: 2026-04-11
updated: 2026-04-11
type: source
tags:
  - source
  - haskell
  - book
  - rwh
related:
  - "[[wiki/concepts/IO Monad]]"
  - "[[wiki/concepts/单子]]"
---

# RWH 第22章-Web客户端编程

## 本章概述

本章介绍 Haskell Web 客户端编程，包括 HTTP 包使用、网络请求、RSS 解析和 Podcast 下载器实现。

## 关键概念

- **HTTP 包**: Network.HTTP
- **请求/响应**: Request、Response、getResponseBody
- **连接管理**: 代理、超时、重试
- **RSS 解析**: Feed、Entry、item 提取
- **内容下载**: ByteString 保存、进度追踪
- **错误处理**: HttpException、网络超时

## 核心代码示例

```haskell
import Network.HTTP
import Network.URI (parseURI)

-- 简单 GET 请求
download :: String -> IO String
download url = do
  resp <- simpleHTTP (getRequest url)
  getResponseBody resp

-- 带错误处理
downloadSafe :: String -> IO (Either String String)
downloadSafe url = do
  result <- simpleHTTP (getRequest url)
  case result of
    Left err -> return $ Left (show err)
    Right resp -> return $ Right (rspBody resp)

-- RSS 解析
import Text.XML.Light (parseXML, filterElementName)

parseRSS :: String -> [String]
parseRSS xml = do
  let content = parseXML xml
  let items = filterElementName (== "item") content
  concatMap (filterElementName (== "title") . elContent) items

-- 下载器
downloadFile :: String -> FilePath -> IO ()
downloadFile url path = do
  content <- download url
  writeFile path content
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/单子]]
- [[wiki/concepts/类型系统]]
