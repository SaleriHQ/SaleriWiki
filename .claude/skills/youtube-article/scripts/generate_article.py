#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YouTube Video to Article Pipeline

流程: YouTube URL → yt-dlp 下载音频 → Whisper 转录 → Claude 生成文章 → Obsidian

Usage:
    python generate_article.py "VIDEO_URL" [options]

Requirements:
    pip install yt-dlp openai-whisper anthropic
    ffmpeg in PATH
"""

import sys
import os
import re
import json
import io
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

# Windows console UTF-8 encoding
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except Exception:
        pass


DEFAULT_MODEL = 'claude-sonnet-4-20250514'
DEFAULT_WHISPER_MODEL = 'base'
DEFAULT_ARTICLE_LANG = 'zh'


class YouTubeArticleGenerator:
    """YouTube video to article generator."""

    def __init__(
        self,
        whisper_model: str = DEFAULT_WHISPER_MODEL,
        article_lang: str = DEFAULT_ARTICLE_LANG,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        output_dir: Optional[str] = None,
        cookies: Optional[str] = None,
    ):
        self.whisper_model = whisper_model
        self.article_lang = article_lang
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        self.model = model
        self.output_dir = output_dir
        self.cookies = cookies or os.getenv('YTDLP_COOKIES')
        self.temp_dir = None

    def extract_video_id(self, url: str) -> str:
        """Extract video ID from various YouTube URL formats."""
        patterns = [
            r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]+)',
            r'(?:youtu\.be\/)([a-zA-Z0-9_-]+)',
            r'(?:youtube\.com\/embed\/)([a-zA-Z0-9_-]+)',
            r'(?:youtube\.com\/shorts\/)([a-zA-Z0-9_-]+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        if re.match(r'^[a-zA-Z0-9_-]{11}$', url):
            return url
        raise ValueError(f"无法从 URL 中提取视频 ID: {url}")

    def get_video_title(self, video_id: str) -> str:
        """Get video title using yt-dlp."""
        try:
            result = subprocess.run(
                ['yt-dlp', '--print', 'title', '--no-download', f'https://www.youtube.com/watch?v={video_id}'],
                capture_output=True, text=True, timeout=30, encoding='utf-8', errors='replace'
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip()
        except Exception:
            pass
        return f"YouTube Video {video_id}"

    def download_audio(self, url: str) -> Optional[str]:
        """Download audio from YouTube video using yt-dlp."""
        self.temp_dir = tempfile.mkdtemp(prefix='youtube_article_')
        audio_path = os.path.join(self.temp_dir, 'audio')

        print(f"[*] 下载音频: {url}")

        cmd = [
            'yt-dlp',
            '-f', 'bestaudio/best',
            '--extract-audio',
            '--audio-format', 'mp3',
            '--audio-quality', '5',
            '-o', audio_path + '.%(ext)s',
            '--no-playlist',
        ]

        # Add cookies if available
        if self.cookies:
            cmd.extend(['--cookies', self.cookies])
            print(f"[*] 使用 cookies: {self.cookies}")

        try:
            result = subprocess.run(
                cmd + [url],
                capture_output=True, text=True, timeout=600, encoding='utf-8', errors='replace'
            )

            if result.returncode != 0:
                print(f"[X] 下载失败:")
                print(result.stderr[-1000:] if len(result.stderr) > 1000 else result.stderr)
                return None

            # Find the downloaded file
            for ext in ['mp3', 'm4a', 'wav', 'webm']:
                potential_path = f"{audio_path}.{ext}"
                if os.path.exists(potential_path):
                    return potential_path

            print("[X] 找不到下载的音频文件")
            return None

        except subprocess.TimeoutExpired:
            print("[X] 下载超时")
            return None
        except Exception as e:
            print(f"[X] 下载出错: {e}")
            return None

    def transcribe(self, audio_path: str) -> Optional[str]:
        """Transcribe audio using Whisper."""
        print(f"[*] 使用 Whisper ({self.whisper_model} 模型) 转录中...")

        try:
            import whisper
            model = whisper.load_model(self.whisper_model)
            result = model.transcribe(
                audio_path,
                language=None,  # Auto-detect
                verbose=False,
            )
            return result['text'].strip()

        except ImportError:
            print("[X] openai-whisper 未安装")
            print("    安装: pip install openai-whisper")
            return None
        except Exception as e:
            print(f"[X] 转录出错: {e}")
            return None

    def save_transcript(self, transcript: str, video_id: str, video_title: str) -> str:
        """Save transcript to file."""
        output_path = self.output_dir or os.path.join(os.getcwd(), 'Clippings')
        os.makedirs(output_path, exist_ok=True)

        safe_title = re.sub(r'[<>:"/\\|?*]', '_', video_title)[:50]
        filename = f"transcript_{video_id}_{safe_title}.txt"
        filepath = os.path.join(output_path, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"标题: {video_title}\n")
            f.write(f"视频ID: {video_id}\n")
            f.write(f"转录时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"模型: whisper-{self.whisper_model}\n")
            f.write("=" * 60 + "\n\n")
            f.write(transcript)

        print(f"[*] 字幕已保存: {filepath}")
        return filepath

    def generate_article(self, transcript: str, video_title: str, video_id: str) -> Optional[str]:
        """Generate article using Claude API."""
        if not self.api_key:
            print("[!] 未设置 ANTHROPIC_API_KEY，仅保存字幕文件")
            return None

        print(f"[*] 使用 Claude ({self.model}) 生成文章...")

        prompt = f"""你是一位专业的技术文章作者。请根据以下视频字幕，写一篇结构完整的中文技术文章。

