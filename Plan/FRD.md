# 功能需求文档 (FRD)

## 多轮面试管理系统

---

## 1. 功能总览

### 1.1 功能架构

```
多轮面试管理系统
├── 候选人管理模块
│   ├── 候选人创建
│   ├── 候选人查询
│   ├── 候选人详情
│   ├── 候选人编辑
│   ├── 候选人删除
│   └── 面试历史
├── 面试流程管理模块
│   ├── 初试管理（技术基础）
│   ├── 复试管理（技术深度）
│   ├── HR面管理（软技能）
│   └── 终面管理（综合决策）
├── 评价管理模块
│   ├── 初试评价（基础问答）
│   ├── 复试评价（深度问答+编程）
│   ├── HR面评价（软技能评估）
│   └── 终面评价（汇总决策）
├── 用户权限模块
│   ├── 登录登出
│   ├── 角色管理
│   └── 权限配置
└── 数据统计模块
    ├── 漏斗分析
    └── KPI看板
```

### 1.2 模块关联

```
候选人管理 ──▶ 面试流程管理 ──▶ 评价管理
    │                │               │
    │                ▼               │
    │          数据统计 ◀────────────┘
    │
    ▼
用户权限（权限控制整体访问）
```

---

## 2. 候选人管理模块

### 2.1 功能列表

| 功能编号 | 功能名称 | 输入 | 输出 | 业务规则 |
|----------|----------|------|------|----------|
| FR-CAN-001 | 创建候选人 | 姓名、手机、邮箱、职位、简历 | 候选人ID | 手机号唯一 |
| FR-CAN-002 | 查询候选人 | 筛选条件 | 分页列表 | 支持姓名/职位/状态/面试官筛选 |
| FR-CAN-003 | 查看详情 | 候选人ID | 完整信息 | 含面试历史+评价汇总 |
| FR-CAN-004 | 编辑候选人 | 候选人ID+修改内容 | 更新结果 | 录用后不可修改 |
| FR-CAN-005 | 删除候选人 | 候选人ID | 删除结果 | 软删除，保留90天 |
| FR-CAN-006 | 查看面试历史 | 候选人ID | Timeline | 按时间倒序 |

### 2.2 用户故事

#### US-CAN-001: HR创建候选人
1. HR登录系统，点击"添加候选人"
2. 填写姓名、手机、邮箱、应聘职位
3. 上传简历附件（PDF/DOC/DOCX）
4. 点击"保存"
5. 系统生成候选人ID，状态默认为"待面试"

---

## 3. 面试流程管理模块

### 3.1 初试管理

#### 功能列表

| 功能编号 | 功能名称 | 输入 | 输出 |
|----------|----------|------|------|
| FR-INI-001 | 安排初试 | 候选人ID、面试官、时间、地点 | 初试ID |
| FR-INI-002 | 初试签到 | 候选人ID | 签到状态 |
| FR-INI-003 | 初试开始/结束 | 初试ID | 时间记录 |
| FR-INI-004 | 基础问答记录 | 题目、候选人回答、得分 | 问答记录 |
| FR-INI-005 | 初试结果提交 | 通过/淘汰、总评 | 结果确认 |

#### 初试评价模板

| 维度 | 分值 | 题型 |
|------|------|------|
| HTML/CSS | 0-10 | 语义化、布局、盒模型 |
| JavaScript | 0-15 | 原型链、异步、作用域 |
| 框架基础 | 0-10 | Vue/React核心概念 |
| 网络基础 | 0-10 | HTTP、跨域、缓存 |
| 工程化 | 0-5 | Webpack、Git |

#### 基础问答题目类型（系统预置）

```typescript
interface InitialQuestion {
  id: string
  category: 'html' | 'css' | 'javascript' | '框架' | '网络' | '工程化'
  question: string       // 题目
  expectedAnswer: string // 期望答案
}
```

### 3.2 复试管理

#### 功能列表

| 功能编号 | 功能名称 | 输入 | 输出 |
|----------|----------|------|------|
| FR-SEC-001 | 安排复试 | 候选人ID、面试官、时间、地点 | 复试ID |
| FR-SEC-002 | 复试签到 | 候选人ID | 签到状态 |
| FR-SEC-003 | 深度问答记录 | 话题、追问链、回答 | 问答记录 |
| FR-SEC-004 | 编程题评价 | 题目、代码、结果、用时 | 编程题记录 |
| FR-SEC-005 | 能力雷达图 | 五维评分 | 雷达图数据 |
| FR-SEC-006 | 复试结果提交 | 通过/淘汰、总评 | 结果确认 |

#### 复试评价内容

