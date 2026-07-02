---
task_id: TASK-046
title: "[Bug] Chất lượng hình ảnh AI không đồng nhất"
type: Bug
priority: 🟠 Cao
module: Content > Ảnh AI
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-018, TASK-047]
---

# [Bug] Chất lượng hình ảnh AI không đồng nhất

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **hình ảnh AI tạo ra có chất lượng đồng nhất giữa các bài viết**, Để **bài viết có hình ảnh chuyên nghiệp, nhất quán về style**.

3. **Mô tả vấn đề**

Chất lượng hình ảnh AI không đồng nhất giữa các lần tạo bài viết mới. Ví dụ: phần text khái niệm trên ảnh có lúc in đậm có lúc không, style hình ảnh thay đổi giữa các bài. Cần tham khảo chuẩn hình ảnh như trên vietnix.vn/hosting-la-gi/ để đồng nhất.

4. **Yêu cầu giải pháp**

Chuẩn hóa prompt tạo ảnh AI: định nghĩa style guide cố định (font, màu sắc, layout, text formatting) để đảm bảo chất lượng đồng nhất giữa các bài. Có thể dùng reference image hoặc style preset.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Hình ảnh AI tạo ra có style đồng nhất giữa các bài viết (font, màu, layout) |
| AC-02     | Text trên ảnh luôn đúng format (in đậm, kích thước) theo chuẩn |
