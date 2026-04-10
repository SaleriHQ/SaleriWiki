# YouTube Video to Article

将 YouTube 视频转换为结构化文章。完整流水线：下载音频 → Whisper 转录 → Claude 生成文章 → 保存到 Obsidian。

## 工作流程

```
YouTube URL
    ↓
[yt-dlp 下载音频]
    ↓
[Whisper 转录]
    ↓
transcript_*.txt
    ↓
[Claude API 生成文章]
    ↓
article.md
    ↓
Obsidian Vault
```

## 环境要求

```bash
# 1. 安装依赖
pip install yt-dlp openai-whisper anthropic

# 2. 安装 ffmpeg (已安装: E:\App\ffmpeg-master-latest-win64-gpl-shared)
#    确保 ffmpeg.exe 在 PATH 中，或配置到系统环境变量

# 3. 设置 Claude API Key
set ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## ⚠️ 重要：YouTube Cookies 配置

**由于网络环境限制，YouTube 需要登录认证才能下载。**

### 方法一：从浏览器导出 Cookies（推荐）

1. 安装浏览器插件：**Get cookies.txt LOCALLY**（Chrome/Edge/Firefox）
2. 登录 YouTube (https://youtube.com)
3. 访问任意 YouTube 页面，点击插件图标，导出 cookies 为 `.txt` 文件
4. 保存到安全位置（如 `E:\workSpace\SaleriWiki\.claude\cookies\youtube.txt`）

### 方法二：使用环境变量

```bash
# 设置 cookies 文件路径（永久生效）
set YTDLP_COOKIES=E:\workSpace\SaleriWiki\.claude\cookies\youtube.txt
```

### 方法三：命令行参数

```bash
python generate_article.py "VIDEO_URL" --cookies "E:\path\to\cookies.txt"
```

> **安全提示**: Cookies 文件包含登录凭证，请勿提交到 Git。将 cookies 目录加入 `.gitignore`。

## 使用方法

### 基本用法

```
/youtube-article VIDEO_URL
```

### 示例

```
/youtube-article https://www.youtube.com/watch?v=UE6XQTAxwE0
/youtube-article https://youtu.be/VIDEO_ID
/youtube-article VIDEO_ID
```

### 参数选项

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--output-dir` | 输出目录 | `Clippings/` |
| `--whisper-model` | Whisper 模型 | `base` |
| `--article-lang` | 文章语言 | `zh` |
| `--model` | Claude 模型 | `claude-sonnet-4-20250514` |
| `--transcript-only` | 仅转录，不生成文章 | `false` |

### Whisper 模型选择

| 模型 | 内存需求 | 速度 | 精度 |
|------|---------|------|------|
| `tiny` | ~1GB | 最快 | 较低 |
| `base` | ~1GB | 快 | 良好 |
| `small` | ~2GB | 中等 | 良好 |
| `medium` | ~5GB | 较慢 | 较好 |
| `large` | ~10GB | 最慢 | 最好 |

> **注意**: 模型文件会在首次使用时自动下载。

### 输出文件

运行后会生成两个文件：

1. **字幕文件** (`transcript_VIDEO_ID_TITLE.txt`)
   - Whisper 原始转录文本
   - 包含元数据（标题、视频ID、转录时间）

2. **文章文件** (`YYYY-MM-DD TITLE.md`)
   - Claude 生成的格式化文章
   - 包含 frontmatter 元数据
   - 可直接导入 Obsidian

## 本地 LLM 支持

如果想使用本地 Ollama 进行文章生成：

```bash
# 设置 Ollama host
set OLLAMA_HOST=http://localhost:11434

# 修改脚本中的 generate_article 函数使用 Ollama API
# 或在调用时传入 --api-key 和自定义 API 地址
```

## 故障排除

### yt-dlp 下载失败
```bash
# 更新 yt-dlp
pip install -U yt-dlp

# 检查视频是否可用
yt-dlp --list-formats "VIDEO_URL"
```

### Whisper 转录失败
```bash
# 确保 ffmpeg 可用
ffmpeg -version

# 指定音频格式
python generate_article.py "URL" --whisper-model tiny
```

### Claude API 错误
- 检查 API Key 是否正确
- 确认账户余额充足
- 查看 API 速率限制

## 性能提示

1. **首次运行**: Whisper 模型需要下载（1-10GB），请耐心等待
2. **长视频**: 10分钟以上视频可能需要更长时间转录
3. **批量处理**: 可修改脚本支持批量 URL
4. **硬件加速**: Whisper 支持 CUDA 加速（如有 NVIDIA 显卡）
