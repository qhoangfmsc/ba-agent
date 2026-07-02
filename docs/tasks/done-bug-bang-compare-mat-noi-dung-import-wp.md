---
task_id: TASK-010
title: "[Bug] Bảng compare mất nội dung khi import WP"
type: Bug
priority: 🟠 Cao
module: Import WP > Block
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên, Bạn Ngân
related_tasks: [TASK-012, TASK-014, TASK-019, TASK-050]
---

# [Bug] Bảng compare mất nội dung khi import WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **bảng compare ưu nhược điểm hiển thị đầy đủ nội dung sau khi import sang WordPress**, Để **bài viết trên WordPress hoàn chỉnh như trên tool**.

3. **Mô tả vấn đề**

Khi import bài viết sang WordPress, block bảng compare (ưu nhược điểm) chỉ giữ được định dạng (khung bảng) nhưng mất toàn bộ nội dung bên trong. Thử tự chèn tay block ưu-nhược điểm trên WordPress cũng chỉ hiện format chứ không có nội dung. Điều này khiến phần so sánh trong bài viết bị trống hoàn toàn.

4. **Yêu cầu giải pháp**

Kiểm tra lại cách convert block compare từ tool sang Gutenberg block trên WordPress. Đảm bảo nội dung text trong từng ô của bảng compare được map đúng vào các field tương ứng của block WordPress. Cần test cả trường hợp bảng có nhiều dòng và nội dung dài.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Bảng compare hiển thị đầy đủ nội dung (ưu điểm, nhược điểm) sau khi import sang WordPress |
| AC-02     | Format bảng giữ nguyên cấu trúc và style trên WordPress |
