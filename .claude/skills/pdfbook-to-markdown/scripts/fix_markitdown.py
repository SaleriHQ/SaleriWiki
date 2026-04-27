#!/usr/bin/env python3
"""
Fix fragmented markdown output from markitdown[pdf].

Optimized for math textbooks (like LADR):
- No callouts, use **bold** instead
- Proper inline ($...$) and block ($$...$$) math formatting
- Fix heading levels for chapter/section/subsection
- Handle proofs with **证明** and $\blacksquare$
- Remove page markers
"""

import re
import sys
from pathlib import Path


# Unicode math symbols → LaTeX (order matters!)
UNICODE_MATH_MAP = [
    # Compound patterns first (most specific)
    ('ℝ', r'\mathbb{R}'), ('ℂ', r'\mathbb{C}'), ('ℕ', r'\mathbb{N}'),
    ('ℤ', r'\mathbb{Z}'), ('ℚ', r'\mathbb{Q}'), ('𝔽', r'\mathbb{F}'),
    # Bold compound (𝐑𝐧 → \mathbb{R}^n)
    ('𝐑𝐧', r'\mathbb{R}^n'), ('𝐂𝐧', r'\mathbb{C}^n'),
    ('𝐑𝐦', r'\mathbb{R}^m'), ('𝐂𝐦', r'\mathbb{C}^m'),
    # Bold capitals
    ('𝐀', r'\mathbf{A}'), ('𝐁', r'\mathbf{B}'), ('𝐂', r'\mathbf{C}'), ('𝐃', r'\mathbf{D}'),
    ('𝐄', r'\mathbf{E}'), ('𝐅', r'\mathbf{F}'), ('𝐆', r'\mathbf{G}'), ('𝐇', r'\mathbf{H}'),
    ('𝐈', r'\mathbf{I}'), ('𝐉', r'\mathbf{J}'), ('𝐊', r'\mathbf{K}'), ('𝐋', r'\mathbf{L}'),
    ('𝐌', r'\mathbf{M}'), ('𝐍', r'\mathbf{N}'), ('𝐎', r'\mathbf{O}'), ('𝐏', r'\mathbf{P}'),
    ('𝐐', r'\mathbf{Q}'), ('𝐑', r'\mathbf{R}'), ('𝐒', r'\mathbf{S}'), ('𝐓', r'\mathbf{T}'),
    ('𝐔', r'\mathbf{U}'), ('𝐕', r'\mathbf{V}'), ('𝐖', r'\mathbf{W}'), ('𝐗', r'\mathbf{X}'),
    ('𝐘', r'\mathbf{Y}'), ('𝐙', r'\mathbf{Z}'),
    # Bold lowercase
    ('𝐚', r'\mathbf{a}'), ('𝐛', r'\mathbf{b}'), ('𝐜', r'\mathbf{c}'), ('𝐝', r'\mathbf{d}'),
    ('𝐞', r'\mathbf{e}'), ('𝐟', r'\mathbf{f}'), ('𝐠', r'\mathbf{g}'), ('𝐡', r'\mathbf{h}'),
    ('𝐢', r'\mathbf{i}'), ('𝐣', r'\mathbf{j}'), ('𝐤', r'\mathbf{k}'), ('𝐥', r'\mathbf{l}'),
    ('𝐦', r'\mathbf{m}'), ('𝐧', r'\mathbf{n}'), ('𝐨', r'\mathbf{o}'), ('𝐩', r'\mathbf{p}'),
    ('𝐪', r'\mathbf{q}'), ('𝐫', r'\mathbf{r}'), ('𝐬', r'\mathbf{s}'), ('𝐭', r'\mathbf{t}'),
    ('𝐮', r'\mathbf{u}'), ('𝐯', r'\mathbf{v}'), ('𝐰', r'\mathbf{w}'), ('𝐱', r'\mathbf{x}'),
    ('𝐲', r'\mathbf{y}'), ('𝐳', r'\mathbf{z}'),
    # Script
    ('𝐴', r'\mathcal{A}'), ('𝐵', r'\mathcal{B}'), ('𝐶', r'\mathcal{C}'), ('𝐷', r'\mathcal{D}'),
    ('𝐸', r'\mathcal{E}'), ('𝐹', r'\mathcal{F}'), ('𝐺', r'\mathcal{G}'), ('𝐻', r'\mathcal{H}'),
    ('𝐼', r'\mathcal{I}'), ('𝐽', r'\mathcal{J}'), ('𝐾', r'\mathcal{K}'), ('𝐿', r'\mathcal{L}'),
    ('𝑀', r'\mathcal{M}'), ('𝑁', r'\mathcal{N}'), ('𝑂', r'\mathcal{O}'), ('𝑃', r'\mathcal{P}'),
    ('𝑄', r'\mathcal{Q}'), ('𝑅', r'\mathcal{R}'), ('𝑆', r'\mathcal{S}'), ('𝑇', r'\mathcal{T}'),
    ('𝑈', r'\mathcal{U}'), ('𝑉', r'\mathcal{V}'), ('𝑊', r'\mathcal{W}'), ('𝑋', r'\mathcal{X}'),
    ('𝑌', r'\mathcal{Y}'), ('𝑍', r'\mathcal{Z}'),
    # Greek lowercase
    ('𝛼', r'\alpha'), ('𝛽', r'\beta'), ('𝛾', r'\gamma'), ('𝛿', r'\delta'),
    ('𝜖', r'\epsilon'), ('𝜁', r'\zeta'), ('𝜂', r'\eta'), ('𝜃', r'\theta'),
    ('𝜄', r'\iota'), ('𝜅', r'\kappa'), ('𝜆', r'\lambda'), ('𝜇', r'\mu'),
    ('𝜈', r'\nu'), ('𝜉', r'\xi'), ('𝜋', r'\pi'), ('𝜌', r'\rho'),
    ('𝜎', r'\sigma'), ('𝜏', r'\tau'), ('𝜐', r'\upsilon'), ('𝜑', r'\phi'),
    ('𝜒', r'\chi'), ('𝜓', r'\psi'), ('𝜔', r'\omega'),
    # Greek uppercase
    ('𝛢', r'\Alpha'), ('𝛣', r'\Beta'), ('𝛤', r'\Gamma'), ('𝛥', r'\Delta'),
    ('𝛦', r'\Epsilon'), ('𝛧', r'\Zeta'), ('𝛨', r'\Eta'), ('𝛩', r'\Theta'),
    ('𝛪', r'\Iota'), ('𝛫', r'\Kappa'), ('𝛬', r'\Lambda'), ('𝛭', r'\Mu'),
    ('𝛮', r'\Nu'), ('𝛯', r'\Xi'), ('𝛰', r'\Omicron'), ('𝛱', r'\Pi'),
    ('𝛲', r'\Rho'), ('𝛳', r'\Sigma'), ('𝛴', r'\Tau'), ('𝛵', r'\Upsilon'),
    ('𝛶', r'\Phi'), ('𝛷', r'\Chi'), ('𝛸', r'\Psi'), ('𝛹', r'\Omega'),
    # Italic
    ('𝑎', r'a'), ('𝑏', r'b'), ('𝑐', r'c'), ('𝑑', r'd'),
    ('𝑒', r'e'), ('𝑓', r'f'), ('𝑔', r'g'), ('ℎ', r'h'),
    ('𝑖', r'i'), ('𝑗', r'j'), ('𝑘', r'k'), ('𝑙', r'l'),
    ('𝑚', r'm'), ('𝑛', r'n'), ('𝑜', r'o'), ('𝑝', r'p'),
    ('𝑞', r'q'), ('𝑟', r'r'), ('𝑠', r's'), ('𝑡', r't'),
    ('𝑢', r'u'), ('𝑣', r'v'), ('𝑤', r'w'), ('𝑥', r'x'),
    ('𝑦', r'y'), ('𝑧', r'z'), ('𝑇', r'^T'),
    # Operators
    ('√', r'\sqrt'), ('∞', r'\infty'), ('∈', r'\in'), ('∉', r'\notin'),
    ('∅', r'\emptyset'), ('⊂', r'\subset'), ('⊃', r'\supset'), ('⊆', r'\subseteq'),
    ('⊇', r'\supseteq'), ('∪', r'\cup'), ('∩', r'\cap'), ('∧', r'\land'),
    ('∨', r'\lor'), ('¬', r'\neg'), ('∀', r'\forall'), ('∃', r'\exists'),
    ('≤', r'\leq'), ('≥', r'\geq'), ('≠', r'\neq'), ('≈', r'\approx'),
    ('≡', r'\equiv'), ('±', r'\pm'), ('∓', r'\mp'), ('×', r'\times'),
    ('÷', r'\div'), ('⋅', r'\cdot'), ('∘', r'\circ'), ('⊕', r'\oplus'),
    ('⊗', r'\otimes'), ('⟨', r'\langle'), ('⟩', r'\rangle'),
    ('→', r'\rightarrow'), ('←', r'\leftarrow'), ('↔', r'\leftrightarrow'),
    ('⇒', r'\Rightarrow'), ('⇐', r'\Leftarrow'), ('⇔', r'\Leftrightarrow'),
    ('∑', r'\sum'), ('∏', r'\prod'), ('∫', r'\int'), ('∂', r'\partial'),
    ('∇', r'\nabla'), ('Δ', r'\Delta'), ('Π', r'\Pi'), ('Σ', r'\Sigma'),
    ('Θ', r'\Theta'), ('Λ', r'\Lambda'), ('Ω', r'\Omega'), ('Φ', r'\Phi'), ('Ψ', r'\Psi'),
    # Dashes
    ('−', '-'), ('—', '—'), ('–', '–'),
    # Superscripts
    ('¹', '^1'), ('²', '^2'), ('³', '^3'), ('⁴', '^4'), ('⁵', '^5'),
    ('⁶', '^6'), ('⁷', '^7'), ('⁸', '^8'), ('⁹', '^9'), ('⁰', '^0'),
    # Subscripts
    ('₀', '_0'), ('₁', '_1'), ('₂', '_2'), ('₃', '_3'), ('₄', '_4'),
    ('₅', '_5'), ('₆', '_6'), ('₇', '_7'), ('₈', '_8'), ('₉', '_9'),
    # Black square
    ('■', r'\blacksquare'), ('□', r'\square'),
]


