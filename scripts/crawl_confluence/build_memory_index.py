"""Tạo INDEX.md và SUMMARY.md từ memory files."""
import re
from datetime import date

from .config import MEMORIES_DIR, SPACE

# Giới hạn chars mỗi page trong SUMMARY.md.
# SUMMARY là input chính cho /viet-task → cần đủ context.
_SUMMARY_CHAR_LIMIT = 5000


def build_index(entries: list[dict]):
    """Tạo INDEX.md — bảng danh sách tất cả pages đã crawl.

    Args:
        entries: list of { id, title, file }
    """
    today = date.today().isoformat()
    rows = "\n".join(
        f"| {e['id']} | {e['title']} | {SPACE} | {today} |"
        for e in entries
    )
    content = f"""# Memories Index

Danh sách tài liệu đã crawl từ Confluence.

## Pages đã crawl

| Page ID | Title | Space | Crawled |
| ------- | ----- | ----- | ------- |
{rows}
"""
    (MEMORIES_DIR / "INDEX.md").write_text(content, encoding="utf-8")


def _smart_truncate(body: str, limit: int) -> str:
    """Truncate tại boundary line — tránh cắt giữa bảng hoặc section.

    Cắt tại limit nhưng tìm dòng trống gần nhất để không cắt giữa chừng.
    """
    if len(body) <= limit:
        return body

    cut = body[:limit]

    # Tìm dòng trống gần nhất (boundary giữa sections)
    last_blank = cut.rfind("\n\n")
    if last_blank > limit * 0.7:
        cut = cut[:last_blank]
    else:
        # Fallback: cắt tại newline gần nhất
        last_newline = cut.rfind("\n")
        if last_newline > limit * 0.8:
            cut = cut[:last_newline]

    return cut + "\n\n... [truncated]"


def build_summary() -> int:
    """Gom tất cả memory files → 1 file SUMMARY.md.

    Đọc từng file .md trong docs/memories/ → smart truncate → nối lại.
    Mục đích: agent chỉ cần đọc 1 file thay vì nhiều file.

    Returns:
        Số pages đã gom.
    """
    memory_files = sorted(
        f for f in MEMORIES_DIR.glob("*.md")
        if f.name not in ("INDEX.md", "SUMMARY.md")
    )
    sections = []
    for f in memory_files:
        text = f.read_text(encoding="utf-8")

        # Tách frontmatter → lấy title, page_id
        title_match = re.search(r"title:\s*(.+)", text)
        title = title_match.group(1).strip() if title_match else f.stem
        page_match = re.search(r"page_id:\s*(.+)", text)
        page_id = page_match.group(1).strip() if page_match else ""

        # Lấy body (phần sau ---)
        body_match = re.search(r"^---\n.*?\n---\n(.+)", text, re.DOTALL)
        body = body_match.group(1).strip() if body_match else text

        body = _smart_truncate(body, _SUMMARY_CHAR_LIMIT)

        sections.append(f"## {title} (ID: {page_id})\n\n{body}\n")

    today = date.today().isoformat()
    summary = f"""---
generated_at: {today}
total_pages: {len(sections)}
---

# Memories Summary

Tổng hợp {len(sections)} tài liệu Confluence.

---

{"---\n\n".join(sections)}
"""
    (MEMORIES_DIR / "SUMMARY.md").write_text(summary, encoding="utf-8")
    return len(sections)

