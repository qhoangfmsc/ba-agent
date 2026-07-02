#!/usr/bin/env python3
"""Batch tạo task markdown files từ JSON input.

Usage:
    .venv/bin/python3 scripts/create-tasks-batch.py <json-file>
    cat tasks.json | .venv/bin/python3 scripts/create-tasks-batch.py -

JSON input: array of task objects.
Required fields: prefix, slug, title
Optional fields: priority, module, feedback_by, source, role, action,
                 benefit, problem, solution, acs, related_tasks

Ví dụ:
    [
      {
        "prefix": "bug",
        "slug": "format-in-dam-loi",
        "title": "[Bug] Format in đậm lỗi",
        "priority": "🟡 Trung bình",
        "module": "Editor > Format",
        "feedback_by": "Chị Liên",
        "source": "Feedback SEO Content — Ngày 08/06/2026",
        "role": "Content Writer",
        "action": "format in đậm hiển thị đúng",
        "benefit": "bài viết chuyên nghiệp",
        "problem": "Mô tả vấn đề 2-4 câu.",
        "solution": "Yêu cầu giải pháp 2-4 câu.",
        "acs": [["AC-01", "Kết quả testable"]],
        "related_tasks": []
      }
    ]
"""

import json
import sys
from datetime import datetime
from pathlib import Path

TASKS_DIR = Path(__file__).resolve().parent.parent / "docs" / "tasks"

TYPE_MAP = {
    "bug": "Bug",
    "enhance": "Enhance",
    "feature": "Feature",
    "hotfix": "Hotfix",
    "refactor": "Refactor",
}

TEMPLATE = """\
---
task_id: {task_id}
title: "{title}"
type: {type}
priority: {priority}
module: {module}
created_at: {created_at}
source: {source}
feedback_by: {feedback_by}
related_tasks: [{related_tasks}]
---

# {title}

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | {date_dd} |

2. **User Story**

Là một **{role}**, Tôi muốn **{action}**, Để **{benefit}**.

3. **Mô tả vấn đề**

{problem}

4. **Yêu cầu giải pháp**

{solution}

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
{acs_rows}
"""


def build_acs_rows(acs: list) -> str:
    if not acs:
        return "| AC-01     | [Cần bổ sung] |"
    return "\n".join(f"| {ac[0]}     | {ac[1]} |" for ac in acs)


def create_tasks(tasks: list[dict]) -> list[dict]:
    TASKS_DIR.mkdir(parents=True, exist_ok=True)


    created_at = datetime.now().strftime("%Y-%m-%d")
    date_dd = datetime.now().strftime("%d.%m.%Y")

    results = []

    for i, task in enumerate(tasks):
        num = str(i + 1).zfill(2)
        prefix = task["prefix"]
        slug = task["slug"]
        title = task["title"]
        task_id = f"TASK-{num}"
        task_type = TYPE_MAP.get(prefix, prefix.capitalize())

        related = task.get("related_tasks", [])
        related_str = ", ".join(f'"{r}"' for r in related) if related else ""

        content = TEMPLATE.format(
            task_id=task_id,
            title=title,
            type=task_type,
            priority=task.get("priority", "🟡 Trung bình"),
            module=task.get("module", "[Cần bổ sung]"),
            created_at=created_at,
            source=task.get("source", "[Cần bổ sung]"),
            feedback_by=task.get("feedback_by", "[Cần bổ sung]"),
            related_tasks=related_str,
            date_dd=date_dd,
            role=task.get("role", "[Cần bổ sung]"),
            action=task.get("action", "[Cần bổ sung]"),
            benefit=task.get("benefit", "[Cần bổ sung]"),
            problem=task.get("problem", "[Cần bổ sung]"),
            solution=task.get("solution", "[Cần bổ sung]"),
            acs_rows=build_acs_rows(task.get("acs", [])),
        )

        filename = f"{prefix}-{slug}.md"
        filepath = TASKS_DIR / filename
        filepath.write_text(content, encoding="utf-8")

        results.append({
            "num": i + 1,
            "task_id": task_id,
            "type": task_type,
            "title": title,
            "priority": task.get("priority", "🟡 Trung bình"),
            "module": task.get("module", ""),
            "feedback_by": task.get("feedback_by", ""),
            "file": filename,
        })

    return results


def print_report(results: list[dict]):
    print(f"\n✅ Tạo thành công {len(results)} task(s)\n")
    header = "| # | Task ID | Type | Title | Priority | Module | Feedback by | File |"
    sep = "|---|---------|------|-------|----------|--------|-------------|------|"
    print(header)
    print(sep)
    for r in results:
        print(
            f"| {r['num']} | {r['task_id']} | {r['type']} "
            f"| {r['title']} | {r['priority']} | {r['module']} "
            f"| {r['feedback_by']} | {r['file']} |"
        )


def main():
    if len(sys.argv) < 2:
        print("Usage: create-tasks-batch.py <json-file|->")
        sys.exit(1)

    source = sys.argv[1]
    if source == "-":
        data = json.load(sys.stdin)
    else:
        with open(source, encoding="utf-8") as f:
            data = json.load(f)

    if not isinstance(data, list):
        print("❌ JSON input phải là array.")
        sys.exit(1)

    if not data:
        print("❌ Không có task nào.")
        sys.exit(1)

    required = ["prefix", "slug", "title"]
    for i, task in enumerate(data):
        missing = [f for f in required if f not in task]
        if missing:
            print(f"❌ Task #{i + 1} thiếu field: {', '.join(missing)}")
            sys.exit(1)

    results = create_tasks(data)
    print_report(results)


if __name__ == "__main__":
    main()