def unicode_math_to_latex(text: str) -> str:
    """Convert Unicode math symbols to LaTeX."""
    for unicode_char, latex in UNICODE_MATH_MAP:
        text = text.replace(unicode_char, latex)
    return text


def fix_camel_case(text: str) -> str:
    """Fix CamelCase and hyphenation issues."""
    result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    result = re.sub(r'(\w)-\n(\w)', r'\1\2', result)
    result = re.sub(r'(\w)—\n(\w)', r'\1\2', result)
    return result


def remove_page_markers(content: str) -> str:
    """Remove page markers like '### 第1A节 ... 第3页'."""
    pattern = r'^###\s*第[^第]*节[^第]*第\d+页\s*$\n?'
    content = re.sub(pattern, '', content, flags=re.MULTILINE)
    return content


def fix_math_delimiters(content: str) -> str:
    """
    Fix standalone math lines to use $$...$$
    Only wrap lines that are clearly equations (contain significant math symbols).
    """
    lines = content.split('\n')
    result = []

    # Strict math indicators - only these warrant block math
    strict_math_indicators = [
        '∑', '∫', r'\frac', r'\sqrt', r'\lim',
        r'\sin', r'\cos', r'\log', r'\exp', r'\infty',
        '→', '⟨', '⟩', '≤', '≥', '≠', '±',
        r'\mathbb', r'\mathbf', r'\mathcal',
        r'\alpha', r'\beta', r'\gamma', r'\delta',
        r'\lambda', r'\mu', r'\sigma', r'\pi',
        r'\otimes', r'\oplus', r'\circ',
        '...'
    ]

    # Lines that look like equations (don't wrap prose)
    equation_patterns = [
        r'^\s*\d+\s*=',  # starts with number =
        r'^\s*[a-z]\s*=',  # x =
        r'^\s*\(',  # starts with (
        r'^\s*\)',  # starts with )
    ]

    for line in lines:
        stripped = line.strip()

        # Skip if already has delimiters or is special line
        if stripped.startswith('$$') or stripped.startswith('$') or \
           stripped.startswith('#') or stripped.startswith('-') or \
           stripped.startswith('>') or stripped.startswith('```') or \
           stripped.startswith('**'):
            result.append(line)
            continue

        # Check if line is clearly an equation
        is_equation = False

        # Check against equation patterns
        for pattern in equation_patterns:
            if re.match(pattern, stripped):
                is_equation = True
                break

        # Check if line is mostly math (very few words)
        words = re.findall(r'[a-zA-Z]{4,}', stripped)
        math_count = sum(1 for ind in strict_math_indicators if ind in stripped)

        # Wrap if: has math symbols AND few words AND reasonable length
        if math_count >= 2 and len(words) <= 1 and 5 < len(stripped) < 200:
            is_equation = True

        if is_equation and not any(stripped.startswith(p) for p in ['**', '>']):
            result.append(f'$${stripped}$$')
        else:
            result.append(line)

    return '\n'.join(result)


