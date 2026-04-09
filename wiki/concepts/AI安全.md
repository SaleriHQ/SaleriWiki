---
title: AI 安全
created: 2026-04-09
updated: 2026-04-09
tags:
  - concept
  - ai
  - security
related:
  - "[[wiki/concepts/零日漏洞]]"
  - "[[wiki/sources/glasswing]]"
---

# AI 安全 (AI Security)

## 定义

AI 安全有两个维度：

1. **AI 系统的安全性**：确保 AI 本身不被攻击、滥用或产生危险输出
2. **以 AI 赋能网络安全**：利用 AI 的强大能力发现和修复漏洞

本页面聚焦于第二个维度——**AI 时代的网络安全**。

## 背景：AI 改变了网络安全格局

传统上，发现和利用软件漏洞需要高度专业化的安全研究人员，数量有限，因此漏洞长期未被发现（如 16 年、27 年未被检测到的漏洞）。

随着 AI 模型编码能力的突破，漏洞发现和利用的门槛大幅降低：

- **发现成本下降**：AI 可以自主扫描代码，自动找到漏洞
- **利用速度提升**：AI 能够自动开发漏洞利用代码
- **专业要求降低**：不再需要顶级安全专家

这意味着**攻击者和防御者的格局被根本性改变**。

## AI 赋能防御

AI 同样可以帮助防御方：

### 漏洞发现

Claude Mythos Preview 在数周内发现了：
- 所有主要操作系统中的数千个高严重性漏洞
- 所有主要 Web 浏览器中的漏洞
- OpenBSD 存在 27 年的漏洞（可远程崩溃任何机器）
- FFmpeg 存在 16 年的漏洞（自动测试工具触发了 500 万次都没发现）
- Linux 内核多个漏洞的链式组合

### 漏洞修复

AI 可以不仅发现漏洞，还能生成修复补丁（如 Google 的 CodeMender、Big Sleep 项目）。

### 安全代码生成

用 AI 编写的新软件比人工编写的安全漏洞更少。

## 关键指标对比

| 指标 | 描述 |
|------|------|
| CyberGym 漏洞重现 | Mythos Preview: 83.1% vs Opus 4.6: 66.6% |
| SWE-bench Verified | Mythos Preview: 93.9% vs Opus 4.6: 80.8% |
| 零日发现速度 | AI 在数周内发现数千个，部分存活数十年 |
| 漏洞窗口 | 从发现到被利用的时间：从数月压缩到数分钟 |

## 行业应对：Project Glasswing

[[wiki/sources/glasswing]] 是 Anthropic 联合 12 家科技巨头发起的 AI 安全计划：

- **使命**：用 AI 为防御方提供持久优势
- **承诺**：$1 亿 API 额度 + $400 万直接捐赠
- **覆盖**：AWS、Anthropic、Apple、Cisco、CrowdStrike、Google、JPMorganChase、Linux 基金会、Microsoft、NVIDIA、Palo Alto Networks

## 核心挑战

| 挑战 | 说明 |
|------|------|
| **Offensive vs Defensive** | AI 的漏洞发现/利用能力对攻击方和防御方同时开放 |
| **开源生态** | 开源软件构成现代系统大部分代码，但维护者缺乏安全资源 |
| **披露机制** | 零日漏洞披露流程需要适应 AI 速度 |
| **监管标准** | 金融等受监管行业需要新的安全标准 |

## 发展趋势

1. **AI 渗透测试普及**：AI 自动执行渗透测试任务
2. **黑盒测试**：无需源码即可测试二进制程序
3. **自动补丁生成**：AI 直接生成并验证修复补丁
4. **安全开发**：AI 辅助的安全开发流程（DevSecOps）

---

## 来源

- [[Clippings/Project Glasswing Securing critical software for the AI era]] - Anthropic 官方报告
- [[wiki/sources/glasswing]] - Glasswing 计划摘要
- [[wiki/concepts/零日漏洞]] - 零日漏洞的概念与发现

## 相关概念

- [[wiki/concepts/零日漏洞]] - AI 发现的未知漏洞类型
- [[wiki/sources/glasswing]] - Project Glasswing 完整摘要
