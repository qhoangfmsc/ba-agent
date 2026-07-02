---
task_id: TASK-007
title: "[Bug] Mục lục không cập nhật khi sửa H2"
type: Bug
priority: 🟠 Cao
module: Editor > Mục lục
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-005]
---

# [Bug] Mục lục không cập nhật khi sửa H2

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **mục lục tự động cập nhật khi tôi sửa heading trong bài viết**, Để **mục lục luôn phản ánh đúng nội dung hiện tại**.

3. **Mô tả vấn đề**

Khi sửa nội dung H2 trong bài viết đã lưu, sau khi reload lại trang, phần mục lục vẫn hiển thị H2 cũ, không cập nhật theo heading mới. Điều này gây nhầm lẫn vì mục lục không phản ánh đúng nội dung thực tế của bài viết.

4. **Yêu cầu giải pháp**

Đảm bảo mục lục được re-generate hoặc sync lại mỗi khi heading trong bài viết thay đổi. Khi lưu bài viết, mục lục phải được cập nhật theo heading mới trước khi lưu vào database.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Sau khi sửa H2 và lưu bài, reload trang thì mục lục hiển thị đúng H2 mới |
| AC-02     | Mục lục sync realtime khi người dùng chỉnh sửa heading trong editor |
