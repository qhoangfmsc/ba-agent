# Hướng dẫn Matt Pocock Agent Skills

> **Source**: [github.com/mattpocock/skills](https://github.com/mattpocock/skills)
> 121k+ ⭐ — "Skills for Real Engineers"

## Tổng quan

Bộ skills từ Matt Pocock giúp AI agent code như engineer thực thụ — không phải "vibe coding". Mỗi skill là một file `SKILL.md` nằm trong `.agent/skills/agent/`, agent sẽ đọc khi cần.

## Danh sách Skills

### 🔧 Engineering Skills

| Skill | Lệnh gọi | Mục đích |
|-------|----------|---------|
| **grill-with-docs** | `/grill-with-docs` | Agent hỏi bạn loạt câu hỏi chi tiết trước khi code, tạo CONTEXT.md & ADR |
| **tdd** | `/tdd` | Red-Green-Refactor workflow — viết test trước, code sau |
| **diagnose** | `/diagnose` | Debug có hệ thống — thu thập evidence trước khi fix |
| **prototype** | `/prototype` | Tạo prototype nhanh để validate ý tưởng |
| **triage** | `/triage` | Phân loại và ưu tiên hóa GitHub issues |
| **to-issues** | `/to-issues` | Chuyển yêu cầu thành GitHub issues có cấu trúc |
| **to-prd** | `/to-prd` | Tạo PRD (Product Requirements Document) từ ý tưởng |
| **improve-codebase-architecture** | `/improve-codebase-architecture` | Phân tích và cải thiện kiến trúc code |
| **zoom-out** | `/zoom-out` | Nhìn tổng quan dự án, không sa vào chi tiết |
| **setup-matt-pocock-skills** | `/setup-matt-pocock-skills` | Bootstrap cấu hình cho tất cả skills |

### 🚀 Productivity Skills

| Skill | Lệnh gọi | Mục đích |
|-------|----------|---------|
| **grill-me** | `/grill-me` | Phiên bản nhẹ của grill-with-docs — hỏi kỹ trước khi làm |
| **caveman** | `/caveman` | Giải thích ngắn gọn, tối giản — không dài dòng |
| **handoff** | `/handoff` | Tóm tắt context session để người/agent khác tiếp tục |
| **write-a-skill** | `/write-a-skill` | Agent giúp bạn viết skill mới |

## Skills hay dùng nhất

### 1. `/grill-me` — Align trước khi code

**Khi nào dùng**: Mỗi khi muốn agent làm gì đó quan trọng.

Agent sẽ:
1. Hỏi bạn 5-10 câu hỏi chi tiết về yêu cầu
2. Xác nhận hiểu đúng
3. Rồi mới bắt đầu code

**Tại sao**: Giảm 90% trường hợp agent code sai hướng vì hiểu nhầm.

### 2. `/grill-with-docs` — Align + tạo docs

Giống `/grill-me` nhưng thêm:
- Tạo `CONTEXT.md` — shared language giữa bạn và agent
- Tạo `ADR` (Architecture Decision Records) — ghi lại lý do quyết định

### 3. `/tdd` — Test-Driven Development

Agent sẽ:
1. 🔴 **Red** — Viết test fail trước
2. 🟢 **Green** — Viết code đủ để pass test
3. 🔵 **Refactor** — Clean up code

### 4. `/diagnose` — Debug có hệ thống

Thay vì đoán mò, agent sẽ:
1. Thu thập evidence (logs, errors, state)
2. Đặt hypotheses
3. Test từng hypothesis
4. Fix root cause, không fix symptoms

### 5. `/handoff` — Chuyển giao context

Khi kết thúc session hoặc muốn người khác tiếp tục, agent tóm tắt:
- Đã làm gì
- Đang ở đâu
- Cần làm gì tiếp

## Cách sử dụng

### Trong Antigravity IDE

Gõ lệnh skill trong chat, ví dụ:
```
/grill-me tôi muốn thêm chức năng export PDF cho báo cáo
```

Agent sẽ đọc `SKILL.md` tương ứng và thực hiện theo quy trình.

### Tùy chỉnh

Mỗi skill nằm trong folder riêng tại `.agent/skills/agent/`. Bạn có thể:
- **Sửa** `SKILL.md` để thay đổi behavior
- **Xóa** folder skill không cần
- **Thêm** skill mới bằng `/write-a-skill`

## File quan trọng

```
.agent/skills/agent/
├── engineering/
│   ├── grill-with-docs/    # Align + tạo docs
│   │   ├── SKILL.md
│   │   ├── ADR-FORMAT.md
│   │   └── CONTEXT-FORMAT.md
│   ├── tdd/                # Test-Driven Development
│   │   ├── SKILL.md
│   │   ├── tests.md
│   │   ├── mocking.md
│   │   └── refactoring.md
│   ├── diagnose/           # Debug có hệ thống
│   ├── prototype/          # Prototype nhanh
│   ├── triage/             # Issue management
│   ├── to-issues/          # Tạo GitHub issues
│   ├── to-prd/             # Tạo PRD
│   └── improve-codebase-architecture/
└── productivity/
    ├── grill-me/           # Hỏi kỹ trước khi làm
    ├── caveman/            # Giải thích tối giản
    ├── handoff/            # Chuyển giao context
    └── write-a-skill/      # Viết skill mới
```

## Tham khảo

- GitHub: https://github.com/mattpocock/skills
- Newsletter: https://www.aihero.dev/s/skills-newsletter
- Skills.sh: https://skills.sh/mattpocock/skills
