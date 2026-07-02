---
task_id: TASK-022
title: "[Bug] Ảnh không đồng bộ vào thư viện WP và bị đổi tên"
type: Bug
priority: 🟠 Cao
module: Import WP > Ảnh
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-009, TASK-013]
---

# [Bug] Ảnh không đồng bộ vào thư viện WP và bị đổi tên

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **ảnh trong bài viết được đồng bộ vào thư viện WordPress với tên gốc**, Để **quản lý ảnh dễ dàng và không ảnh hưởng đến SEO ảnh**.

3. **Mô tả vấn đề**

Khi import bài viết sang WordPress, ảnh do người dùng tự tạo và tải vào bài không được đồng bộ vào Media Library của WordPress. Ngoài ra, tên ảnh cũng bị thay đổi so với tên gốc. Điều này ảnh hưởng đến quản lý media và SEO ảnh (tên file ảnh là yếu tố ranking).

4. **Yêu cầu giải pháp**

Cải thiện flow import ảnh: upload tất cả ảnh trong bài viết vào WordPress Media Library, giữ nguyên tên file gốc (hoặc tên đã được SEO trên tool). Cập nhật URL ảnh trong nội dung bài viết trỏ về ảnh đã upload trên WordPress.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Tất cả ảnh trong bài viết được upload vào WordPress Media Library |
| AC-02     | Tên file ảnh giữ nguyên tên gốc trên tool, không bị đổi tên |
| AC-03     | URL ảnh trong bài viết trỏ về ảnh đã upload trên WordPress |
