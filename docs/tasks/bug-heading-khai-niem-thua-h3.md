---
task_id: TASK-039
title: "[Bug] Heading khái niệm không nên triển khai H3"
type: Bug
priority: 🟡 Trung bình
module: Outline > Structure
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-028, TASK-040]
---

# [Bug] Heading khái niệm không nên triển khai H3

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **heading khái niệm ("X là gì?") chỉ làm 1 H2, không triển khai H3 bên dưới**, Để **cấu trúc bài viết gọn gàng, đúng thực tế**.

3. **Mô tả vấn đề**

Các heading khái niệm (dạng "X là gì?") đang bị triển khai thêm nhiều H3 bên dưới, trong khi thực tế heading này chỉ cần viết 1 đoạn text ngắn giải thích khái niệm là đủ. Việc thêm H3 khiến phần định nghĩa bị kéo dài không cần thiết, không phù hợp với cách triển khai của đối thủ.

4. **Yêu cầu giải pháp**

Thêm rule vào logic tạo outline: các heading khái niệm (chứa keyword "là gì", "khái niệm", "định nghĩa") chỉ làm 1 H2 đơn, không triển khai H3 bên dưới. Tham khảo cách triển khai thực tế của đối thủ.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Heading khái niệm ("X là gì?") chỉ có H2, không có H3 bên dưới |
