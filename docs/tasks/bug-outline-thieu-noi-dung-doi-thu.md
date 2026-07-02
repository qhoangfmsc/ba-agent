---
task_id: TASK-027
title: "[Bug] Outline thiếu nội dung so với đối thủ"
type: Bug
priority: 🟠 Cao
module: Outline > Content
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn
related_tasks: [TASK-026, TASK-003]
---

# [Bug] Outline thiếu nội dung so với đối thủ

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline cover đầy đủ nội dung mà đối thủ top đầu đang có**, Để **bài viết không bị thiếu topic quan trọng và có thể cạnh tranh rank**.

3. **Mô tả vấn đề**

Khi đối chiếu outline với các bài viết top đầu của đối thủ, outline đang thiếu khá nhiều nội dung. Các chủ đề mà đối thủ đã viết nhưng outline không có, khiến bài viết bị thiếu depth và khó cạnh tranh trên SERP.

4. **Yêu cầu giải pháp**

Cải thiện bước phân tích đối thủ khi tạo outline: crawl và so sánh heading structure của top 10 đối thủ, xác định các topic/heading mà đa số đối thủ đều có nhưng outline đang thiếu. Bổ sung các heading thiếu vào outline, đặt ở vị trí logic phù hợp.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Outline cover ít nhất 80% các topic chính mà đối thủ top 5 đang có |
| AC-02     | Có hiển thị so sánh outline vs đối thủ để người dùng đánh giá |
