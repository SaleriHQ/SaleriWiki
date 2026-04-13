# 起因

市面上的软件收费不好用 Or 开源的软件不好用，老旧，需要重构，集成性差

# 目标

制作一个**私人的语言学习 SaaS 平台**，为用户提供服务，支持会员制。我负责管理所有人的词库和数据。

---

# 📐 一、项目架构计划（Architecture Plan）

## 1. 项目定位

> 一个**多租户 SaaS 语言学习平台**，支持：

- 📚 PDF / EPUB 阅读
- 📖 单词/句子标注
- 📘 本地 + 在线词典
- 🖼 图片辅助记忆
- 🧠 Anki 导出
- 👥 会员制服务
- 🔐 用户认证与数据隔离

---

## 2. 总体架构

```
浏览器客户端
 ├── 阅读器（EPUB / PDF）
 ├── 标注系统
 ├── 单词管理
 │
 ↓ REST API
后端服务（Node.js / Bun）
 ├── 用户认证（Clerk / 自建）
 ├── 业务逻辑
 ├── 词典 API
 ├── 翻译 API
 ├── 图片 API 代理
 └── Anki 导出 API
 │
 ↓
PostgreSQL（主数据库）
 ├── 用户表
 ├── 词库表
 ├── 标注表
 ├── 书籍表
 └── 会员表
 │
 ↓
S3 / R2（文件存储）
 ├── 书籍文件
 └── 用户图片
```

---

## 3. 技术栈

### 前端

- Nuxt 3（SPA 模式）
- Vue 3 + Composition API
- SCSS
- Pinia（状态管理）
- ~~IndexedDB~~ → 改用 API 调用

### 阅读引擎

- EPUB：epub.js
- PDF：pdf.js

### 数据库

- **PostgreSQL**（主存储）
- Redis（缓存、会话）

### 后端

- Node.js / Bun / Hono / Fastify
- Prisma（Drizzle ORM）
- ~~Nuxt Nitro~~ → 独立后端

### 部署

- ~~Docker 自托管~~ → 云服务部署
- Vercel / Railway / Fly.io（后端）
- Supabase / Neon（PostgreSQL）

---

---

## 4. 用户使用流程

```
┌─────────────────────────────────────────────────────────────┐
│                      1. 用户打开软件                         │
│                    （登录/注册认证）                          │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  2. 导入书籍                                 │
│  ┌─────────┐    ┌─────────┐    ┌──────────────────────┐   │
│  │上传文件   │ → │解析内容   │ → │存储到服务器             │   │
│  │EPUB/PDF │    │提取文本   │    │S3 + PostgreSQL        │   │
│  └─────────┘    └─────────┘    └──────────────────────┘   │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  3. 阅读页面                                 │
│  ┌─────────┐    ┌─────────┐    ┌──────────────────────┐   │
│  │加载书籍  │ → │智能标注  │ → │词典查词               │   │
│  │美观排版  │    │词库高亮  │    │服务端离线词典          │   │
│  └─────────┘    └─────────┘    └──────────────────────┘   │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  4. 学习/复习                                │
│  ┌─────────┐    ┌─────────┐    ┌──────────────────────┐   │
│  │单词复习  │ → │导出Anki │ → │复习进度跟踪           │   │
│  │计划生成  │    │格式导出  │    │下次阅读位置           │   │
│  └─────────┘    └─────────┘    └──────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### 核心功能说明

| 步骤 | 功能 | 说明 |
|------|------|------|
| 2.导入书籍 | 文件上传 | 用户上传 EPUB/PDF |
| 2.解析内容 | 文本提取 | 服务端解析书籍内容存储 |
| 3.智能标注 | 单词高亮 | 根据用户词库自动标注已学习/待学习单词 |
| 3.词典查词 | 离线查词 | 服务端部署本地词典，无需联网 |
| 4.复习 | Anki 导出 | 生成复习卡包 |

---

## 5. 核心模块设计

### 5.1 书籍管理模块

#### 功能：

- 上传 EPUB / PDF 文件
- 服务端解析提取文本内容
- 书籍元数据提取（标题、作者、封面）
- 全文内容存储（用于搜索和单词统计）

#### 数据库结构：

```sql
-- 书籍表
CREATE TABLE books (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255),
  file_url TEXT NOT NULL,           -- S3 存储地址
  file_type VARCHAR(10) NOT NULL,   -- 'epub' | 'pdf'
  file_size BIGINT,                 -- 文件大小
  content TEXT,                     -- 解析后的纯文本（用于搜索）
  total_words INT,                  -- 总词数
  unique_words INT,                 -- 不重复词数
  cover_url TEXT,                   -- 封面图片地址
  language VARCHAR(10) DEFAULT 'en', -- 书籍语言
  reading_progress FLOAT DEFAULT 0, -- 阅读进度 0-100%
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_books_user ON books(user_id);
CREATE INDEX idx_books_language ON books(language);
```

#### 数据流：

```
用户上传 EPUB
    ↓
