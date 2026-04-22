---
title: AI/LLM 自学路线
created: 2026-04-22
tags:
  - plan
  - learning
  - ai
  - llm
  - self-study
related:
  - "[[Clippings/Computer Science and Engineering]]"
  - "[[Clippings/Mathematics]]"
---

# AI/LLM 自学路线

## 背景

- **身份**：计算机科学大三学生
- **数学基础**：薄弱
- **目标**：自学全流程，从数学到人工智能，尽快过渡到 AI/LLM

## 核心理念

> **先上手，再深入** — 理解概念 > 会推导，缺什么补什么

---

# 一、总体路线图

```
Week 1-4        Week 5-8        Week 9-14       Week 15+
─────────       ─────────       ─────────       ─────────
线性代数  →     概率统计   →     ML 基础     →    深度学习
(只学必要)       (只学必要)       (快速过一遍)      (核心 + 实践)
                                    ↓
                              Week 10+ 可开始
                              简单项目实战
```

---

# 二、Phase 1：线性代数速成（3-4 周）

## 学习目标

能够理解：
- 向量、矩阵运算的意义
- 矩阵乘法在计算什么
- 特征值/特征向量的几何意义
- 在神经网络中的应用

## 必须掌握的概念

| 概念 | 为什么 | 优先级 |
|------|--------|--------|
| 向量、矩阵定义 | 数据表示基础 | ✅ 必须 |
| 矩阵乘法 | 神经网络前向传播 | ✅ 必须 |
| 转置、逆矩阵 | 推导计算 | ⚠️ 了解 |
| 行列式 | 理解变换 | ⚠️ 了解 |
| 特征值/特征向量 | PCA、神经网络收敛性 | ✅ 必须 |
| SVD 奇异值分解 | 推荐系统、嵌入 | ⚠️ 了解 |
| 范数 (L1/L2) | 正则化、损失函数 | ⚠️ 了解 |

## 学习资源

### 视频（优先）

| 资源 | 来源 | 时长 | 说明 |
|------|------|------|------|
| **3Blue1Brown — Essence of Linear Algebra** | B站/YouTube | ~2小时 | ⭐ 直观理解，必看 |

```
B站搜索：3Blue1Brown 线性代数
或直接访问：https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab
```

### 书籍（参考）

| 书籍 | 来源 | 章节 | 用途 |
|------|------|------|------|
| **Linear Algebra Done Right** (Axler) | [[Clippings/Mathematics]] | Finite-Dimensional Vector Spaces | 理论深入 |
| **Shilov** (Dover) | [[Clippings/Mathematics]] | Finite-Dimensional Vector Spaces | 练习题 |
| **Linear Algebra and Its Applications** (Strang) | [[Clippings/Mathematics]] | Applied Linear Algebra | 应用视角 |

### 实践任务

```python
# Week 4 目标：用 NumPy 实现以下
import numpy as np

# 1. 矩阵乘法（手动实现 vs np.dot）
# 2. 求特征值 (np.linalg.eig)
# 3. SVD 分解 (np.linalg.svd)
# 4. 实现一个简单线性回归
```

## 进入下一阶段的条件

- [ ] 能解释矩阵乘法在算什么
- [ ] 能说明特征值在 ML 中的作用
- [ ] 能用 NumPy 做基本矩阵运算

---

# 三、Phase 2：概率统计速成（2-3 周）

## 学习目标

能够理解：
- 什么是概率分布
- 期望值、方差的含义
- 最大似然估计的直观意义
- 交叉熵损失函数

## 必须掌握的概念

| 概念 | 为什么 | 优先级 |
|------|--------|--------|
| 概率基础（条件概率、全概率） | 贝叶斯网络基础 | ✅ 必须 |
| 概率分布（正态/伯努利） | 模型基础 | ✅ 必须 |
| 期望、方差、标准差 | 评估指标 | ✅ 必须 |
| 最大似然估计 | 训练模型的核心 | ⚠️ 重要 |
| 贝叶斯定理 | 朴素贝叶斯、先验知识 | ⚠️ 重要 |
| 信息熵 | 交叉熵损失函数 | ⚠️ 了解 |

## 学习资源

### 视频

| 资源 | 时长 | 说明 |
|------|------|------|
| **3Blue1Brown — Probability** | ~2小时 | 直观理解概率 |

