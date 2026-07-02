---
task_id: TASK-028
title: "[Bug] Outline lạm dụng cấu trúc H3"
type: Bug
priority: 🟠 Cao
module: Outline > Structure
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn, Bạn Ngân
related_tasks: [TASK-035, TASK-037, TASK-039, TASK-040]
---

# [Bug] Outline lạm dụng cấu trúc H3

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline không lạm dụng cấu trúc H3 dưới mỗi H2**, Để **cấu trúc bài viết phù hợp với cách triển khai thực tế của đối thủ**.

3. **Mô tả vấn đề**

Tool đang có xu hướng tự động tạo nhiều H3 dưới mỗi H2, ngay cả khi heading đó không cần chia nhỏ (ví dụ: heading khái niệm, heading ưu nhược điểm). So với đối thủ thực tế, nhiều H2 chỉ có nội dung text mà không cần H3. Lạm dụng H3 khiến bài viết bị chia quá nhỏ, không tự nhiên.

4. **Yêu cầu giải pháp**

Cải thiện logic sinh outline: tham khảo cách triển khai heading thực tế của đối thủ để quyết định heading nào cần H3, heading nào không. Các heading như "X là gì?", "Ưu nhược điểm" thường không cần H3. Dựa vào đối thủ top đầu để xác định cấu trúc phù hợp.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Outline không tạo H3 cho các heading đơn giản (khái niệm, ưu nhược điểm) khi đối thủ không làm vậy |
| AC-02     | Cấu trúc heading phù hợp với cách triển khai thực tế của đối thủ top 10 |
