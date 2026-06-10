"""Convert Confluence HTML → Markdown dùng markitdown."""
import tempfile
from pathlib import Path

from markitdown import MarkItDown

_converter = MarkItDown()


def html_to_markdown(html: str) -> str:
    """Convert HTML string → clean Markdown.

    markitdown nhận file path, nên ghi ra temp file trước.
    """
    with tempfile.NamedTemporaryFile(
        suffix=".html", delete=False, mode="w", encoding="utf-8"
    ) as f:
        f.write(f"<html><body>{html}</body></html>")
        tmp_path = f.name
    try:
        result = _converter.convert(tmp_path)
        return result.text_content.strip()
    finally:
        Path(tmp_path).unlink(missing_ok=True)