服务端接收文件 → 上传到 S3
    ↓
解析 EPUB（提取 HTML/纯文本）
    ↓
文本内容存入 PostgreSQL
    ↓
统计词频、生成元数据
    ↓
返回书籍信息给前端
```

---

### 5.2 阅读器模块

#### 功能：

- 加载 EPUB / PDF
- 文本选择（word / sentence）
- 高亮与标注
- **智能单词标注**：根据用户词库自动区分已学习/待学习单词

#### 阅读器特色功能

| 功能 | 说明 |
|------|------|
| 单词高亮 | 已学习单词绿色，已标注单词蓝色，待学习单词无色 |
| 点击查词 | 点击任意单词弹出词典释义 |
| 进度同步 | 自动保存阅读位置，下次打开从上次位置继续 |

#### 组件划分：

```
components/
 ├── EpubReader.vue
 ├── PdfViewer.vue
 ├── TextSelectionOverlay.vue
 ├── WordHighlight.vue         # 智能单词标注
 └── DictionaryPopover.vue     # 查词弹窗
```

---

### 5.3 书籍管理模块

#### 功能：

- 上传 EPUB / PDF 文件
- 服务端解析提取文本内容
- 书籍元数据提取（标题、作者、封面）
- 全文内容存储（用于搜索和单词统计）

#### 数据库结构：

```sql
-- 书籍表
CREATE TABLE books (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255),
  file_url TEXT NOT NULL,           -- S3 存储地址
  file_type VARCHAR(10) NOT NULL,   -- 'epub' | 'pdf'
  file_size BIGINT,                 -- 文件大小
  content TEXT,                     -- 解析后的纯文本（用于搜索）
  total_words INT,                  -- 总词数
  unique_words INT,                 -- 不重复词数
  cover_url TEXT,                   -- 封面图片地址
  language VARCHAR(10) DEFAULT 'en', -- 书籍语言
  reading_progress FLOAT DEFAULT 0, -- 阅读进度 0-100%
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- 阅读进度表
CREATE TABLE reading_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  book_id UUID NOT NULL REFERENCES books(id),
  position JSONB,                  -- EPUB: CFI, PDF: page
  percentage FLOAT DEFAULT 0,     -- 阅读百分比
  last_position TEXT,             -- 最后阅读位置（文本锚点）
  last_read_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(user_id, book_id)
);
```

#### 数据流：

```
用户上传 EPUB
    ↓
服务端接收文件 → 上传到 S3
    ↓
解析 EPUB（提取 HTML/纯文本）
    ↓
文本内容存入 PostgreSQL
    ↓
统计词频、生成元数据
    ↓
返回书籍信息给前端
```

---

### 5.5 标注系统（核心）

#### 数据库结构：

```sql
CREATE TABLE annotations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  book_id UUID REFERENCES books(id),
  type VARCHAR(20) NOT NULL CHECK (type IN ('word', 'sentence')),
  content TEXT NOT NULL,
  context TEXT,
  translation TEXT,
  images TEXT[],
  source VARCHAR(255),
  position JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_annotations_user ON annotations(user_id);
CREATE INDEX idx_annotations_book ON annotations(book_id);
CREATE INDEX idx_annotations_type ON annotations(type);
```

---

### 5.6 词典服务（服务端部署）

#### 设计理念

- **服务端部署本地词典**：词典数据存储在服务器，用户查询时调用 API
- **离线可用**：无需第三方 API，无网络请求限制
- **隐私保护**：用户查询数据不泄露给第三方
- **多语言支持**：可同时部署多个词典（英汉、英英、日汉等）

#### 词典格式

| 格式 | 特点 | 生态 |
|------|------|------|
| **MDict (.mdx)** | 流行，压缩率高 | 词典资源丰富 |
| StarDict (.dict) | 老牌格式 | 工具较多 |
| DSL (.dsl) | ABBYY Lingvo | 欧洲语言词典多 |

#### 开源词典资源

```
词典库：
- https://github.com/skywind3000/ECDICT      # 英汉词典（推荐）
- https://github.com/szqc/english-dictionary  # 英汉
- https://github.com/isyourlife/awesome-dict  # MDict 词典合集

