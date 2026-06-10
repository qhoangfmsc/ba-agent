---
trigger: always_on
---

# Agent Skills & Workflows Index — Đọc file này TRƯỚC, chỉ mở khi cần

**KHÔNG đọc tất cả cùng lúc**. Xác định tình huống → mở đúng file cần thiết.

## 🔴 BA Workflows (`.agent/workflows/`)

Workflows chính của dự án — dùng khi user yêu cầu làm việc BA.

| Tình huống | Workflow | Path |
|-----------|----------|------|
| Crawl Confluence về memories | **crawl-confluence** | `../../workflows/crawl-confluence.md` |
| Tạo task từ requirements + memories | **viet-task** | `../../workflows/viet-task.md` |

## 🟡 Engineering Skills (`agent/engineering/`)

Dùng khi user yêu cầu liên quan đến coding/engineering.

| Tình huống | Skill | Path |
|-----------|-------|------|
| Task phức tạp, cần hỏi kỹ trước khi làm | **grill-me** | `agent/productivity/grill-me/` |
| Task phức tạp + tạo CONTEXT.md & ADR | **grill-with-docs** | `agent/engineering/grill-with-docs/` |
| Debug có hệ thống, tìm root cause | **diagnose** | `agent/engineering/diagnose/` |
| Viết code theo TDD | **tdd** | `agent/engineering/tdd/` |
| Tạo prototype nhanh | **prototype** | `agent/engineering/prototype/` |
| Phân loại, ưu tiên issues | **triage** | `agent/engineering/triage/` |
| Chuyển yêu cầu thành GitHub issues | **to-issues** | `agent/engineering/to-issues/` |
| Tạo PRD từ ý tưởng | **to-prd** | `agent/engineering/to-prd/` |
| Cải thiện kiến trúc codebase | **improve-codebase-architecture** | `agent/engineering/improve-codebase-architecture/` |
| Nhìn tổng quan dự án | **zoom-out** | `agent/engineering/zoom-out/` |

## 🟢 Productivity Skills (`agent/productivity/`)

| Tình huống | Skill | Path |
|-----------|-------|------|
| Tóm tắt session để chuyển giao | **handoff** | `agent/productivity/handoff/` |
| Giải thích ngắn gọn, tối giản | **caveman** | `agent/productivity/caveman/` |
| Viết skill mới | **write-a-skill** | `agent/productivity/write-a-skill/` |

## Quy tắc

1. **BA workflows là ưu tiên** — nếu user nói về task, crawl, memories → dùng workflow
2. **Chỉ mở 1 file** — đọc file được chọn, không đọc tất cả
3. **User gọi trực tiếp** — `/viet-task`, `/crawl-confluence`, `/grill-me`... → mở thẳng
4. **Confluence = READ-ONLY** — chỉ đọc, không create/edit/delete
5. **Không chắc chắn** → mặc định hỏi user trước

