---
task_id: TASK-020
title: "[Bug] Tiêu đề bị dính chữ khi gõ tiếng Việt"
type: Bug
priority: 🟠 Cao
module: Editor > Input
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: []
---

# [Bug] Tiêu đề bị dính chữ khi gõ tiếng Việt

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **gõ tiếng Việt ở phần tiêu đề mà không bị dính chữ**, Để **trải nghiệm nhập liệu mượt mà như các editor khác**.

3. **Mô tả vấn đề**

Khi chỉnh sửa tiêu đề bài viết, gõ tiếng Việt bị dính chữ (các ký tự bị nối liền nhau). Vẫn gõ được tiếng Việt nhưng phải dùng dấu cách để tách ra sau mỗi từ, rất bất tiện. Lỗi này chỉ xảy ra ở trường tiêu đề, có thể do IME composition event không được xử lý đúng.

4. **Yêu cầu giải pháp**

Kiểm tra lại cách xử lý IME composition event (compositionstart, compositionupdate, compositionend) trong trường tiêu đề. Đảm bảo input handler không can thiệp vào quá trình gõ tiếng Việt bằng bộ gõ (Telex, VNI). Tham khảo cách xử lý IME của các editor như ProseMirror, Slate.js.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Gõ tiếng Việt ở tiêu đề không bị dính chữ, hiển thị đúng từng từ |
| AC-02     | Hoạt động bình thường với cả bộ gõ Telex và VNI |