词典格式转换工具：
- https://github.com/skywind3000/mdict-tools
- https://github.com/nicklhy/mdict_parser
```

#### 服务架构

```
客户端                         服务端
  │                              │
  │  查询 "hello"               │
  ├─────────────────────────────►
  │                              │
  │                        ┌─────┴─────┐
  │                        │ 词典服务   │
  │                        │ /api/dict │
  │                        └─────┬─────┘
  │                              │
  │                        ┌─────┴─────┐
  │                        │ 本地词典  │
  │                        │ /data/dict│
  │                        │  ├─ en_zh │
  │                        │  ├─ en_en │
  │                        │  └─ ja_zh │
  │                        └───────────┘
  │                              │
  │  返回：释义、音标、例句...    │
  ◄──────────────────────────────┘
```

#### 词典服务 API

```typescript
// 查询接口
GET /api/dictionary/lookup?word=hello&dict=en_zh

// 返回格式
{
  "word": "hello",
  "phonetic": "/həˈloʊ/",
  "definitions": [
    {
      "partOfSpeech": "n.",
      "meaning": "问候语；打招呼"
    },
    {
      "partOfSpeech": "v.",
      "meaning": "向...打招呼"
    }
  ],
  "examples": [
    "Hello, how are you?",
    "She said hello to everyone."
  ],
  "dict": "en_zh"
}
```

#### 词典加载策略

```typescript
// 服务启动时加载词典到内存
class DictionaryService {
  private dicts: Map<string, DictIndex> = new Map()

  async loadDictionary(name: string) {
    const dictPath = `/data/dict/${name}.mdx`
    // 使用 mdict-parser 解析
    const dict = await MDictParser.load(dictPath)
    this.dicts.set(name, dict)
  }

