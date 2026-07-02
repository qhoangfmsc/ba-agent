---
task_id: TASK-057
title: "[Bug] Outline không dựa theo đối thủ thực tế"
type: Bug
priority: 🔴 Rất cao
module: Outline > Crawl
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-003, TASK-026, TASK-027]
---

# [Bug] Outline không dựa theo đối thủ thực tế

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline được tạo dựa trên dữ liệu thực tế từ đối thủ đang rank top**, Để **bài viết có cấu trúc cạnh tranh và nội dung chính xác**.

3. **Mô tả vấn đề**

Tool tạo outline không dựa theo đối thủ thực tế trên SERP. Sau khi người dùng chỉnh lại outline để viết, tool không tổng hợp và viết được thông tin chính xác, nội dung trả về nhiều lỗi. Mặc dù tool đã crawl đúng URL top 1 (ví dụ docs.openclaw.ai/install/uninstall) nhưng thông tin từ URL đó chưa được phản ánh vào heading đầu tiên của bài viết.

4. **Yêu cầu giải pháp**

Cải thiện toàn bộ flow tạo outline: (1) crawl đúng và đầy đủ top 10 đối thủ thực tế, (2) phân tích cấu trúc heading và nội dung từng đối thủ, (3) tổng hợp thành outline dựa trên thực tế đối thủ chứ không chỉ dựa vào AI knowledge. Khi viết bài, nội dung phải phản ánh đúng thông tin từ nguồn đối thủ đã crawl.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Outline phản ánh đúng cấu trúc và nội dung từ đối thủ thực tế top 10 |
| AC-02     | Thông tin từ URL đối thủ đã crawl được sử dụng đúng trong bài viết |
| AC-03     | Nội dung viết từ outline chỉnh sửa không bị lỗi hoặc sai thông tin |
