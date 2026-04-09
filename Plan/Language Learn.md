# 起因

市面上的软件收费不好用 Or 开源的软件不好用，老旧，需要重构，集成性差

# 目标

制作有一个好用的`自托管`的语言学习软件，可以接入本地的词典和线上的词典，拥有方便的形式进行词汇管理和复习，进行Anki导出，.....


# 📐 一、项目架构计划（Architecture Plan）

## 1. 项目定位

> 一个**可自托管的语言学习平台**，支持：

- 📚 PDF / EPUB 阅读
    
- 📖 单词/句子标注
    
- 📘 本地 + 在线词典
    
- 🖼 图片辅助记忆
    
- 🧠 Anki 导出
    
- 🐳 Docker 部署
    

---

## 2. 总体架构

```
客户端（浏览器 / PWA）
 ├── 阅读器（EPUB / PDF）
 ├── 标注系统
 ├── 单词管理
 ├── IndexedDB（本地数据存储）
 │
 └── Nuxt Server（Nitro）
      ├── 词典 API
      ├── 翻译 API
      ├── 图片 API 代理
      ├── Anki 导出 API
      └── 用户数据同步（可选）
```

---

## 3. 技术栈

### 前端

- Nuxt 3（SPA 模式）
- Vue 3 + Composition API
- TailwindCSS（UI）
- Pinia（状态管理
### 阅读引擎

- EPUB：epub.js
- PDF：pdf.js（可选/后期）

### 数据存储

- IndexedDB（主存储）
- SQLite（服务端可选）
    

### 后端（Nuxt Nitro）

- API Routes（server/api）
- Node.js runtime
### 部署

- Docker
- Docker Compose
## 4. 核心模块设计

### 4.1 阅读器模块

#### 功能：

- 加载 EPUB / PDF
    
- 文本选择（word / sentence）
    
- 高亮与标注
    

#### 组件划分：

```
components/
 ├── EpubReader.vue
 ├── PdfViewer.vue
 ├── TextSelectionOverlay.vue
```

---

### 4.2 标注系统（核心）

#### 数据结构：

```ts
Annotation {
  id: string
  type: "word" | "sentence"
  content: string
  context: string
  translation: string
  images: string[]
  source: string
  position: object
  created_at: number
}
```

---

### 4.3 词典系统（插件化）

#### 抽象接口：

```ts
interface DictionaryProvider {
  name: string
  lookup(word: string): Promise<Result>
}
```

#### 支持：

- 在线词典
    
- 本地词典（MDict / Stardict）
    

---

### 4.4 图片系统

#### 功能：

- 单词 → 图片搜索
    
- 图片选择 → 插入卡片
    

#### 数据结构：

```ts
Image {
  url: string
  source: string
}
```

---

### 4.5 单词管理系统

#### 功能：

- 单词本
    
- 标注列表
    
- 复习状态（可扩展）
    

---

### 4.6 Anki 导出模块

#### 支持：

- AnkiConnect（实时）
    
- CSV 导出（备用）
    

#### API：

```
/api/anki/export
/api/anki/add
```

---

### 4.7 本地存储（IndexedDB）

#### 存储内容：

- books
    
- annotations
    
- words
    
- settings
    

---

### 4.8 插件系统

#### 类型：

- 词典插件
    
- 翻译插件
    
- 图片插件
    
- 导出插件
    

#### 位置：

```
/plugins/
```

---

## 5. 路由设计

```
/                首页
/reader/[id]     阅读器
/library         书库
/wordbook        单词本
/settings        设置
```

---

## 6. Docker 架构

```
Docker
 ├── Nuxt App（3000）
 ├── 数据卷（/data）
```

---

## 7. 数据流

```
用户选词
 → 查询词典（API）
 → 显示结果
 → 保存到 IndexedDB
 → 可导出 Anki
```

---

# 🚀 二、开发计划（Development Plan）

---

## 🟢 第一阶段：MVP（2–3 周）

### 🎯 目标：

实现最小可用产品

### 功能：

-  EPUB 阅读器
    
-  文本选择
    
-  在线词典查询
    
-  保存单词（IndexedDB）
    
-  单词列表页面
    
-  CSV 导出
    

### 技术重点：

- epub.js 集成
    
- Pinia 状态管理
    
- IndexedDB 封装
    

---

## 🟡 第二阶段：核心功能完善（2–4 周）

### 功能：

-  PDF 支持（基础）
    
-  标注系统（高亮 + 句子）
    
-  图片搜索 + 插入
    
-  多词典支持
    
-  UI 优化（阅读体验）
    

### 技术重点：

- pdf.js
    
- 标注定位
    
- 图片 API
    

---

## 🔵 第三阶段：高级功能（3–5 周）

### 功能：

-  AnkiConnect 集成
    
-  本地词典（MDict）
    
-  插件系统
    
-  数据导入导出
    
-  阅读进度跟踪
    

### 技术重点：

- 插件架构
    
- 本地词典解析
    
- API 抽象层
    

---

## 🔴 第四阶段：自托管与同步（2–3 周）

### 功能：

-  用户数据同步（可选）
    
-  多设备支持
    
-  Docker 部署优化
    
-  配置管理
    

---

## 🟣 第五阶段：增强功能（可选）

### 功能：

-  AI 翻译 / 解释
    
-  自动生成卡片
    
-  词频统计
    
-  学习计划系统
    

---

## 📅 建议开发顺序

```
1. EPUB阅读器
2. 选词 + 查词
3. 保存单词
4. 单词本
5. 导出功能
6. PDF支持
7. 图片功能
8. 插件系统
```

---

## ⚠️ 风险与难点

|模块|难点|
|---|---|
|PDF|文本选取困难|
|词典|MDX 解析复杂|
|标注|精确定位|
|Anki|格式 & 通信|
|浏览器|文件权限限制|

---

## ✅ 最终目标

> 一个类似：

- 阅读器（EPUB/PDF）
    
- 语言学习工具（查词 + 标注）
    
- 知识提取工具（导出 Anki）
    
- 可自托管系统（Docker）
    

---

如果你下一步想继续推进，我可以帮你👇：

- 👉 生成 **项目目录结构（Nuxt版）**
    
- 👉 写 **第一个 EPUB 阅读器组件**
    
- 👉 做 **选词 → 查词 → 保存 的完整代码流程**
    

直接说你要哪一步 👍