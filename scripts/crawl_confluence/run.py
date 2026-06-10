#!/usr/bin/env python3
"""Entry point: crawl Confluence pages → lưu memories.

Gọi tuần tự: fetch pages → convert HTML → save MD → build index.

Usage:
    cd scripts && ../.venv/bin/python3 crawl_confluence/run.py <PAGE_ID> [--children]
"""
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Khi chạy trực tiếp (python3 scripts/crawl-confluence/run.py),
# cần thêm parent vào path để import relative hoạt động
if __name__ == "__main__":
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent))

from crawl_confluence.config import MEMORIES_DIR
from crawl_confluence.fetch_confluence_pages import fetch_children, fetch_page
from crawl_confluence.save_as_memory import save_as_memory
from crawl_confluence.build_memory_index import build_index, build_summary


def main():
    if len(sys.argv) < 2:
        print("Usage: run.py <PAGE_ID> [--children]")
        sys.exit(1)

    page_id = sys.argv[1]
    crawl_children = "--children" in sys.argv

    MEMORIES_DIR.mkdir(parents=True, exist_ok=True)
    entries = []

    # 1. Fetch + save parent page
    print(f"📄 Crawling parent: {page_id}")
    parent = fetch_page(page_id)
    entry = save_as_memory(parent)
    entries.append(entry)
    print(f"   ✅ {entry['file']}")

    # 2. Fetch + save children (concurrent)
    if crawl_children:
        children = fetch_children(page_id)
        print(f"\n📁 Found {len(children)} children\n")

        def process(child):
            page = fetch_page(child["id"])
            return save_as_memory(page)

        with ThreadPoolExecutor(max_workers=5) as pool:
            futures = {pool.submit(process, c): c for c in children}
            for future in as_completed(futures):
                entry = future.result()
                entries.append(entry)
                print(f"   ✅ {entry['file']}")

    # 3. Build INDEX.md + SUMMARY.md
    build_index(entries)
    summary_count = build_summary()

    # 4. Report
    print(f"\n{'='*50}")
    print(f"✅ Crawl hoàn tất!")
    print(f"   📄 Pages: {len(entries)}")
    print(f"   📁 Output: docs/memories/")
    print(f"   📋 INDEX.md: updated")
    print(f"   📝 SUMMARY.md: {summary_count} pages")
    print(f"{'='*50}")
    print(f"\nDanh sách pages:")
    for i, e in enumerate(entries, 1):
        print(f"   {i}. {e['title']} ({e['id']})")


if __name__ == "__main__":
    main()
