#!/usr/bin/env python3
"""Fetch Google Docs → export HTML → convert sang Markdown.

Usage:
    .venv/bin/python3 scripts/fetch-gdocs-to-md.py <GOOGLE_DOCS_URL> [OUTPUT_PATH]

Ví dụ:
    .venv/bin/python3 scripts/fetch-gdocs-to-md.py \
        "https://docs.google.com/document/d/1xxx/edit?tab=t.abc123" \
        requirements/feedback-seo.md

Hỗ trợ tab:
    Nếu URL chứa ?tab=t.xxx, script sẽ export NỘI DUNG CỦA TAB ĐÓ.
    Mỗi tab cho ra nội dung khác nhau.
"""
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen

from markitdown import MarkItDown


def extract_doc_id(url: str) -> str:
    """Trích xuất document ID từ Google Docs URL."""
    match = re.search(r'/document/d/([a-zA-Z0-9_-]+)', url)
    if not match:
        raise ValueError(f"Không tìm được document ID từ URL: {url}")
    return match.group(1)


def extract_tab_id(url: str) -> str | None:
    """Trích xuất tab ID từ Google Docs URL nếu có.

    VD: ?tab=t.ot1s3877c62m → "t.ot1s3877c62m"
    """
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    if "tab" in params:
        return params["tab"][0]

    # Cũng check fragment (sau #)
    frag_params = parse_qs(parsed.fragment)
    if "tab" in frag_params:
        return frag_params["tab"][0]

    return None


def fetch_as_html(doc_id: str, tab_id: str | None = None) -> bytes:
    """Download Google Docs dưới dạng HTML.

    Nếu có tab_id, export nội dung của tab đó.
    Không có tab_id → export tab mặc định (tab đầu tiên).
    """
    export_url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
    if tab_id:
        export_url += f"&tab={tab_id}"
    with urlopen(export_url) as resp:
        return resp.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch-gdocs-to-md.py <GOOGLE_DOCS_URL> [OUTPUT_PATH]")
        sys.exit(1)

    url = sys.argv[1]
    doc_id = extract_doc_id(url)
    tab_id = extract_tab_id(url)

    # Default output path
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = Path("requirements") / f"gdocs-{doc_id[:12]}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if tab_id:
        print(f"📑 Export tab: {tab_id}")

    print(f"📥 Fetching Google Docs: {doc_id}...")
    try:
        html_bytes = fetch_as_html(doc_id, tab_id)
    except Exception as e:
        print(f"❌ Lỗi khi fetch Google Docs: {e}")
        sys.exit(1)

    print(f"   Downloaded {len(html_bytes):,} bytes HTML")

    # Ghi HTML ra temp file → markitdown convert
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp:
        tmp.write(html_bytes)
        tmp_path = tmp.name

    print(f"🔄 Converting HTML → Markdown...")
    try:
        md = MarkItDown()
        result = md.convert(tmp_path)
        markdown_text = result.text_content
    except Exception as e:
        Path(tmp_path).unlink(missing_ok=True)
        print(f"❌ Lỗi khi convert HTML → Markdown: {e}")
        sys.exit(1)

    Path(tmp_path).unlink(missing_ok=True)

    output_path.write_text(markdown_text, encoding="utf-8")
    print(f"✅ Saved: {output_path} ({len(markdown_text):,} chars)")


if __name__ == "__main__":
    main()
