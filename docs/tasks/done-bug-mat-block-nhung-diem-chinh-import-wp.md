---
task_id: TASK-012
title: "[Bug] Mất block Những điểm chính khi import WP"
type: Bug
priority: 🟠 Cao
module: Import WP > Block
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-010, TASK-014, TASK-019]
---

# [Bug] Mất block Những điểm chính khi import WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **block "Những điểm chính" được import đầy đủ sang WordPress**, Để **bài viết trên WordPress có đầy đủ các block quan trọng**.

3. **Mô tả vấn đề**

Khi import bài viết sang WordPress, block "Những điểm chính" (Key Takeaways) bị mất hoàn toàn, không xuất hiện trong Gutenberg editor. Block này chứa thông tin tóm tắt quan trọng của bài viết, việc mất block khiến bài viết thiếu phần tổng quan.

4. **Yêu cầu giải pháp**

Kiểm tra lại logic convert block "Những điểm chính" từ tool sang Gutenberg block. Đảm bảo block được map đúng sang custom block hoặc block HTML tương ứng trên WordPress. Nếu WordPress không có custom block tương ứng, cần convert sang block HTML giữ nguyên nội dung và format.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Block "Những điểm chính" xuất hiện đầy đủ nội dung sau khi import sang WordPress |
| AC-02     | Format và style của block được giữ nguyên trên WordPress |
