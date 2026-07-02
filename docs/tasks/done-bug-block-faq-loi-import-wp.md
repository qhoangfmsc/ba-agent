---
task_id: TASK-014
title: "[Bug] Block FAQ lỗi khi import WP"
type: Bug
priority: 🟠 Cao
module: Import WP > Block
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-008, TASK-010, TASK-012, TASK-019]
---

# [Bug] Block FAQ lỗi khi import WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **block FAQ hiển thị đúng và hoạt động bình thường trên WordPress sau khi import**, Để **không phải sửa lại FAQ thủ công**.

3. **Mô tả vấn đề**

Khi import bài viết sang WordPress, block FAQ bị lỗi hiển thị. WordPress báo block không hợp lệ và đề xuất "Thử khôi phục". Khi bấm "Thử khôi phục" thì toàn bộ nội dung FAQ bị mất. Lỗi này khiến người dùng phải nhập lại toàn bộ FAQ thủ công trên WordPress.

4. **Yêu cầu giải pháp**

Kiểm tra lại cấu trúc Gutenberg block FAQ được sinh ra khi import. Đảm bảo block markup tuân đúng schema của plugin FAQ đang sử dụng trên WordPress (RankMath FAQ, Yoast FAQ, hoặc custom). Test kỹ với các trường hợp FAQ có nhiều câu hỏi, câu trả lời dài, và chứa HTML formatting.

5. **Acceptance Criteria**

|           |                                                                     |
| --------- | ------------------------------------------------------------------- |
| **AC ID** | **Kết quả mong đợi**                                                |
| AC-01     | Block FAQ hiển thị đúng trên WordPress, không báo lỗi invalid block |
| AC-02     | Nội dung FAQ (question + answer) đầy đủ và đúng format              |