```typescript
interface SecondRoundEvaluation {
  // 技术深度问答
  depthQuestions: {
    topic: '架构设计' | '性能优化' | '原理源码' | '项目经验' | '故障排查'
    question: string
    followUps: string[]      // 追问链
    candidateAnswer: string
    depthScore: 0-5
    clarityScore: 0-5
    logicScore: 0-5
  }[]

  // 编程题
  codingChallenge: {
    title: string
    difficulty: 'easy' | 'medium' | 'hard'
    candidateCode: string
    timeSpent: number        // 分钟
    result: 'AC' | 'WA' | 'TLE' | '未完成'
  }

  // 能力雷达图
  radarScores: {
    前端性能: 0-5
    工程架构: 0-5
    问题排查: 0-5
    代码质量: 0-5
    技术深度: 0-5
  }
}
```

### 3.3 HR面管理

#### 功能列表

| 功能编号 | 功能名称 | 输入 | 输出 |
|----------|----------|------|------|
| FR-HR-001 | 安排HR面 | 候选人ID、HR、时间、地点 | HR面ID |
| FR-HR-002 | HR面签到 | 候选人ID | 签到状态 |
| FR-HR-003 | 薪资记录 | 当前薪资、期望薪资、可协商 | 薪资信息 |
| FR-HR-004 | 稳定性评估 | 在职时长、跳槽次数、离职原因 | 稳定性评分 |
| FR-HR-005 | 软技能评分 | 沟通、协作、价值观 | 评分 |
| FR-HR-006 | 风险标记 | 频繁跳槽/空窗期/薪资超标等 | 风险列表 |
| FR-HR-007 | HR面结果提交 | 通过/淘汰、综合评价 | 结果确认 |

#### HR面评价内容

```typescript
interface HrEvaluation {
  // 薪资
  currentSalary: number
  expectedSalary: number
  salaryNegotiable: boolean

  // 稳定性
  currentCompanyDuration: string
  reasonsForLeaving: string
  stabilityScore: 1-5

  // 软技能
  communicationScore: 1-5
  cultureFitScore: 1-5
  careerGrowth: string

  // 风险标记
  redFlags: ('频繁跳槽' | '空窗期长' | '薪资超标' | '态度消极')[]

  // 结论
  recommendation: 'strong_pass' | 'pass' | 'doubtful' | 'reject'
}
```

### 3.4 终面管理

#### 功能列表

| 功能编号 | 功能名称 | 输入 | 输出 |
|----------|----------|------|------|
| FR-FIN-001 | 安排终面 | 候选人ID、高层、时间、地点 | 终面ID |
| FR-FIN-002 | 终面签到 | 候选人ID | 签到状态 |
| FR-FIN-003 | 前轮汇总查看 | 候选人ID | 初试+复试+HR评价 |
| FR-FIN-004 | 综合评分 | 五维综合评分 | 评分 |
| FR-FIN-005 | 优势/顾虑勾选 | 优势列表、顾虑列表 | 勾选结果 |
| FR-FIN-006 | 终面决策 | 录用/拒绝/待定/薪资谈判 | 决策结果 |
| FR-FIN-007 | Offer信息填写 | 薪资、职级、入职日期 | Offer数据 |

#### 终面评价内容

```typescript
interface FinalEvaluation {
  // 前面轮次汇总
  summary: {
    initialRound: { score: number, conclusion: string, highlights: string[], concerns: string[] }
    secondRound: { score: number, conclusion: string, highlights: string[], concerns: string[] }
    hrRound: { recommendation: string, salaryExpectation: number }
  }

  // 高层决策
  overallScore: 1-5
  strengthPoints: string[]   // 核心优势勾选
  concernPoints: string[]   // 顾虑点勾选

  // 决策
  decision: 'offer' | 'reject' | 'pending' | 'salary_negotiation'

  // Offer
  offerSalary?: number
  offerLevel?: 'P5' | 'P6' | 'P7'
  startDate?: string

  // 批复
  approverComments: string
  approverSignature: string
}
```

---

## 4. 评价管理模块

### 4.1 各轮评价对比

| 维度 | 初试 | 复试 | HR面 | 终面 |
|------|------|------|------|------|
| 评价类型 | 基础问答 | 深度问答+编程 | 软技能+薪资 | 综合汇总 |
| 评分方式 | 逐题打分 | 雷达图 | 多维度评分 | 综合打分 |
| 决策选项 | 通过/淘汰 | 通过/淘汰 | 通过/淘汰 | 录用/拒绝 |
| 核心关注 | 基础知识 | 技术深度 | 软实力 | 综合判断 |

### 4.2 评价汇总展示

