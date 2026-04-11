---
title: "RWH 第13章-数据结构"
source: "Clippings/RWH-Chapters-zh/第13章-数据结构.md"
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

# RWH 第13章-数据结构

## 本章概述

本章介绍 Haskell 标准库中的核心数据结构：关联列表、Data.Map、Data.Set、树结构和图算法。

## 关键概念

- **关联列表**: [(key, value)]、简单键值对
- **Data.Map**: 高效键值存储、平衡 BST 实现
- **Data.Set**: 无序唯一集合、集合运算
- **树结构**: 二叉搜索树、AVL 树
- **图算法**: 邻接表、深度优先搜索、广度优先搜索
- **模块组织**: Data.List、Data.Map、Data.Set

## 核心代码示例

```haskell
import Data.Map (Map)
import qualified Data.Map as Map
import Data.Set (Set)
import qualified Data.Set as Set

-- Map 操作
insertWith :: Ord k => (v -> v -> v) -> k -> v -> Map k v -> Map k v
fromList :: Ord k => [(k, v)] -> Map k v
lookup :: Ord k => k -> Map k v -> Maybe v

-- Set 操作
empty :: Set a
insert :: Ord a => a -> Set a -> Set a
union :: Ord a => Set a -> Set a -> Set a
intersection :: Ord a => Set a -> Set a -> Set a

-- 二叉搜索树
data Tree a = Empty | Node (Tree a) a (Tree a)
insert' :: Ord a => a -> Tree a -> Tree a
insert' x Empty = Node Empty x Empty
insert' x (Node l v r)
  | x < v     = Node (insert' x l) v r
  | x > v     = Node l v (insert' x r)
  | otherwise = Node l v r
```

## 与维基的关联

此章节涉及:
- [[wiki/concepts/代数数据类型]]
- [[wiki/concepts/类型系统]]
- [[wiki/concepts/递归]]
