---
task_id: TASK-032
title: "[Bug] Lời kết nhắc dịch vụ sai rule"
type: Bug
priority: 🟡 Trung bình
module: Content > Rule
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn
related_tasks: [TASK-043, TASK-052, TASK-053]
---

# [Bug] Lời kết nhắc dịch vụ sai rule

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **phần lời kết tổng hợp lại bài viết mà không nhắc dịch vụ**, Để **bài viết tuân đúng rule viết content**.

3. **Mô tả vấn đề**

Phần lời kết (Kết luận) của bài viết đang nhắc đến dịch vụ Vietnix, không đúng với rule. Theo rule, lời kết chỉ tổng hợp lại nội dung bài viết, không cần nhắc dịch vụ ở đây. Phần PR dịch vụ nằm ở vị trí riêng trong bài viết.

4. **Yêu cầu giải pháp**

Cập nhật prompt viết lời kết: chỉ tổng hợp lại nội dung chính của bài viết, không nhắc đến dịch vụ Vietnix. Xem lại rule viết content và đảm bảo prompt tuân thủ đúng.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Phần lời kết chỉ tổng hợp nội dung bài viết, không nhắc dịch vụ |
