---
task_id: TASK-041
title: "[Bug] Tổng hợp thông tin sai nhầm phiên bản với gói"
type: Bug
priority: 🟠 Cao
module: Outline > Content
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-027]
---

# [Bug] Tổng hợp thông tin sai nhầm phiên bản với gói

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **thông tin tổng hợp trong outline chính xác, phân biệt đúng giữa phiên bản và gói dịch vụ**, Để **bài viết cung cấp thông tin đáng tin cậy cho người đọc**.

3. **Mô tả vấn đề**

Tool tổng hợp thông tin không chính xác: nhầm lẫn giữa "các phiên bản" và "các gói dịch vụ" của một sản phẩm. Ví dụ: tổng hợp danh sách phiên bản nhưng thực tế đó là các gói dịch vụ (pricing plans). Có thể tham khảo cách trình bày của đối thủ để tổng hợp đúng.

4. **Yêu cầu giải pháp**

Cải thiện prompt tổng hợp thông tin: phân biệt rõ giữa "phiên bản (version)" và "gói dịch vụ (pricing plan)". Khi crawl thông tin từ đối thủ, cần hiểu ngữ cảnh để phân loại đúng. Nếu không chắc chắn, đánh dấu để người dùng review.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Thông tin tổng hợp phân biệt đúng giữa phiên bản và gói dịch vụ |
| AC-02     | Nội dung tổng hợp chính xác so với nguồn gốc trên website sản phẩm |
