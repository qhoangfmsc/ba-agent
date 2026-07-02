#!/usr/bin/env python3
"""Tạo file task markdown trong docs/tasks/.

Usage:
    echo "<content>" | .venv/bin/python3 scripts/create-task.py <filename>

Ví dụ:
    echo "---\ntask_id: TASK-01\n---\n# Title" | \
        .venv/bin/python3 scripts/create-task.py bug-fix-loi-format.md

Args:
    filename: Tên file (không cần path đầy đủ, sẽ tự đặt vào docs/tasks/).
              Nếu truyền path đầy đủ, dùng đúng path đó.

Content được đọc từ stdin.
"""
import sys
from pathlib import Path


TASKS_DIR = Path(__file__).resolve().parent.parent / "docs" / "tasks"


def main():
    if len(sys.argv) < 2:
        print("Usage: echo '<content>' | create-task.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    # Đọc content từ stdin
    content = sys.stdin.read()
    if not content.strip():
        print("❌ Content rỗng (stdin trống).")
        sys.exit(1)

    # Xác định output path
    file_path = Path(filename)
    if not file_path.is_absolute():
        file_path = TASKS_DIR / filename

    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Ghi file
    file_path.write_text(content, encoding="utf-8")
    print(f"✅ Created: {file_path}")


if __name__ == "__main__":
    main()