  lookup(word: string, dictName: string) {
    return this.dicts.get(dictName)?.lookup(word)
  }
}
```

#### 词库整合

用户查询单词时，系统自动：
1. 查询词典获取释义
2. 同时检查用户词库（是否已学习）
3. 返回释义 + 单词状态（已学习/待学习）

---

### 5.5 智能标注系统

#### 功能

根据用户词库，在阅读时自动标注单词状态：

| 状态 | 颜色 | 条件 |
|------|------|------|
| 已学习 | 🟢 绿色 | 单词在用户词库中且标记为"已掌握" |
| 待复习 | 🔵 蓝色 | 单词在用户词库中，需要复习 |
| 待学习 | ⚪ 默认 | 单词不在用户词库中 |
| 生词 | 🟡 黄色 | 系统推断为高频必学词汇 |

#### 推断逻辑

```typescript
// 推断待学习单词
async function inferNewWords(text: string, userId: string) {
  // 1. 获取用户已学单词
  const learnedWords = await getLearnedWords(userId)

  // 2. 提取文本中的单词
  const words = extractWords(text)

  // 3. 过滤已学习的
  const newWords = words.filter(w => !learnedWords.has(w))

  // 4. 词频分析（使用常用词表）
  const commonWords = await getCommonWordsSet(language)
  const toLearn = newWords.filter(w => commonWords.has(w))

  return toLearn
}
```

---

### 5.6 阅读进度追踪

#### 功能

- 自动保存阅读位置
- 多设备同步
- 下次打开从上次位置继续
- 阅读统计数据

#### 追踪数据

```typescript
interface ReadingProgress {
  bookId: string
  position: {
    type: 'epub' | 'pdf'
    cfi?: string      // EPUB CFI 位置
    page?: number     // PDF 页码
    percentage: number
  }
  lastReadAt: Date
  totalReadingTime: number
}
```

---

### 5.7 图片系统

#### 功能：

- 单词 → 图片搜索
- 图片选择 → 插入卡片

#### 数据库结构：

```sql
CREATE TABLE images (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  url TEXT NOT NULL,
  source TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

### 5.8 单词管理系统

#### 功能：

- 单词本
- 标注列表
- 复习状态（可扩展）

#### 数据库结构：

```sql
CREATE TABLE words (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  word TEXT NOT NULL,
  translation TEXT,
  pronunciation TEXT,
  images TEXT[],
  notes TEXT,
  mastery_level INT DEFAULT 0,  -- 0-5 掌握程度
  review_count INT DEFAULT 0,
  last_reviewed_at TIMESTAMP,
  next_review_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_words_user ON words(user_id);
CREATE INDEX idx_words_word ON words(word);
CREATE INDEX idx_words_review ON words(next_review_at);
```

---

### 5.9 会员系统

#### 数据库结构：

```sql
CREATE TYPE membership_tier AS ENUM ('free', 'pro', 'team');

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255),
  name VARCHAR(255),
  membership membership_tier DEFAULT 'free',
  membership_expires_at TIMESTAMP,
  storage_used BIGINT DEFAULT 0,
  storage_limit BIGINT DEFAULT 1073741824, -- 1GB for free
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id),
  stripe_customer_id VARCHAR(255),
  stripe_subscription_id VARCHAR(255),
  tier membership_tier NOT NULL,
  status VARCHAR(50),
  current_period_end TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);
```

---

### 5.10 Anki 导出模块

#### 功能：

- 导出用户选中的单词到 Anki
- 支持自定义卡片模板
- 支持 CSV 导出

#### API：

```
POST /api/anki/export
POST /api/anki/add
GET  /api/anki/templates
```

---

## 6. 多租户数据隔离

### 策略：行级安全（Row Level Security）

```sql
-- PostgreSQL RLS
ALTER TABLE annotations ENABLE ROW LEVEL SECURITY;
ALTER TABLE words ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_isolation ON annotations
  USING (user_id = current_setting('app.current_user_id')::UUID);

CREATE POLICY user_isolation ON words
  USING (user_id = current_setting('app.current_user_id')::UUID);
```

### API 层隔离

```ts
// 每个 API 自动注入 user_id
async function withUser(ctx, handler) {
  const userId = ctx.get('userId') // 从 JWT 获取
  ctx.set('userId', userId)
  await pool.query(`SET LOCAL app.current_user_id = '${userId}'`)
  return handler(ctx)
}
```

---

## 7. 路由设计

```
前端（Nuxt）
/                    首页
/login               登录
/register            注册
/pricing             定价
/dashboard           用户面板
/reader/[id]         阅读器
/library             书库
/wordbook            单词本
/settings            设置
/admin               管理后台（可选）

后端 API
认证
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/logout
GET    /api/auth/me

书籍管理
GET    /api/books              # 获取用户书籍列表
POST   /api/books/upload        # 上传书籍（支持 EPUB/PDF）
GET    /api/books/:id          # 获取书籍详情
DELETE /api/books/:id          # 删除书籍
GET    /api/books/:id/content   # 获取书籍文本内容（分页）

阅读进度
GET    /api/progress/:bookId   # 获取阅读进度
PUT    /api/progress/:bookId   # 更新阅读进度

标注
GET    /api/annotations         # 获取用户标注列表
POST   /api/annotations         # 创建标注
PUT    /api/annotations/:id     # 更新标注
DELETE /api/annotations/:id     # 删除标注
GET    /api/annotations/book/:bookId  # 获取某本书的标注

单词管理
GET    /api/words               # 获取用户单词列表
POST   /api/words               # 添加单词
PUT    /api/words/:id           # 更新单词
DELETE /api/words/:id           # 删除单词
POST   /api/words/import        # 导入单词
POST   /api/words/check         # 批量检查单词状态（用于智能标注）

词典服务
GET    /api/dictionary/lookup  # 查词（服务端词典）
GET    /api/dictionary/dicts    # 获取可用词典列表

导出
POST   /api/anki/export         # 导出到 Anki（CSV/APKG）
POST   /api/export/csv          # CSV 导出

上传
POST   /api/upload/image        # 上传图片
POST   /api/upload/book         # 上传书籍文件

支付
POST   /api/webhook/stripe      # Stripe Webhook
```

---

## 8. 会员权益设计

| 功能 | Free | Pro | Team |
|------|------|-----|------|
| 书籍数量 | 3 | 无限 | 无限 |
| 单词数量 | 500 | 无限 | 无限 |
| 存储空间 | 1GB | 10GB | 50GB |
| 图片辅助 | ❌ | ✅ | ✅ |
| Anki 导出 | ✅ | ✅ | ✅ |
| 本地词典 | ❌ | ✅ | ✅ |
| 团队共享 | ❌ | ❌ | ✅ |
| 价格 | 免费 | ¥30/月 | ¥80/月 |

---

# 🚀 二、开发计划（Development Plan）

---

## 🟢 第一阶段：基础架构（2–3 周）

### 目标：

搭建完整的 SaaS 基础设施

### 功能：

- 用户认证系统（注册/登录/JWT）
- PostgreSQL 数据库设计
- 基础 CRUD API
- 会员系统框架

### 技术重点：

- Prisma / Drizzle ORM
- Clerk 或自建 Auth
- PostgreSQL RLS

---

## 🟡 第二阶段：MVP 阅读功能（2–3 周）

### 功能：

- **书籍上传**：EPUB/PDF 上传到 S3，服务端解析提取文本
- **阅读器**：EPUB 阅读器 + 文本选择
- **服务端词典**：部署本地词典（ECDICT 英汉）
- **单词保存**：点击查词 → 保存到数据库
- **单词列表**：查看已保存的单词
- **进度追踪**：自动保存阅读位置

### 技术重点：

- epub.js 集成
- 服务端 EPUB 解析（unzip + 文本提取）
- MDict 词典加载与查询
- 阅读位置持久化

---

## 🔵 第三阶段：智能标注 + PDF 支持（3–4 周）

### 功能：

- **PDF 阅读器**：基于 pdf.js
- **智能单词标注**：根据词库自动高亮已学习/待学习单词
- **批量查词**：传入文本 + 词库 → 返回标注结果
- **标注系统**：高亮 + 句子标注
- 图片搜索 + 插入

### 技术重点：

- 文本分词 + 词频统计
- 常用词表集成（CEFR / 高频词表）
- PDF 文本提取

---

## 🟣 第四阶段：复习 + 导出（3–4 周）

### 功能：

- **单词复习**：基于间隔重复（SM-2 算法）
- **Anki 导出**：生成 CSV/APKG 文件
- **Stripe 支付**：会员订阅
- **插件系统**：扩展词典/导出格式

### 技术重点：

- 间隔重复算法
- AnkiConnect API
- Stripe Checkout + Webhook

---

## 🔴 第五阶段：管理与运营（2–3 周）

### 功能：

- 管理后台（查看用户、数据管理）
- 用户数据分析
- 性能优化
- 隐私合规（数据导出/删除）

---

## 🔴 第五阶段：管理与运营（2–3 周）

### 功能：

- 管理后台（查看用户、数据）
- 数据分析
- 用户支持系统
- 性能优化

---

## ⚠️ 风险与难点

| 模块 | 难点 | 解决方案 |
|------|------|---------|
| 多租户隔离 | PostgreSQL RLS 配置 | 使用 API 层隔离 + 中间件 |
| 支付集成 | Stripe Webhook 处理 | 使用 Stripe Billing |
| 数据迁移 | 用户数据导出/导入 | 提供完整导出功能 |
| 隐私合规 | GDPR 数据删除 | 级联删除 + 备份 |
| 存储成本 | S3 费用控制 | 按需压缩 + 限制文件大小 |
| 词典加载 | 大词典内存占用 | 按需加载 + LRU 缓存 |
| EPUB 解析 | 特殊格式兼容 | 使用成熟库（epub.js / unzipper） |

---

## 📦 词典资源清单

| 词典 | 语言对 | 大小 | 来源 |
|------|--------|------|------|
| ECDICT | 英汉 | ~50MB | [GitHub](https://github.com/skywind3000/ECDICT) |
|朗文当代高级英语辞典|英英|~100MB|需购买或寻找免费版|
| JLPT 词典 | 日汉 | ~30MB | MDict 社区 |

**初期建议**：只集成 ECDICT（免费开源），后续按需扩展

---

## ✅ 最终目标

> 一个类似：

- 阅读器（EPUB/PDF）
- 语言学习工具（查词 + 标注）
- 知识提取工具（导出 Anki）
- **多租户 SaaS 平台**
- **会员制服务**

---

## 📊 预估成本（单用户版）

| 服务 | 方案 | 月费用 |
|------|------|--------|
| PostgreSQL | Supabase Pro | $25/月 |
| 后端 | Railway Hobby | $5/月 |
| 前端 | Vercel Free | $0 |
| 存储 | S3 100GB | ~$2/月 |
| 域名 + SSL | - | $10/年 |
| **总计** | | **~$32/月** |

### 盈利模型

- Free 用户：成本分摊
- 10 个 Pro 用户：覆盖成本
- 50 个 Pro 用户：盈利

---

---

## ✅ 确认待办

### 需要确认的问题

- [ ] **目标语言**：主要是英语，还是多语言（日语、法语等）？
- [ ] **AI 辅助**：是否需要 AI 自动生成例句、解释？
- [ ] **离线需求**：用户需要离线使用吗？（影响架构设计）
- [ ] **会员定价**：Free/Pro/Team 的具体功能和定价？

### 下一步行动

如果确认以上功能列表，可以开始：

1. 👉 生成 **完整 Prisma Schema**（数据库结构）
2. 👉 创建 **项目目录结构**
3. 👉 写 **服务端词典加载代码**
4. 👉 写 **EPUB 解析服务**
5. 👉 设计 **前端阅读器组件**

---

## 📝 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-04-13 | 架构转型：从自托管改为多租户 SaaS |
| 2026-04-13 | 新增用户流程、词典服务、智能标注系统 |
| 2026-04-13 | 更新技术栈为 PostgreSQL + 服务端词典 |
