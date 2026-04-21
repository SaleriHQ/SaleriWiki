---
title: "RWH 第12章-条形码识别"
source: "Clippings/RWH-Chapters-zh/第12章-条形码识别.md"
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

# RWH 第12章-条形码识别

## 本章概述

本章通过实现 EAN-13/UPC-A 条形码识别系统，展示图像处理、数字化信号处理和条形码解码算法的实际应用。

## 关键概念

- **EAN-13/UPC-A**: 零售条形码标准、13/12 位数字
- **图像处理**: 灰度转换、像素数组
- **数字化信号**: 阈值化、边缘检测
- **条形码解码**: 位模式匹配、校验位验证
- **模式识别**: Run-length encoding、峰检测
- **错误处理**: Maybe、Either 优雅处理

## 核心代码示例

```haskell
-- 条形码数字位模式
patterns :: [[Bool]]
patterns = [[True,False,True],
            [False,True,False],
            -- ... 0-9 的模式
           ]

-- 数字化信号
type Signal = [Int]
type Run = (Int, Int)  -- (长度, 值)

runs :: Signal -> [Run]
runs [] = []
runs (x:xs) = let (len, vals) = span (== x) xs
              in (len+1, x) : runs vals

-- 校验位验证
checkDigit :: [Int] -> Int
checkDigit digits = (10 - sum weighted) `mod` 10
  where weighted = zipWith (*) digits [1,3,1,3...]
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/模式匹配]]
- [[wiki/concepts/递归]]
