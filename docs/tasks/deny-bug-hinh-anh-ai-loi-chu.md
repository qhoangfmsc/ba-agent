---
task_id: TASK-047
title: "[Bug] Hình ảnh AI bị lỗi chữ"
type: Bug
priority: 🟠 Cao
module: Content > Ảnh AI
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-018, TASK-046]
---

# [Bug] Hình ảnh AI bị lỗi chữ

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **hình ảnh AI tạo ra không bị lỗi chữ**, Để **hình ảnh trong bài viết có chất lượng chuyên nghiệp, đọc được**.

3. **Mô tả vấn đề**

Hình ảnh do AI tạo ra bị lỗi chữ: text bị biến dạng, sai chính tả, hoặc không đọc được. Đây là lỗi phổ biến của AI image generation khi render text trên ảnh, đặc biệt với tiếng Việt có dấu.

4. **Yêu cầu giải pháp**

Cải thiện chất lượng text trên ảnh AI: có thể dùng phương pháp overlay text lên ảnh AI bằng code (thay vì để AI tự render text), hoặc chọn model AI tốt hơn trong việc render text. Đảm bảo text tiếng Việt có dấu hiển thị đúng.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Text trên hình ảnh AI không bị lỗi chữ, đọc được rõ ràng |
| AC-02     | Tiếng Việt có dấu hiển thị đúng trên ảnh |
