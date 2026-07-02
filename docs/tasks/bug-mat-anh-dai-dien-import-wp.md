---
task_id: TASK-009
title: "[Bug] Mất ảnh đại diện khi import WP"
type: Bug
priority: 🔴 Rất cao
module: Import WP > Ảnh
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-011, TASK-013, TASK-022]
---

# [Bug] Mất ảnh đại diện khi import WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **ảnh đại diện (featured image) được import đúng khi chuyển bài sang WordPress**, Để **bài viết hiển thị đầy đủ trên WordPress**.

3. **Mô tả vấn đề**

Khi import bài viết từ tool sang WordPress (staging), ảnh đại diện (featured image) không được truy xuất, hiển thị trống. Điều này buộc người dùng phải tự tay upload lại ảnh đại diện trên WordPress, tạo thêm thao tác thừa.

4. **Yêu cầu giải pháp**

Kiểm tra lại flow import ảnh đại diện sang WordPress, đảm bảo ảnh được upload vào Media Library và gán đúng vào featured image của post. Cần xử lý cả trường hợp ảnh từ URL bên ngoài và ảnh đã upload trên tool.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Ảnh đại diện được import và hiển thị đúng trên WordPress sau khi import |
| AC-02     | Ảnh được upload vào Media Library của WordPress |
