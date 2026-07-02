# Task Format — Quy tắc viết task BA

> Rule này định nghĩa format chuẩn cho mọi task document trong `docs/tasks/`.

## Nguyên tắc cốt lõi

**Mỗi task chỉ giải quyết đúng 1 vấn đề duy nhất.** KHÔNG gộp nhiều vấn đề vào 1 task.

- 1 bug = 1 task
- 1 cải tiến = 1 task
- 1 tính năng mới = 1 task

## Prefix bắt buộc

Title của mỗi task **PHẢI** bắt đầu bằng 1 trong 5 prefix sau:

| Prefix | Khi nào dùng | Ví dụ |
|---|---|---|
| `[Bug]` | Lỗi cần sửa — hệ thống hoạt động sai so với mong đợi | `[Bug] H3 mục lục không scroll tới nội dung` |
| `[Enhance]` | Nâng cấp/cải tiến tính năng đã có | `[Enhance] Tối ưu crawl heading đối thủ` |
| `[Feature]` | Tính năng mới hoàn toàn chưa có | `[Feature] Tích hợp Auto-save editor` |
| `[Hotfix]` | Lỗi nghiêm trọng cần sửa gấp, ảnh hưởng production | `[Hotfix] Mất ảnh đại diện khi import WordPress` |
| `[Refactor]` | Tái cấu trúc code, không thay đổi hành vi | `[Refactor] Tách logic parse Gutenberg block` |

**Cách phân biệt:**
- **Bug vs Hotfix**: Hotfix = bug nghiêm trọng ảnh hưởng trực tiếp đến user trên production, cần fix ngay. Bug = lỗi bình thường, có thể lên lịch fix.
- **Enhance vs Feature**: Enhance = tính năng đã có nhưng cần cải thiện. Feature = tính năng hoàn toàn mới, chưa tồn tại.
- **Refactor**: Không thay đổi hành vi bên ngoài, chỉ cải thiện code bên trong.

## Tên file

`docs/tasks/<prefix>-<slug>.md`

- **prefix**: loại task viết thường, không dấu ngoặc (`bug`, `enhance`, `feature`, `hotfix`, `refactor`).
- **slug**: viết thường, dùng dấu `-`, không dấu tiếng Việt.
- VD: `bug-loi-format-in-dam.md`

## Frontmatter (bắt buộc)

```yaml
---
task_id: TASK-<số thứ tự>
title: "[Prefix] <Mô tả ngắn 3-8 từ>"
type: <Bug | Enhance | Feature | Hotfix | Refactor>
priority: <🔴 Rất cao | 🟠 Cao | 🟡 Trung bình>
module: <Tên module chính > Sub-module>
created_at: YYYY-MM-DD
source: <Nguồn feedback — tên tài liệu/kênh, ngày feedback>
feedback_by: <Tên người đã report vấn đề này>
related_tasks: [] # Optional — danh sách task_id liên quan
---
```

**Giải thích các trường:**
- `title`: BẮT BUỘC có prefix. Ngắn gọn 3-8 từ, mô tả đúng 1 vấn đề.
- `type`: Khớp với prefix trong title (`[Bug]` → `Bug`, `[Enhance]` → `Enhance`, v.v.).
- `source`: nguồn gốc feedback (VD: "Feedback SEO Content (Google Docs) — Ngày 3/6/2026").
- `feedback_by`: ai đã report vấn đề này (VD: "Chị Liên", "Bạn Ngân"). Vì mỗi task là 1 vấn đề, thường chỉ có 1 người report.
- `related_tasks`: optional, liên kết các task cùng nhóm feedback hoặc cùng module.

## Cấu trúc nội dung

```markdown
# [Prefix] <Mô tả ngắn — giống title trong frontmatter>

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | DD.MM.YYYY |

2. **User Story**

Là một **<role>**, Tôi muốn **<action>**, Để **<benefit>**.

3. **Mô tả vấn đề**

<Mô tả bối cảnh và vấn đề cụ thể trong 2-4 câu. Ghi rõ: hiện tại hệ thống làm gì sai / thiếu gì, ảnh hưởng ra sao đến người dùng.>

4. **Yêu cầu giải pháp**

<Mô tả giải pháp kỹ thuật hoặc nghiệp vụ cần thực hiện trong 2-4 câu. Cụ thể, actionable.>

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | <Kết quả testable>   |
| AC-02     | <Kết quả testable>   |
```

## Nguyên tắc bắt buộc

### Atomic task
- **1 task = 1 vấn đề**. KHÔNG gộp nhiều vấn đề bằng "và" hay "&".
- **Title ngắn gọn** (3-8 từ) + prefix bắt buộc.
- **Section 3 (Mô tả vấn đề)** và **Section 4 (Yêu cầu giải pháp)**: viết đoạn văn ngắn 2-4 câu, KHÔNG dùng bảng (vì chỉ có 1 vấn đề).
- **Tối đa 1-3 AC** — vì chỉ giải quyết 1 vấn đề, không cần nhiều AC.
- Dùng `related_tasks` để liên kết các task cùng nhóm.

### Format
- **Sections dùng numbered list** (`1.`, `2.`, `3.`...) — KHÔNG dùng `## 1.`, `## 2.`.
- **Sub-sections dùng bold** (`**6.1. Tên mục**`) — KHÔNG dùng `### 4.1.`.
- **Chỉ dùng H1 cho title** — toàn bộ structure nằm trong numbered list.

### Nội dung
- Tiếng Việt, technical terms giữ tiếng Anh.
- Văn phong BA/PO chuyên nghiệp, ngắn gọn.
- Không để trống section — thiếu info ghi `[Cần bổ sung]`.
- Mỗi AC phải testable (có thể verify được).

### Nguồn feedback
- `source` và `feedback_by` KHÔNG được để trống.
- Nếu user không cung cấp tên người feedback → hỏi lại trước khi tạo task.