```typescript
interface EvaluationSummary {
  candidateId: string
  candidateName: string
  position: string
  currentStatus: string

  rounds: {
    round: 'initial' | 'second' | 'hr' | 'final'
    status: 'pending' | 'completed'
    interviewer: string
    completedAt: string
    score: number
    conclusion: string
  }[]

  timeline: {
    event: string
    time: string
    actor: string
    detail: string
  }[]

  finalDecision: string
}
```

---

## 5. 用户权限模块

### 5.1 角色定义

| 角色 | 权限描述 | 可访问菜单 |
|------|----------|------------|
| Admin | 全部权限 | 全部 |
| 面试官 | 技术面试 | 我的面试、评价填写 |
| HR | 招聘协调 | 候选人管理、面试安排、HR面 |
| 高层 | 最终决策 | 候选人查看、终面、数据统计 |

### 5.2 权限矩阵

| 权限项 | Admin | 面试官 | HR | 高层 |
|--------|-------|--------|-----|------|
| 候选人CRUD | ✓ | - | ✓ | 读 |
| 初试安排 | ✓ | - | ✓ | - |
| 初试评价 | ✓ | ✓ | - | - |
| 复试安排 | ✓ | - | ✓ | - |
| 复试评价 | ✓ | ✓ | - | - |
| HR面安排 | ✓ | - | ✓ | - |
| HR面评价 | ✓ | - | ✓ | - |
| 终面安排 | ✓ | - | - | ✓ |
| 终面决策 | ✓ | - | - | ✓ |
| 数据统计 | ✓ | - | ✓ | ✓ |
| 用户管理 | ✓ | - | - | - |

---

## 6. 数据统计模块

### 6.1 漏斗分析

| 阶段 | 指标 | 计算 |
|------|------|------|
| 候选人总量 | 进入初试人数 | COUNT(初试安排) |
| 初试通过 | 通过人数 | 初试结果=通过 |
| 复试通过 | 通过人数 | 复试结果=通过 |
| HR面通过 | 通过人数 | HR面结果=通过 |
| 终面通过 | 录用人数 | 终面结果=录用 |

### 6.2 KPI看板

| 指标 | 目标 |
|------|------|
| 平均面试周期 | ≤14天 |
| 到面率 | ≥90% |
| 初试通过率 | 40-60% |
| 终面通过率 | 80-95% |

---

## 7. 接口需求

### 7.1 候选人接口

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /candidates | 创建候选人 |
| GET | /candidates | 查询列表 |
| GET | /candidates/:id | 详情 |
| PUT | /candidates/:id | 更新 |
| DELETE | /candidates/:id | 删除 |
| GET | /candidates/:id/interviews | 面试历史 |
| GET | /candidates/:id/evaluations | 评价汇总 |

### 7.2 面试接口

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /interviews | 安排面试 |
| GET | /interviews/:id | 面试详情 |
| PUT | /interviews/:id | 更新 |
| POST | /interviews/:id/result | 提交结果 |

### 7.3 评价接口

| 方法 | 路径 | 描述 |
|------|------|------|
| POST | /evaluations | 提交评价 |
| GET | /evaluations/:id | 评价详情 |
| PUT | /evaluations/:id | 修改评价 |
| GET | /evaluations/templates | 评价模板 |

---

## 8. 数据模型

### 8.1 核心实体

```typescript
// 候选人
interface Candidate {
  id: string
  name: string
  phone: string
  email: string
  position: string
  status: 'pending' | 'interviewing' | 'passed' | 'rejected' | 'hired'
  currentRound: 'initial' | 'second' | 'hr' | 'final' | null
  createdAt: string
}

// 面试记录
interface Interview {
  id: string
  candidateId: string
  round: 'initial' | 'second' | 'hr' | 'final'
  interviewerId: string
  status: 'pending' | 'completed' | 'skipped'
  scheduledAt: string
  completedAt?: string
}

// 评价
interface Evaluation {
  id: string
  interviewId: string
  round: 'initial' | 'second' | 'hr' | 'final'
  scores: object        // 各轮不同
  comment: string
  conclusion: 'pass' | 'reject'
  createdAt: string
}

// 用户
interface User {
  id: string
  username: string
  name: string
  role: 'admin' | 'interviewer' | 'hr' | 'manager'
}
```

### 8.2 实体关系

```
User 1 ──N Interview (面试官)
Candidate 1 ──N Interview
Interview 1 ──1 Evaluation
```

---

## 9. 交叉需求

### 9.1 候选人状态流转

```
pending → interviewing → passed → hired
              ↓
           rejected
```

### 9.2 面试轮次流转

```
初试通过 → 复试通过 → HR面通过 → 终面通过 → 录用
    ↓           ↓          ↓          ↓
  淘汰       淘汰       淘汰       拒绝
```

---

**文档版本**：v1.0
**创建日期**：2024-03-24
