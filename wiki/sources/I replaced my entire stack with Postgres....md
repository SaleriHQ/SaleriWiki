---
title: "I replaced my entire stack with Postgres"
source: "https://www.youtube.com/watch?v=TdondBmyNXc"
author:
  - The Coding Gopher
created: 2026-04-27
type: source
tags:
  - source
  - postgres
  - backend
  - database
---

## 摘要

本文是 The Coding Gopher 的视频，讲述如何使用 PostgreSQL 替代整个技术栈（Redis、RabbitMQ、Elasticsearch、向量数据库等），通过 Postgres 的丰富扩展生态实现"一刀切"的架构。

## 核心论点

**问题**：现代软件工程被云厂商"操控"，为构建简单应用需要拼凑大量专用微服务，导致成本高昂、架构脆弱。

**解决方案**：使用 PostgreSQL 这一30年历史的开源数据库，通过其强大的扩展生态替代几乎所有云依赖。

## PostgreSQL 的核心优势

### 1. JSONB 数据类型（替代 MongoDB）

- **JSONB** (Binary)：在插入时将 JSON 转换为二进制格式，避免每次查询解析
- **GIN 索引**：倒排索引，直接映射键到行 ID，实现毫秒级嵌套属性查询
- 在单一 ACID 事务中查询嵌套文档并与关系表 JOIN

### 2. 任务队列（替代 RabbitMQ/Redis）

- 使用 `SKIP LOCKED` 实现并发无锁队列
- 两个 worker 同时抢同一行时，被锁住的 worker 直接跳过，不会死锁
- 可处理每秒数千个任务

### 3. 全文搜索（替代 Elasticsearch）

- **TS Vector / TS Query**：去除停用词、词干提取（如 running → run）
- **pg_trigram 扩展**：三字母分块实现模糊匹配/容错搜索
- 无需同步数据到外部集群

### 4. 向量搜索（替代 Pinecone）

- **pgvector 扩展**：存储高维向量，紧邻核心业务数据
- **HNSW 索引**：分层可导航小世界图，近似最近邻搜索
- 避免"混合搜索问题"：跨数据库查询语义相似+关系过滤极慢

### 5. 地理空间（PostGIS，替代专业 GIS 系统）

- **GiST 索引**：广义搜索树，绘制简单边界框快速过滤
- 查询复杂地理多边形内咖啡店：先丢弃无关数据点，再精确计算

### 6. 时序数据（替代 TimescaleDB/InfluxDB）

- **声明式分区**：按日期/月自动拆分大表
- **BRIN 索引**：只存储物理块的最小/最大时间戳
- 查询时跳过不包含目标时间范围的磁盘页

### 7. 物化视图（替代 Snowflake 数据仓库）

- **Materialized View**：运行一次查询，结果物理保存到磁盘
- `REFRESH MATERIALIZED VIEW CONCURRENTLY`：后台增量更新，不锁用户

### 8. API 层（替代 Node.js/Python 中间件）

- **PostgREST / pg_graphql**：分析 schema 自动生成 REST/GraphQL API
- **行级安全策略 (RLS)**：数据库内直接写加密策略，用户只能读写自己数据
- 数据库本身成为后端

## 局限性与适用场景

| 场景 | PostgreSQL 适用性 |
|------|------------------|
| 中小规模应用 | ✅ 最佳选择 |
| 需要水平分片 | ⚠️ 复杂，不推荐 |
| 每秒百万级事件摄取 | ❌ 需要专用分布式工具 |
| 百万级并发 WebSocket | ❌ 需要内存缓存层 |

**结论**：在突破大规模企业级阈值之前，使用 PostgreSQL 是最明智、最具成本效益的工程决策。

## 与维基的关联

此来源涉及：
- [[wiki/concepts/函数式编程]] - 声明式数据处理思想
- [[wiki/sources/RWH-Chapters-zh/第21章-使用数据库]] - 数据库基础