视频标题: {video_title}

字幕内容:
---
{transcript[:8000]}
---

要求:
1. 文章标题使用中文
2. 包含摘要、关键要点、详细内容、总结等章节
3. 技术内容准确，保持专业性
4. 代码片段保留原文
5. 如果有数字、人名、技术术语，保留英文或添加英文原文
6. 文章长度适中（1500-3000字），内容充实
7. 使用 Markdown 格式输出，包含适当的标题层级

直接输出文章内容，不需要其他说明。"""

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=self.api_key)

            response = client.messages.create(
                model=self.model,
                max_tokens=8192,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.content[0].text

        except ImportError:
            print("[!] anthropic 库未安装，无法生成文章")
            print("    安装: pip install anthropic")
            return None
        except Exception as e:
            print(f"[!] Claude API 出错: {e}")
            return None

    def save_article(self, article: str, video_id: str, video_title: str) -> Optional[str]:
        """Save generated article to Obsidian vault."""
        output_path = self.output_dir or os.path.join(os.getcwd(), 'Clippings')
        os.makedirs(output_path, exist_ok=True)

        safe_title = re.sub(r'[<>:"/\\|?*]', '_', video_title)[:50]
        date_str = datetime.now().strftime('%Y-%m-%d')
        filename = f"{date_str} {safe_title}.md"
        filepath = os.path.join(output_path, filename)

        # Extract article content (remove thinking blocks if present)
        content = re.sub(r'<thinking>.*?</thinking>\s*', '', article, flags=re.DOTALL)
        content = content.strip()

        frontmatter = f"""---
title: "{video_title}"
source: "https://www.youtube.com/watch?v={video_id}"
created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
tags:
  - youtube-article
video_id: "{video_id}"
transcribed_by: whisper-{self.whisper_model}
---

