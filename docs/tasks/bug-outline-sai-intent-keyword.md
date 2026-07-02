---
task_id: TASK-026
title: "[Bug] Outline sai intent search keyword"
type: Bug
priority: 🔴 Rất cao
module: Outline > Intent
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn, Bạn Ngân
related_tasks: [TASK-029, TASK-057]
---

# [Bug] Outline sai intent search keyword

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline được tạo ra đúng intent search của keyword**, Để **bài viết đáp ứng đúng nhu cầu tìm kiếm của người dùng và có cơ hội rank cao**.

3. **Mô tả vấn đề**

Góc tiếp cận keyword trong outline bị sai intent. Ví dụ keyword về định nghĩa ("X là gì") cần bắt đầu bằng heading định nghĩa, nhưng outline lại tiếp cận theo hướng khác. Outline cũng chưa lồng các intent phụ vào nội dung heading, dẫn đến bài viết không cover hết search intent và thiếu nội dung so với đối thủ top đầu.

4. **Yêu cầu giải pháp**

Cải thiện logic phân tích keyword intent trước khi tạo outline. Cần xác định đúng intent chính (informational, navigational, transactional, commercial) và các intent phụ, sau đó map chúng vào cấu trúc heading. Đối chiếu outline với bài viết top 10 đối thủ để đảm bảo cover đủ nội dung.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Outline tiếp cận đúng intent chính của keyword (ví dụ: keyword "là gì" → heading đầu là định nghĩa) |
| AC-02     | Các intent phụ được lồng vào nội dung heading phù hợp |
| AC-03     | Outline cover đủ nội dung so với đối thủ top 10 |