### 书籍

| 书籍 | 来源 | 章节 | 用途 |
|------|------|------|------|
| **All of Statistics** (Wasserman) | [[Clippings/CS&E]] | Mathematics | ⭐ 快速过一遍 |
| **Introduction to Probability** (Bertsekas) | [[Clippings/Mathematics]] | Probability and Randomness | 深入学习 |

### Khan Academy（补充）

```
https://www.khanacademy.org/math/statistics-probability
- 概率基础
- 随机变量
- 推论统计
```

## 实践任务

```python
# Week 6 目标：
import numpy as np
from scipy import stats

# 1. 计算均值、方差
# 2. 生成正态分布样本
# 3. 理解最大似然估计
# 4. 用贝叶斯方法做简单分类
```

## 进入下一阶段的条件

- [ ] 能解释什么是正态分布
- [ ] 能说明最大似然估计在做什么
- [ ] 能区分频率学派和贝叶斯学派

---

# 四、Phase 3：机器学习基础（3-4 周）

## 学习目标

能够：
- 理解监督学习/无监督学习的区别
- 实现线性回归、逻辑回归
- 理解过拟合/欠拟合
- 使用 sklearn 完成简单项目

## 必须掌握的概念

```
监督学习：
├── 线性回归 → 梯度下降
├── 逻辑回归 → 分类问题
├── 决策树 / 随机森林 → 集成方法
├── 支持向量机 → 核方法
└── 过拟合 / 欠拟合 → 泛化能力

无监督学习：
├── K-means → 聚类
└── PCA → 降维

基础概念：
├── 训练 / 验证 / 测试集
├── 交叉验证
└── 偏差-方差权衡
```

## 学习资源

### 视频（优先）

| 资源 | 时长 | 说明 |
|------|------|------|
| **Andrew Ng ML 课程** (Coursera) | ~40小时 | ⭐ 最经典，建议 2x 速播 |

```
Coursera: https://www.coursera.org/learn/machine-learning
B站有中文搬运版
```

### 书籍

