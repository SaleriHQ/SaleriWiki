---
title: "RWH 第26章-布隆过滤器"
source: "Clippings/RWH-Chapters-zh/第26章-布隆过滤器.md"
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
  - "[[wiki/concepts/类型系统]]"
---

# RWH 第26章-布隆过滤器

## 本章概述

本章通过实现布隆过滤器数据结构，展示 ST Monad、可变数组 (STArray) 编程和性能优化技术，以及 Cabal 包发布。

## 关键概念

- **布隆过滤器**: 概率数据结构、空间效率
- **误判率**: FP rate、哈希函数数量
- **ST Monad**: 纯代码中的可变状态
- **STArray**: 可变数组、freeze/thaw
- **MArray**: 通用可变数组接口
- **Cabal**: Haskell 包管理、构建发布

## 核心代码示例

```haskell
import Data.Array.ST
import Data.Array.MArray
import Control.Monad.ST
import Data.Bits (shiftL, (.&.))
import Data.Hashable (hash)

-- 布隆过滤器
data BloomFilter a = Bloom {
  bfHashFuns :: [a -> Int],
  bfBitArray :: STArray s Int Bool
}

-- 创建布隆过滤器
newBloom :: Int -> [a -> Int] -> ST s (BloomFilter a)
newBloom size hashes = do
  arr <- newArray (0, size-1) False
  return $ Bloom hashes arr

-- 添加元素
insert :: Eq a => BloomFilter a -> a -> ST s ()
insert bf elt = do
  let indices = map (\h -> h elt `mod` arraySize) (bfHashFuns bf)
  mapM_ (\i -> writeArray (bfBitArray bf) i True) indices
  where arraySize = rangeSize $ bounds (bfBitArray bf)

-- 查询
member :: Eq a => BloomFilter a -> a -> ST s Bool
member bf elt = do
  let indices = map (\h -> h elt `mod` arraySize) (bfHashFuns bf)
  and $ map (\i -> readArray (bfBitArray bf) i) indices
  where arraySize = rangeSize $ bounds (bfBitArray bf)
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/单子]]