def wrap_definitions_bold(content: str) -> str:
    """Wrap definitions/notation/theorems/examples in **bold**."""
    patterns = [
        # Pattern: number Type: followed by newline or start of list
        (r'(?m)^(\d+\.\d+)\s*[Dd]efinition:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 定义：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Nn]otation:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 记号：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Tt]heorem:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 定理：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Ee]xample:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 例：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Ll]emma:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 引理：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Cc]orollary:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 推论：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Pp]roposition:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 命题：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Rr]emark:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 注：** \2\n'),
        (r'(?m)^(\d+\.\d+)\s*[Cc]laim:?\s*([^\n]*?)\s*(?:\n|$)', r'**\1 主张：** \2\n'),
    ]

    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)

    return content


def handle_proofs(content: str) -> str:
    """Handle proof markers."""
    content = re.sub(r'\*\*Proof\.\*\*', r'**证明。**', content, flags=re.IGNORECASE)
    return content


def fix_exercises_section(content: str) -> str:
    """Fix exercises section heading."""
    content = re.sub(r'(?m)^####\s*[Ee]xercises\s*(\d+[A-Z]?)\s*$',
                     r'#### 练习 \1', content)
    return content


def fix_heading_levels(content: str) -> str:
    """Fix heading levels for math textbook structure."""
    lines = content.split('\n')
    result = []

    for line in lines:
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            result.append(line)
            continue

        # # Chapter 1: Introduction → ## 第1章 简介
        m = re.match(r'^#\s+[Cc]hapter\s+(\d+)[:\s]+(.+)$', stripped)
        if m:
            result.append(f'## 第{m.group(1)}章 {m.group(2).rstrip(":").strip()}')
            continue

        # # Chapter1 (no space) → ## 第1章
        m = re.match(r'^#\s+[Cc]hapter(\d+)\s*(.*)$', stripped)
        if m:
            title = m.group(2).strip()
            result.append(f'## 第{m.group(1)}章 {title}' if title else f'## 第{m.group(1)}章')
            continue

        # # Part X → ## 第X部分
        m = re.match(r'^#\s+[Pp]art\s+(\d+)[:\s]*(.*)$', stripped)
        if m:
            title = m.group(2).strip()
            result.append(f'## 第{m.group(1)}部分 {" " + title if title else ""}')
            continue

        # ## 1A Title / ## 1A. Title → ### 1A Title
        m = re.match(r'^##\s+(\d+[A-Z]?)\.?\s+(.+)$', stripped)
        if m:
            result.append(f'### {m.group(1)} {m.group(2).strip()}')
            continue

        # ## Chapter X → ### Chapter X
        m = re.match(r'^##\s+[Cc]hapter\s+(\d+)[:\s]*(.*)$', stripped)
        if m:
            result.append(f'### 第{m.group(1)}章 {m.group(2).strip()}')
            continue

        # ### X.X.X → #### X.X.X
        m = re.match(r'^###\s+(\d+\.\d+(?:\.\d+)?)\s+(.+)$', stripped)
        if m:
            result.append(f'#### {m.group(1)} {m.group(2)}')
            continue

        # Detect section headings WITHOUT # (like "1A 𝐑𝐧 and 𝐂𝐧" or "Complex Numbers")
        # Pattern: starts with number+letter or just capitalized words at start of content block
        m = re.match(r'^(\d+[A-Z])\s+(.+)$', stripped)
        if m and not stripped.startswith('$$') and not stripped.startswith('**'):
            # Check if next significant line looks like content (not another heading)
            result.append(f'### {m.group(1)} {m.group(2)}')
            continue

        result.append(line)

    return '\n'.join(result)


