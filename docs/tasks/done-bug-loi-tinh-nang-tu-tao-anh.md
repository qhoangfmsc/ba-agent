---
task_id: TASK-018
title: "[Bug] Lỗi tính năng tự tạo ảnh"
type: Bug
priority: 🟠 Cao
module: Editor > Ảnh AI
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-046, TASK-047]
---

# [Bug] Lỗi tính năng tự tạo ảnh

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **tính năng tự tạo ảnh hoạt động bình thường**, Để **có thể tạo ảnh minh họa cho bài viết nhanh chóng**.

3. **Mô tả vấn đề**

Khi sử dụng tính năng tự tạo ảnh (AI image generation) trong editor, tính năng gặp lỗi và không tạo được ảnh. Chi tiết lỗi cần kiểm tra thêm log hệ thống. Điều này khiến người dùng phải tự tạo ảnh bên ngoài rồi upload thủ công.

4. **Yêu cầu giải pháp**

Kiểm tra lại API tạo ảnh AI, xác định nguyên nhân lỗi (timeout, API key hết quota, prompt không hợp lệ...). Fix lỗi và thêm error handling rõ ràng để thông báo cho người dùng khi gặp sự cố.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Tính năng tự tạo ảnh hoạt động bình thường, tạo được ảnh từ prompt |
| AC-02     | Khi gặp lỗi, hiển thị thông báo rõ ràng cho người dùng (nguyên nhân + cách xử lý) |
