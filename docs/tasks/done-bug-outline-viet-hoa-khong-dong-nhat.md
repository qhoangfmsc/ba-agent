---
task_id: TASK-023
title: "[Bug] Outline chưa đồng nhất viết hoa viết thường"
type: Bug
priority: 🟡 Trung bình
module: Outline > Format
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn
related_tasks: [TASK-024]
---

# [Bug] Outline chưa đồng nhất viết hoa viết thường

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline tự động sinh ra có format viết hoa viết thường đồng nhất**, Để **không phải chỉnh sửa lại format heading thủ công**.

3. **Mô tả vấn đề**

Outline được AI tạo ra có heading không đồng nhất về viết hoa viết thường. Có heading viết hoa chữ cái đầu, có heading viết thường toàn bộ, không tuân theo một quy tắc nhất quán. Điều này ảnh hưởng đến tính chuyên nghiệp của outline và bài viết.

4. **Yêu cầu giải pháp**

Thêm bước post-processing sau khi AI tạo outline: chuẩn hóa format viết hoa viết thường cho tất cả heading theo quy tắc thống nhất (ví dụ: viết hoa chữ cái đầu mỗi heading). Có thể thêm vào prompt hoặc xử lý bằng code.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Tất cả heading trong outline có format viết hoa/thường đồng nhất theo quy tắc chuẩn |
