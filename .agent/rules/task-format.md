# Task Format — Quy tắc viết task BA

> Rule này định nghĩa format chuẩn cho mọi task document trong `docs/tasks/`.

## Tên file

`docs/tasks/YYYY-MM-DD-<slug>.md` — slug viết thường, dùng dấu `-`, không dấu tiếng Việt.

## Frontmatter (bắt buộc)

```yaml
---
task_id: TASK-YYYY-MMDD-<số>
title: <Tiêu đề ngắn 3-6 từ>
type: <bug-fix | feature>
priority: <🔴 Rất cao | 🟠 Cao | 🟡 Trung bình>
module: <Tên module chính > Sub-module>
created_at: YYYY-MM-DD
source: <Nguồn feedback — tên tài liệu/kênh, ngày feedback>
feedback_by: <Tên người/team đã ghi feedback>
---
```

**Giải thích các trường:**
- `source`: nguồn gốc feedback (VD: "Feedback SEO Content (Google Docs) — Ngày 3/6/2026")
- `feedback_by`: ai đã report/ghi feedback (VD: "Chị Hoa — Team Marketing", "Team SEO Content")

## Cấu trúc nội dung

```markdown
# <Tiêu đề ngắn — giống title trong frontmatter>

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | DD.MM.YYYY |

2. **User Story**

Là một **<role>**, Tôi muốn **<action>**, Để **<benefit>**.

3. **Mô tả vấn đề**

<Mô tả bối cảnh chung 1-2 câu>

|            |            |                     |
| ---------- | ---------- | ------------------- |
| **Vấn đề** | **Mô tả** | **Người feedback**  |
| <Vấn đề 1> | <Chi tiết> | <Tên người — ngày>  |
| <Vấn đề 2> | <Chi tiết> | <Tên người — ngày>  |

4. **Yêu cầu chi tiết**

|             |            |
| ----------- | ---------- |
| **Yêu cầu** | **Mô tả** |
| <Yêu cầu 1> | <Mô tả>   |
| <Yêu cầu 2> | <Mô tả>   |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | <Kết quả testable>   |
| AC-02     | <Kết quả testable>   |
```

## Nguyên tắc bắt buộc

### Format
- **Title ngắn gọn** (3-6 từ). KHÔNG viết câu mô tả dài. KHÔNG gộp task bằng "và" hay "&".
- **Sections dùng numbered list** (`1.`, `2.`, `3.`...) — KHÔNG dùng `## 1.`, `## 2.`.
- **Sub-sections dùng bold** (`**6.1. Tên mục**`) — KHÔNG dùng `### 4.1.`.
- **Chỉ dùng H1 cho title** — toàn bộ structure nằm trong numbered list.
- **Mô tả vấn đề**: dùng bảng `| **Vấn đề** | **Mô tả** |`.
- **Tối đa 1 bảng yêu cầu + 1 bảng AC** — gộp hết, không tách.

### Nội dung
- Tiếng Việt, technical terms giữ tiếng Anh.
- Văn phong BA/PO chuyên nghiệp, ngắn gọn.
- Không để trống section — thiếu info ghi `[Cần bổ sung]`.
- Mỗi AC phải testable (có thể verify được).
- Mỗi task phải độc lập, riêng biệt.

### Nguồn feedback
- `source` và `feedback_by` KHÔNG được để trống.
- Nếu user không cung cấp tên người feedback → hỏi lại trước khi tạo task.