"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
            f.write(content)

        print(f"[*] 文章已保存: {filepath}")
        return filepath

    def cleanup(self):
        """Clean up temporary files."""
        if self.temp_dir and os.path.exists(self.temp_dir):
            import shutil
            try:
                shutil.rmtree(self.temp_dir)
                print(f"[*] 已清理临时文件")
            except Exception:
                pass

    def run(self, url: str) -> Dict[str, Any]:
        """Run the complete pipeline."""
        print("=" * 60)
        print("YouTube Video to Article Generator")
        print("=" * 60)

        # Step 1: Extract video ID
        try:
            video_id = self.extract_video_id(url)
            print(f"[*] 视频ID: {video_id}")
        except ValueError as e:
            return {'success': False, 'error': str(e)}

        # Step 2: Get video title
        video_title = self.get_video_title(video_id)
        print(f"[*] 视频标题: {video_title}")

        # Step 3: Download audio
        audio_path = self.download_audio(url)
        if not audio_path:
            return {'success': False, 'error': '音频下载失败'}

        # Step 4: Transcribe
        transcript = self.transcribe(audio_path)
        if not transcript:
            self.cleanup()
            return {'success': False, 'error': '转录失败'}

        print(f"[*] 转录完成 ({len(transcript)} 字符)")

        # Step 5: Save transcript
        transcript_path = self.save_transcript(transcript, video_id, video_title)

        # Step 6: Generate article
        article = self.generate_article(transcript, video_title, video_id)

        # Step 7: Save article
        article_path = None
        if article:
            article_path = self.save_article(article, video_id, video_title)

        # Cleanup
        self.cleanup()

        return {
            'success': True,
            'video_id': video_id,
            'video_title': video_title,
            'transcript_path': transcript_path,
            'article_path': article_path,
        }


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='YouTube Video to Article Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python generate_article.py "https://www.youtube.com/watch?v=VIDEO_ID"

    # 指定输出目录
    python generate_article.py "VIDEO_ID" --output-dir "E:\\Vault\\Clippings"

    # 指定 Whisper 模型 (tiny/base/small/medium/large)
    python generate_article.py "VIDEO_ID" --whisper-model medium

    # 使用本地 LLM (设置环境变量 OLLAMA_HOST)
    # 文章生成会使用本地 Ollama API
"""
    )

    parser.add_argument('url', help='YouTube URL 或视频 ID')
    parser.add_argument('--output-dir', help='输出目录 (默认: Clippings)')
    parser.add_argument('--whisper-model', default=DEFAULT_WHISPER_MODEL,
                        choices=['tiny', 'base', 'small', 'medium', 'large'],
                        help=f'Whisper 模型 (默认: {DEFAULT_WHISPER_MODEL})')
    parser.add_argument('--article-lang', default=DEFAULT_ARTICLE_LANG,
                        help=f'文章语言 (默认: {DEFAULT_ARTICLE_LANG})')
    parser.add_argument('--api-key', help='Claude API Key (或设置 ANTHROPIC_API_KEY)')
    parser.add_argument('--model', default=DEFAULT_MODEL, help=f'Claude 模型 (默认: {DEFAULT_MODEL})')
    parser.add_argument('--transcript-only', action='store_true',
                        help='仅转录，不生成文章')
    parser.add_argument('--cookies', help='YouTube cookies 文件路径 (用于绕过地区限制)')

    args = parser.parse_args()

    generator = YouTubeArticleGenerator(
        whisper_model=args.whisper_model,
        article_lang=args.article_lang,
        api_key=args.api_key,
        model=args.model,
        output_dir=args.output_dir,
        cookies=args.cookies,
    )

    result = generator.run(args.url)

    print("\n" + "=" * 60)
    if result['success']:
        print("[✓] 处理完成!")
        print(f"    视频标题: {result['video_title']}")
        print(f"    字幕文件: {result['transcript_path']}")
        if result['article_path']:
            print(f"    文章文件: {result['article_path']}")
        else:
            print("    文章: 未生成 (请设置 ANTHROPIC_API_KEY)")
    else:
        print(f"[X] 处理失败: {result.get('error', '未知错误')}")
        sys.exit(1)


if __name__ == '__main__':
    main()