| 书籍 | 来源 | 用途 |
|------|------|------|
| **Pattern Recognition and Machine Learning** (Bishop) | [[Clippings/CS&E]] | ⭐ 概率视角，经典 |
| **The Elements of Statistical Learning** (Hastie) | [[Clippings/CS&E]] | ⭐ 理论深度，[免费在线](https://hastie.su.domains/Papers/ESLII.pdf) |
| **Information Theory, Inference & Learning Algorithms** (MacKay) | [[Clippings/CS&E]] | [免费在线](http://www.inference.phy.cam.ac.uk/mackay/itila/) |

### 在线课程补充

| 资源 | 说明 |
|------|------|
| **Fast.ai** | 实践导向，边做边学 |
| **李宏毅机器学习** (B站) | 中文，LLM 部分很全 |

## 实践任务

```python
# Week 10 目标：完成以下项目之一
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression

# 选项 1：Kaggle Titanic 生存预测
# 选项 2：房价预测
# 选项 3：鸢尾花分类
```

## 进入下一阶段的条件

- [ ] 能独立用 sklearn 跑模型
- [ ] 能解释训练集/验证集/测试集的作用
- [ ] 能判断过拟合/欠拟合并调参

---

# 五、Phase 4：深度学习 + LLM（4-6 周）

## 学习目标

能够：
- 理解神经网络的前向传播和反向传播
- 用 PyTorch 实现简单网络
- 理解 Transformer 架构
- 用 Hugging Face 微调模型

## 知识图谱

```
神经网络核心：
├── 感知机 → 全连接层
├── 激活函数 (ReLU/Sigmoid/Softmax)
├── 损失函数 (MSE/Cross-entropy)
├── 反向传播 → 链式法则（概念）
└── 优化器 (SGD/Adam)

卷积神经网络 CNN：
├── 卷积层 → 特征提取
├── 池化层 → 降维
└── 应用：图像分类

循环神经网络 RNN：
├── 序列处理
├── LSTM/GRU
└── 应用：文本生成

Transformer（LLM 核心）：
├── Self-Attention 机制
├── Multi-Head Attention
├── Positional Encoding
├── Encoder / Decoder
└── GPT / BERT / LLaMA 架构
```

## 学习资源

### 视频

| 资源 | 说明 |
|------|------|
| **Fast.ai 深度学习课程** | ⭐ 从实践开始，最快上手 |
| **3Blue1Brown — Neural Networks** | 直观理解反向传播 |
| **李宏毅 — 机器学习/深度学习** | 中文，Transformer 讲得很清楚 |

### 书籍

| 书籍 | 说明 |
|------|------|
| **Deep Learning with Python** (Chollet) | Keras 作者，写得极好 |
| **Dive into Deep Learning** | 中文友好，[免费在线](https://d2l.ai/) |

### 文档

| 资源 | 说明 |
|------|------|
| **PyTorch 官方教程** | https://pytorch.org/tutorials/ |
| **Hugging Face 文档** | https://huggingface.co/docs |

## 实践任务

```python
# Week 12-14 目标：

# 1. 用 PyTorch 实现手写数字识别 (MNIST)
import torch
import torch.nn as nn

# 2. 用 Hugging Face Transformers
from transformers import AutoModel, AutoTokenizer

# 3. 微调一个小模型
# 4. 运行一个 LLM demo (GPT-2 / LLaMA)
```

---

# 六、项目实战（持续）

## 阶段一：巩固练习

| 项目 | 数据集 | 技能 |
|------|--------|------|
| MNIST 手写识别 | 内置 | CNN 基础 |
| IMDB 情感分类 | 内置 | 文本分类 |
| 房价预测 | Kaggle | 回归模型 |

## 阶段二：LLM 专项

| 项目 | 工具 | 说明 |
|------|------|------|
| 文本生成 | GPT-2 | 熟悉生成任务 |
| 问答系统 | BERT | 熟悉微调 |
| 对话机器人 | LLaMA/Alpaca | 综合应用 |

## 阶段三：进阶项目

- RAG 系统构建
- Agent 开发
- 模型部署与优化

---

# 七、书籍来源对照表

## 来源：[[Clippings/Computer Science and Engineering]]

| 书籍 | 章节位置 | 本计划中的用途 |
|------|----------|----------------|
| Pattern Recognition and Machine Learning (Bishop) | AI, Machine Learning | ML 理论 |
| The Elements of Statistical Learning (Hastie) | AI, Machine Learning | ML 理论 |
| Information Theory, Inference & Learning Algorithms (MacKay) | AI, Machine Learning | ML 理论 |
| AI: A Modern Approach (Russell & Norvig) | AI, Machine Learning | AI 基础 |

## 来源：[[Clippings/Mathematics]]

| 书籍 | 章节位置 | 本计划中的用途 |
|------|----------|----------------|
| Linear Algebra Done Right (Axler) | Finite-Dimensional Vector Spaces | 线代理论 |
| Shilov (Dover) | Finite-Dimensional Vector Spaces | 线代练习 |
| Introduction to Probability (Bertsekas) | Probability and Randomness | 概率基础 |

---

# 八、时间汇总

| Phase | 内容 | 周数 | 累计 |
|-------|------|------|------|
| 1 | 线性代数速成 | 3-4 | 3-4 |
| 2 | 概率统计速成 | 2-3 | 5-7 |
| 3 | 机器学习基础 | 3-4 | 8-11 |
| 4 | 深度学习 + LLM | 4-6 | 12-17 |
| + | 项目实战 | 持续 | 18+ |

**预计时间**：3-4 个月完成基础，进入 LLM 实战

---

# 九、判断标准

| 阶段 | 进入下一阶段的条件 |
|------|-------------------|
| 线性代数 | 能说出矩阵乘法在算什么、特征值有什么用 |
| 概率统计 | 能解释什么是正态分布、什么是过拟合 |
| ML 基础 | 能独立跑一个 sklearn 模型、调参 |
| 深度学习 | 能用 PyTorch 写一个简单网络 |

---

# 十、关键原则

1. **不要纠结证明** — 理解概念 > 会推导
2. **不要买太多书** — 一本书 + 视频 + 实践 足够
3. **不要只看不动手** — 每周末必须跑代码
4. **不会的再回头补** — 按需学习，不预先学完

---

## 更新日志

| 日期 | 内容 |
|------|------|
| 2026-04-22 | 初版创建，基于 CS 大三、数学薄弱背景的速成路线 |
