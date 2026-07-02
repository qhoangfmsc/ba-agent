---
task_id: TASK-003
title: "[Bug] Crawl sai/thiếu heading đối thủ"
type: Bug
priority: 🟠 Cao
module: Outline > Crawl heading
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên, Chị Túc Văn
related_tasks: [TASK-002, TASK-057]
---

# [Bug] Crawl sai/thiếu heading đối thủ

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **tool crawl đầy đủ và chính xác các heading từ bài viết đối thủ**, Để **outline được tạo ra có đầy đủ thông tin tham khảo**.

3. **Mô tả vấn đề**

Tool tham khảo đối thủ crawl sai hoặc thiếu các heading trong bài viết đối thủ. Khi kiểm tra bằng các tool khác (SEOquake) thì vẫn ra đủ heading. Điều này khiến outline bị thiếu nội dung quan trọng mà đối thủ đang có, ảnh hưởng đến chất lượng bài viết.

4. **Yêu cầu giải pháp**

Kiểm tra lại logic crawl heading từ URL đối thủ, đảm bảo parse đúng và đầy đủ tất cả heading (H1-H6) từ HTML của bài viết. Cần xử lý các trường hợp heading được render bằng JavaScript hoặc nằm trong các structure phức tạp. So sánh kết quả crawl với các tool chuẩn (SEOquake) để validate.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Tool crawl đầy đủ các heading (H1-H6) từ bài viết đối thủ, kết quả khớp với các SEO tool khác |
| AC-02     | Không bị mất heading do lỗi parse HTML hoặc JavaScript rendering |
