---
task_id: TASK-019
title: "[Enhance] Cải thiện chất lượng block CTA khi import sang WP"
type: Enhance
priority: 🟠 Cao
module: Import WP > Block
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-010, TASK-012, TASK-014, TASK-048]
---

# [Enhance] Cải thiện chất lượng block CTA khi import sang WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |
| v1.1        | BA Agent       | Chuyển từ Bug sang Enhance — cải thiện block CTA | 02.07.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **block CTA (Call-to-Action) được convert chính xác và hiển thị đẹp trên WordPress sau khi import**, Để **bài viết có phần chuyển đổi (conversion) chuyên nghiệp, tăng tỷ lệ click và tương tác của người đọc**.

3. **Mô tả hiện trạng**

Hiện tại quá trình import block CTA từ tool sang WordPress chưa hỗ trợ đầy đủ các dạng CTA (button, banner, inline). Block CTA sau khi chuyển đổi chưa được mapping sang đúng Gutenberg block hoặc shortcode tương ứng trên WordPress, dẫn đến kết quả hiển thị chưa đạt chất lượng mong muốn. Content Writer cần chỉnh sửa thủ công sau mỗi lần import, ảnh hưởng đến năng suất và tính nhất quán của bài viết.

4. **Yêu cầu giải pháp**

Nâng cấp logic convert block CTA từ tool sang WordPress Gutenberg block: hỗ trợ mapping cho tất cả các dạng CTA (button, banner, inline) sang custom block hoặc shortcode CTA tương ứng trên WordPress. Đảm bảo nội dung, link, và style của CTA được giữ nguyên sau khi import. Bổ sung cơ chế validate kết quả convert để phát hiện sớm các trường hợp CTA chưa được hỗ trợ.

5. **Acceptance Criteria**

|           |                                                                                              |
| --------- | -------------------------------------------------------------------------------------------- |
| **AC ID** | **Kết quả mong đợi**                                                                         |
| AC-01     | Tất cả các dạng block CTA (button, banner, inline) được convert sang đúng Gutenberg block/shortcode trên WordPress |
| AC-02     | Nội dung, link và style trong CTA được giữ nguyên sau khi import                             |
| AC-03     | Hệ thống cảnh báo khi phát hiện dạng CTA chưa được hỗ trợ trong quá trình import            |
