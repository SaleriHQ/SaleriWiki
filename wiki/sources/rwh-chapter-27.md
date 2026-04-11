---
title: "RWH 第27章-套接字与系统日志"
source: "Clippings/RWH-Chapters-zh/第27章-套接字与系统日志.md"
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

# RWH 第27章-套接字与系统日志

## 本章概述

本章介绍 Haskell 网络编程，包括 UDP/TCP 套接字编程、Syslog 协议实现和并发服务器设计。

## 关键概念

- **UDP 套接字**: 无连接、快速
- **TCP 套接字**: 面向连接、可靠
- **Syslog 协议**: 系统日志、UDP 端口 514
- **Network 包**: Network.Socket
- **并发服务器**: forkIO、连接池
- **字节处理**: ByteString、网络序列化

## 核心代码示例

```haskell
import Network.Socket
import Network.Socket.ByteString (send, recv)

-- TCP 服务器
tcpServer :: PortID -> (Socket -> IO ()) -> IO ()
tcpServer port handler = do
  sock <- socket AF_INET Stream defaultProtocol
  bindSocket sock (SockAddrInet port iNADDR_ANY)
  listen sock 5
  forever $ do
    (conn, addr) <- accept sock
    forkIO (handler conn)
    return ()

-- TCP 客户端
tcpClient :: HostName -> PortID -> IO ()
tcpClient host port = do
  sock <- socket AF_INET Stream defaultProtocol
  addr <- inetAddr host port
  connect sock addr
  send sock "Hello"
  recv sock 1024

-- UDP 服务器
udpServer :: PortID -> IO ()
udpServer port = do
  sock <- socket AF_INET Datagram defaultProtocol
  bindSocket sock (SockAddrInet port iNADDR_ANY)
  forever $ do
    (msg, addr) <- recvFrom sock 1024
    sendTo sock "ACK" addr

-- Syslog 消息
data SyslogMsg = SyslogMsg {
  priority :: Int,
  timestamp :: String,
  hostname :: String,
  message :: String
}
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/单子]]
- [[wiki/concepts/并发编程]]
