---
title: "How I run multiple $10K MRR companies on a $20/month tech stack"
source: https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack
author: Steve Hanov
published: 2026-03
created: 2026-04-21
type: source
tags:
  - source
  - bootstrap
  - tech-stack
  - business
related:
  - "[[Plan/Language Learn]]"
  - "[[Plan/Language Learn SOP]]"
---

# How I run multiple $10K MRR companies on a $20/month tech stack

## 核心观点

作者 Steve Hanov 分享了他用极低成本（$20/月）运行多个 MRR $10K 级别公司的技术方案，核心是**极简架构**：

1. **VPS 单服务器** — $5-10/月的 DigitalOcean/Linode，1GB RAM + swapfile 足够
2. **Go 语言** — 静态编译单二进制，无依赖地狱，高并发
3. **SQLite + WAL 模式** — 本地数据库比远程 PostgreSQL 更快，支持并发
4. **本地 AI** — Ollama 迭代 → VLLM 生产，支持 8K context
5. **OpenRouter** — 统一 API 接口，自动降级
6. **GitHub Copilot** — 按请求计费而非按 token

## 关键要点

### 1. 服务器选择

| 推荐 | 价格 | 说明 |
|------|------|------|
| DigitalOcean/Linode | $5-10/月 | 单 VPS 足够 |
| 不推荐 AWS | - | 控制台复杂，容易超支 |

> 1GB RAM 听起来很少，但对 Go 应用绰绰有余

### 2. Go 优势

- 编译成**单二进制**，`scp` 到服务器即可运行
- 无 `pip install` / 虚拟环境地狱
- 轻松处理每秒数千请求
- LLM 易于理解和生成

```go
// 完整生产级服务器
func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, your MRR is safe here.")
    })
    http.ListenAndServe(":8080", nil) 
}
```

### 3. SQLite WAL 模式

```sql
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
```

- 读者不阻塞写者
- 写者不阻塞读者
- 单 .db 文件支持数千并发用户
- 比远程 PostgreSQL 更快（无网络开销）

### 4. 本地 AI 升级路径

```
Ollama (迭代) → VLLM (生产) → Transformer Lab (微调)
```

- VLLM 使用 PagedAttention，并发 8-16 请求批量处理
- RTX 3090 24GB 足够运行 32B 模型
- [laconic](https://github.com/smhanov/laconic) - 8K context 优化

### 5. Copilot 技巧

- **按请求计费**，不是按 token
- 写详细 prompt + "keep going until all errors are fixed"
- 30 分钟代码修改 = $0.04

## 成本对比

| 方案 | 月成本 | 说明 |
|------|--------|------|
| **本文方案** | $20 | VPS + SQLite + 本地 AI |
| 企业方案 | $300+ | AWS EKS + RDS + NAT Gateway |

## 与 Language Learn 的关联

本文的极简架构非常适合 Language Learn 项目：

| 本文建议 | Language Learn 应用 |
|----------|-------------------|
| VPS 单服务器 | 自托管部署 [[Plan/Language Learn SOP]] |
| Go/静态编译 | 后端可考虑 Go/Rust |
| SQLite WAL | 词典服务用 SQLite FTS |
| 本地 AI | 可用 Ollama 做单词释义增强 |
| OpenRouter | 预留 AI fallback 路由 |

**实践建议**：
- MVP 阶段用 SQLite 存储用户数据
- 词典服务用 SQLite FTS5 全文搜索
- 生产规模后再考虑 PostgreSQL
- 本地 GPU 做 batch AI 任务（如单词复习推荐）

## 来源

- [原文链接](https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack)
- [smhanov/auth](https://github.com/smhanov/auth) - SQLite 认证库
- [laconic](https://github.com/smhanov/laconic) - 本地 AI 研究员
- [llmhub](https://github.com/smhanov/llmhub) - LLM 统一接口
