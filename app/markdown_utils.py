# -*- coding: utf-8 -*-
"""
Markdown detection and standardization utilities.

When the real Thần Nông AI (or any upstream LLM) returns content,
newlines may arrive as literal '\\n' strings instead of real newlines,
which breaks Markdown rendering on the client.

This module:
1. Detects whether a string is plain text or Markdown.
2. If Markdown, normalises it so the client always receives
   well-formed Markdown with real newline characters.
"""

import re

# ── Markdown detection ────────────────────────────────────────────────────────

# Patterns that strongly indicate Markdown content
_MD_PATTERNS: list[re.Pattern] = [
    re.compile(r'^#{1,6}\s', re.MULTILINE),          # headings
    re.compile(r'\*\*[^*]+\*\*'),                      # bold
    re.compile(r'\|.*\|.*\|', re.MULTILINE),           # table rows
    re.compile(r'^>\s', re.MULTILINE),                 # blockquote
    re.compile(r'^[-*+]\s', re.MULTILINE),             # unordered list
    re.compile(r'^\d+\.\s', re.MULTILINE),             # ordered list
    re.compile(r'`[^`]+`'),                            # inline code
    re.compile(r'^```', re.MULTILINE),                 # code fence
    re.compile(r'\[.+\]\(.+\)'),                       # link
    re.compile(r'^---$', re.MULTILINE),                # horizontal rule
    re.compile(r'- \[ \]|- \[x\]', re.MULTILINE),     # task list
]

# Minimum number of distinct pattern matches to classify as Markdown
_MD_THRESHOLD = 2


def is_markdown(text: str) -> bool:
    """Return True if *text* looks like Markdown rather than plain text."""
    if not text:
        return False
    hits = sum(1 for p in _MD_PATTERNS if p.search(text))
    return hits >= _MD_THRESHOLD


# ── Markdown standardisation ─────────────────────────────────────────────────

def standardize_markdown(text: str) -> str:
    """
    Normalise a Markdown string so that it renders correctly on the client.

    Handles the common issues produced by LLM responses:
    • Literal '\\n' sequences  → real newlines
    • Literal '\\t' sequences  → real tabs
    • Mixed CRLF / CR          → LF
    • Excess blank lines (> 2) → collapsed to 2
    • Missing blank line before headings / tables / blockquotes
    • Trailing whitespace per line (preserved only for MD line-break "  \\n")
    """

    # 1) Convert literal escape sequences to real characters.
    #    The LLM often returns "Hello\\nWorld" as a JSON string value,
    #    which after JSON decoding becomes the Python str "Hello\nWorld" —
    #    but sometimes the escaping is doubled, leaving a literal backslash-n.
    text = text.replace('\\n', '\n')
    text = text.replace('\\t', '\t')

    # 2) Normalise line endings to LF
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # 3) Collapse runs of 3+ blank lines to exactly 2 (one visual blank line)
    text = re.sub(r'\n{3,}', '\n\n', text)

    # 4) Ensure a blank line BEFORE block-level elements so they render properly.
    #    (heading, table separator, blockquote, horizontal rule, list item start)
    def _ensure_blank_before(pattern: str, text: str) -> str:
        """Insert a blank line before *pattern* if the preceding line is not blank."""
        return re.sub(
            r'([^\n])\n((?:' + pattern + r'))',
            r'\1\n\n\2',
            text,
        )

    text = _ensure_blank_before(r'#{1,6}\s', text)          # headings
    text = _ensure_blank_before(r'>\s', text)                # blockquotes
    text = _ensure_blank_before(r'---', text)                # horizontal rules

    # 5) Strip trailing whitespace on each line (except the intentional
    #    two-space line break which Markdown uses).
    lines = text.split('\n')
    cleaned: list[str] = []
    for line in lines:
        stripped = line.rstrip()
        # Keep trailing double-space (MD soft line break)
        if line.endswith('  \n') or line.endswith('  '):
            cleaned.append(line.rstrip('\n'))
        else:
            cleaned.append(stripped)
    text = '\n'.join(cleaned)

    # 6) Trim leading / trailing whitespace of the whole block
    text = text.strip()

    return text


# ── Public helper ─────────────────────────────────────────────────────────────

def normalize_reply(text: str) -> str:
    """
    Smart normaliser for bot replies.

    • Plain text → returned as-is (no changes).
    • Markdown   → passed through ``standardize_markdown`` to fix
      escaped newlines, spacing, etc.
    """
    if not text:
        return text

    # Quick pre-check: if the raw text contains literal '\\n' we
    # need to unescape first before we can reliably detect markdown.
    preview = text.replace('\\n', '\n').replace('\\t', '\t')

    if is_markdown(preview):
        return standardize_markdown(text)

    return text

