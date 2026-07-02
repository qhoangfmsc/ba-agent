---
task_id: TASK-011
title: "[Bug] Tác giả không hiển thị khi import WP"
type: Bug
priority: 🔴 Rất cao
module: Import WP > Meta
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-009, TASK-021]
---

# [Bug] Tác giả không hiển thị khi import WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **tác giả đã chọn trên tool được import đúng sang WordPress**, Để **bài viết hiển thị đúng thông tin tác giả mà không cần chỉnh tay**.

3. **Mô tả vấn đề**

Khi import bài viết sang WordPress, phần tác giả bị mất mặc dù đã được chọn ngay từ khi bắt đầu viết bài trên tool. Điều này buộc người dùng phải tự chọn lại tác giả trên WordPress, gây thêm thao tác thừa và rủi ro chọn sai.

4. **Yêu cầu giải pháp**

Kiểm tra lại flow import, đảm bảo trường author trên tool được map đúng sang WordPress author. Cần xử lý cả trường hợp author trên tool không tồn tại trên WordPress (tạo mới hoặc map sang author mặc định).

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Tác giả đã chọn trên tool được hiển thị đúng trên WordPress sau khi import |
| AC-02     | Nếu tác giả không tồn tại trên WordPress, hệ thống thông báo hoặc map sang author phù hợp |
