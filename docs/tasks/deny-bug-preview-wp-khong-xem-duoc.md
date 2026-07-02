---
task_id: TASK-015
title: "[Bug] Preview WP không xem được bài viết"
type: Bug
priority: 🟠 Cao
module: Import WP > Preview
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: []
---

# [Bug] Preview WP không xem được bài viết

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **bấm nút Preview WP trên tool và xem được bài viết trên WordPress**, Để **kiểm tra bài viết đã import trước khi publish**.

3. **Mô tả vấn đề**

Khi bấm vào nút "Preview WP" trên tool, trang không xem được bài viết. Link trỏ tới WordPress admin nhưng tài khoản Growth Marketing không có quyền xem post đó, trong khi các post khác xem bình thường. Nguyên nhân có thể do post được tạo bởi user khác hoặc permission không đúng.

4. **Yêu cầu giải pháp**

Kiểm tra lại cách tạo post trên WordPress khi import: đảm bảo post được gán author hoặc permission cho phép các role Growth Marketing xem được. Hoặc sử dụng preview link public thay vì admin edit link.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Bấm "Preview WP" trên tool, có thể xem được bài viết trên WordPress với tài khoản Growth Marketing |
| AC-02     | Link preview hoạt động cho tất cả bài viết đã import |
