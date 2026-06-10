"""Lưu page data thành memory .md file với frontmatter."""
import re
from datetime import date

from .config import BASE_URL, MEMORIES_DIR, SPACE
from .convert_html_to_md import html_to_markdown


def slugify(title: str) -> str:
    """Tạo slug từ title tiếng Việt."""
    slug = title.lower()
    for pattern, repl in {
        r'[àáạảãâầấậẩẫăằắặẳẵ]': 'a', r'[èéẹẻẽêềếệểễ]': 'e',
        r'[ìíịỉĩ]': 'i', r'[òóọỏõôồốộổỗơờớợởỡ]': 'o',
        r'[ùúụủũưừứựửữ]': 'u', r'[ỳýỵỷỹ]': 'y', r'[đ]': 'd',
    }.items():
        slug = re.sub(pattern, repl, slug)
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug).strip('-')
    return slug[:50]


def save_as_memory(page: dict) -> dict:
    """Convert HTML → MD rồi lưu thành memory file.

    Args:
        page: { id, title, space, html }

    Returns:
        { id, title, file } — metadata entry
    """
    page_id = page["id"]
    title = page["title"]
    space = page.get("space", SPACE)
    filename = f"{page_id}-{slugify(title)}.md"
    filepath = MEMORIES_DIR / filename

    markdown = html_to_markdown(page["html"])
    today = date.today().isoformat()

    content = f"""---
source: {BASE_URL}/wiki/spaces/{space}/pages/{page_id}
page_id: {page_id}
title: {title}
space: {space}
crawled_at: {today}
---

# {title}

{markdown}
"""
    filepath.write_text(content, encoding="utf-8")
    return {"id": page_id, "title": title, "file": filename}
