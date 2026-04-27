#!/usr/bin/env python3
"""
Split a markdown file into chapters based on heading patterns.

Chapter detection rules (in order of priority):
1. `# 第X章` or `# Chapter X` or `# Part X`
2. `# X. ` (e.g., `# 1. Introduction`)
3. `## X. ` or `## Chapter X`
4. `# X ` (single `#` + number)
"""

import re
import sys
from pathlib import Path
from datetime import date


def normalize_title(title: str) -> str:
    """Normalize chapter title for filename and display."""
    # Remove leading/trailing whitespace
    title = title.strip()

    # Remove leading # and whitespace
    title = re.sub(r'^#+\s*', '', title)

    # Replace multiple spaces with single space
    title = re.sub(r'\s+', ' ', title)

    # Remove special characters that are problematic in filenames
    title = title.replace('/', '-').replace('\\', '-').replace(':', '-')
    title = title.replace('*', '').replace('?', '').replace('"', '')
    title = title.replace('<', '-').replace('>', '-').replace('|', '-')

    return title.strip()


def extract_chapter_number(title: str) -> str:
    """Extract chapter/section number from title."""
    # Try to find patterns like "1.2", "Chapter 1", "第1章", "Part 1", "1. "
    patterns = [
        r'^第(\d+)[章节部]',  # 第1章, 第12节
        r'^[Cc]hapter\s*(\d+)',  # Chapter 1
        r'^[Pp]art\s*(\d+)',  # Part 1
        r'^(\d+)\.\s*',  # 1. Introduction
        r'^(\d+)\s+',  # 1 Introduction (single # heading)
        r'^(\d+):',  # 1: Introduction
    ]

    for pattern in patterns:
        match = re.search(pattern, title, re.IGNORECASE)
        if match:
            return match.group(1).zfill(2)

    return '00'


def title_to_filename(title: str, chapter_num: str) -> str:
    """Convert title to filename with chapter number prefix."""
    normalized = normalize_title(title)

    # Try to get Chinese chapter name if available
    chinese_pattern = r'第[一二三四五六七八九十百千万\d]+[章节部]\s*(.+)'
    match = re.search(chinese_pattern, title)
    if match:
        chapter_name = match.group(1).strip()
    else:
        # Use English name, translated roughly
        chapter_name = normalized

    # Truncate long names
    if len(chapter_name) > 30:
        chapter_name = chapter_name[:30].rsplit(' ', 1)[0]

    # Create filename
    if chapter_name:
        return f"第{chapter_num.zfill(2)}章-{chapter_name}.md"
    else:
        return f"第{chapter_num.zfill(2)}章.md"


def is_chapter_heading(line: str) -> tuple[bool, str, int]:
    """
    Check if a line is a chapter heading.

    Returns:
        (is_chapter, heading_text, heading_level)
    """
    stripped = line.strip()

    # Must start with #
    if not stripped.startswith('#'):
        return False, '', 0

    # Count heading level
    level = len(stripped) - len(stripped.lstrip('#'))
    if level > 3:  # Skip too deep headings
        return False, '', 0

    # Get heading text
    text = stripped.lstrip('#').strip()

    # Chapter patterns (higher priority = checked first)
    chapter_patterns = [
        r'^第[一二三四五六七八九十百千万\d]+[章节部]',  # 第1章
        r'^[Cc]hapter\s*\d+',  # Chapter 1
        r'^[Pp]art\s*\d+',  # Part 1
        r'^\d+\.\s*\D',  # 1. Introduction (number followed by non-digit and space)
        r'^\d+\s+[A-Z]',  # 1 Introduction (single # heading with capital letter)
        r'^\d+:',  # 1: Introduction
    ]

    for pattern in chapter_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True, text, level

    # For # headings (level 1), also check if it starts with a number
    if level == 1:
        if re.match(r'^\d+\s', text):
            return True, text, level

    return False, '', 0


def split_chapters(content: str, source_pdf: str = '') -> dict[str, str]:
    """
    Split markdown content into chapters.

    Returns:
        dict of {filename: content}
    """
    lines = content.split('\n')
    chapters = []
    current_chapter = {'title': '', 'level': 0, 'lines': [], 'number': ''}

    for line in lines:
        is_chap, title, level = is_chapter_heading(line)

        if is_chap:
            # Save previous chapter if exists
            if current_chapter['lines']:
                chapters.append(current_chapter)

            # Start new chapter
            current_chapter = {
                'title': title,
                'level': level,
                'lines': [line],
                'number': extract_chapter_number(title)
            }
        else:
            if current_chapter['lines'] or current_chapter['title']:
                current_chapter['lines'].append(line)

    # Don't forget the last chapter
    if current_chapter['lines']:
        chapters.append(current_chapter)

    # Generate chapter files
    result = {}
    for i, chapter in enumerate(chapters):
        filename = title_to_filename(chapter['title'], chapter['number'])
        if not filename.startswith('第'):
            filename = f"第{str(i+1).zfill(2)}章-{filename}"

        # Build content with frontmatter
        body = '\n'.join(chapter['lines'])
        today = date.today().isoformat()

        frontmatter = f"""---
title: {normalize_title(chapter['title'])}
source: {source_pdf}
created: {today}
type: chapter
tags:
  - book
  - chapter
---

"""

        result[filename] = frontmatter + body

    return result


def main():
    if len(sys.argv) < 3:
        print("Usage: split_chapters.py <input.md> <output_dir> [source_pdf]", file=sys.stderr)
        print("       split_chapters.py <input.md> -          # Output to stdout", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_arg = sys.argv[2]
    source_pdf = sys.argv[3] if len(sys.argv) > 3 else input_path.stem

    content = input_path.read_text(encoding='utf-8')
    chapters = split_chapters(content, source_pdf)

    if output_arg == '-':
        # Output to stdout
        for filename, chapter_content in chapters.items():
            print(f"=== {filename} ===")
            print(chapter_content)
            print()
    else:
        output_dir = Path(output_arg)
        output_dir.mkdir(parents=True, exist_ok=True)

        for filename, chapter_content in chapters.items():
            output_path = output_dir / filename
            output_path.write_text(chapter_content, encoding='utf-8')
            print(f"Created: {output_path}")

    print(f"\nTotal chapters: {len(chapters)}")


if __name__ == '__main__':
    main()
