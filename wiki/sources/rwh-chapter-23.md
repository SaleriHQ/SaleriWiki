---
title: "RWH 第23章-GUI编程"
source: "Clippings/RWH-Chapters-zh/第23章-GUI编程.md"
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

# RWH 第23章-GUI编程

## 本章概述

本章介绍使用 gtk2hs 进行 Haskell GUI 编程，包括事件驱动编程、控件使用、布局管理和图形界面构建。

## 关键概念

- **gtk2hs**: Haskell GTK+ 绑定
- **事件驱动**: Signal、Callback、onEvent
- **控件**: Button、Entry、Label、Window
- **布局**: VBox、HBox、Table、fixed
- **回调**: type Handler、onClicked、onActivate
- **主循环**: GTKMain、mainGUI

## 核心代码示例

```haskell
import Graphics.UI.Gtk

main :: IO ()
main = do
  initGUI
  -- 创建窗口
  window <- windowNew
  set window [ windowTitle := "Hello World",
               containerBorderWidth := 10 ]

  -- 创建按钮
  button <- buttonNewWithLabel "Click Me"
  on button buttonActivated $ do
    putStrLn "Button clicked!"

  -- 布局
  containerAdd window button

  -- 显示
  widgetShowAll window

  -- 主循环
  mainGUI

-- 回调示例
onClicked :: Button -> IO () -> IO (ConnectId Button)
onActivate :: Action -> IO () -> IO (ConnectId Action)

-- 布局
boxPackStart :: Box -> Widget -> Packing -> Fill -> Padding -> IO ()
boxPackEnd :: Box -> Widget -> Packing -> Fill -> Padding -> IO ()
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/IO Monad]]
- [[wiki/concepts/单子]]
- [[wiki/concepts/类型类]]