def is_garbage_line(line: str) -> bool:
    """Check if line is garbage that should be removed."""
    stripped = line.strip()

    # Skip header artifacts
    if re.match(r'^Linear\s*Algebra\s*Done\s*Right', stripped, re.I):
        return True
    if re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+$', stripped):
        return True
    if re.match(r'^[A-Z][a-z]+,fourthedition', stripped, re.I):
        return True
    if re.match(r'^[A-Z][a-z]+[A-Z][a-z]+$', stripped):
        return True
    if re.match(r'^\d+$', stripped):
        return True  # Standalone page numbers
    return False


def process(content: str) -> str:
    """Main processing pipeline."""
    # 1. Remove page markers
    content = remove_page_markers(content)

    # 2. Process line by line for cleanup
    lines = content.split('\n')
    cleaned_lines = []
    skip_mode = False
    consecutive_table_rows = 0

    for line in lines:
        stripped = line.strip()

        # Skip garbage lines
        if is_garbage_line(stripped):
            continue

        # Detect garbage tables (TOC-like)
        if stripped.startswith('|') and stripped.endswith('|'):
            cells = [c.strip() for c in stripped.split('|') if c.strip()]
            is_garbage = False

            if cells and len(cells) <= 3:
                if any(re.match(r'^(Chapter|Section|Appendix|Part|Preface|Acknowledgments|Contents)', c, re.I) for c in cells):
                    is_garbage = True
                elif all(re.match(r'^(第?[一二三四五六七八九十\d]+章?|Page|\d+)$', c) for c in cells):
                    is_garbage = True

            if is_garbage:
                consecutive_table_rows += 1
                if consecutive_table_rows > 3:
                    skip_mode = True
                continue
            else:
                consecutive_table_rows = 0
                if skip_mode:
                    skip_mode = False
        else:
            consecutive_table_rows = 0

        if skip_mode and not stripped.startswith('#'):
            continue

        cleaned_lines.append(line)

    content = '\n'.join(cleaned_lines)

    # 3. Fix heading levels
    content = fix_heading_levels(content)

    # 4. Wrap definitions in bold
    content = wrap_definitions_bold(content)

    # 5. Handle proofs
    content = handle_proofs(content)

    # 6. Fix CamelCase
    content = fix_camel_case(content)

    # 7. Convert Unicode math BEFORE math delimiter fix
    content = unicode_math_to_latex(content)

    # 8. Fix math delimiters (after Unicode conversion)
    content = fix_math_delimiters(content)

    # 9. Fix exercises
    content = fix_exercises_section(content)

    return content


def main():
    if len(sys.argv) < 3:
        print("Usage: fix_markitdown.py <input.md> <output.md>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    content = input_path.read_text(encoding='utf-8')
    content = process(content)
    output_path.write_text(content, encoding='utf-8')
    print(f"Fixed markdown written to: {output_path}")


if __name__ == '__main__':
    main()
