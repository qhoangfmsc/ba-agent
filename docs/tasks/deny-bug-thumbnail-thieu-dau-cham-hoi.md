---
task_id: TASK-042
title: "[Bug] Thumbnail thiếu dấu chấm hỏi keyword là gì"
type: Bug
priority: 🟡 Trung bình
module: Content > Thumbnail
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: []
---

# [Bug] Thumbnail thiếu dấu chấm hỏi keyword là gì

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **thumbnail tự động có dấu chấm hỏi cho keyword dạng "là gì"**, Để **thumbnail đúng chính tả và chuyên nghiệp**.

3. **Mô tả vấn đề**

Khi tạo thumbnail cho bài viết có keyword dạng "X là gì", text trên thumbnail thiếu dấu chấm hỏi cuối câu. Keyword có "là gì" thì phải có dấu "?" — đây là lỗi chính tả cơ bản trên thumbnail ảnh đại diện.

4. **Yêu cầu giải pháp**

Cập nhật logic tạo thumbnail: khi keyword chứa "là gì", tự động thêm dấu "?" nếu chưa có. Kiểm tra text overlay trước khi render thumbnail.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Thumbnail keyword "là gì" luôn có dấu chấm hỏi "?" |
