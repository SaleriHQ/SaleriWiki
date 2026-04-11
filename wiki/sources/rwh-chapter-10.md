---
title: "RWH 第10章-案例研究-解析二进制数据格式"
source: "Clippings/RWH-Chapters-zh/第10章-案例研究-解析二进制数据格式.md"
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
  - "[[wiki/concepts/代数数据类型]]"
  - "[[wiki/concepts/模式匹配]]"
---

# RWH 第10章-案例研究-解析二进制数据格式

## 本章概述

本章通过解析 netpbm 图像格式中的 PGM 文件，深入讲解二进制数据解析技术，包括 Word8 类型、ByteString 处理和渐进式重构。

## 关键概念

- **二进制解析**: Word8、ByteString、Bit 操作
- **netpbm 格式**: PBM/PGM/PPM、文本/二进制
- **PGM 格式**: 灰度图像、头部+像素数据
- **State Monad**: 解析状态传递
- **交错格式**: 大端/小端、Word8 数组
- **渐进重构**: 识别模式、抽象提取

## 核心代码示例

```haskell
import Data.ByteString as B
import Data.Word8 (Word8)

-- PGM 解析器
data Greymap = Greymap {
  gmWidth  :: Int,
  gmHeight :: Int,
  gmMaxGrey :: Int,
  gmBitmap :: B.ByteString
} deriving (Show)

parseP5 :: B.ByteString -> Maybe (Greymap, B.ByteString)
parseP5 s =
  case matchHeader (B.pack "P5") s of
    Nothing -> Nothing
    Just s1 ->
      case getNat s1 of
        Nothing -> Nothing
        Just (width, s2) ->
          case getNat s2 of
            -- ... 继续解析
            Nothing -> Nothing
            Just (height, s3) ->
              -- 解析更多字段...
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/模式匹配]]
- [[wiki/concepts/递归]]
