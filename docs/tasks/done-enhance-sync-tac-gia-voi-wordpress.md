---
task_id: TASK-021
title: "[Enhance] Sync tác giả giữa tool và WordPress"
type: Enhance
priority: 🟠 Cao
module: Import WP > Meta
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-011]
---

# [Enhance] Sync tác giả giữa tool và WordPress

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |
| v1.1        | BA Agent       | Chuyển từ Bug sang Enhance — sync tác giả | 26.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **danh sách tác giả trên tool được đồng bộ tự động với danh sách user trên WordPress**, Để **khi import bài viết, tác giả luôn được gán chính xác mà không cần kiểm tra hay sửa thủ công**.

3. **Mô tả vấn đề**

Hiện tại việc mapping tác giả giữa tool và WordPress đang thực hiện thủ công hoặc dựa trên logic mapping tĩnh, dẫn đến tình trạng tác giả trên WordPress không khớp với tác giả đã chọn trên tool. Khi có tác giả mới được thêm trên WordPress hoặc trên tool, hệ thống không tự cập nhật, buộc Content Writer phải sửa lại tác giả thủ công sau mỗi lần import.

4. **Yêu cầu giải pháp**

Xây dựng cơ chế sync danh sách tác giả giữa tool và WordPress: pull danh sách WordPress users có quyền author/editor về tool, tự động mapping theo email hoặc username, và cập nhật khi có thay đổi (thêm/xóa/đổi tên tác giả). Khi import bài viết, hệ thống sử dụng mapping đã sync để gán đúng tác giả WordPress tương ứng.

5. **Acceptance Criteria**

|           |                                                                                          |
| --------- | ---------------------------------------------------------------------------------------- |
| **AC ID** | **Kết quả mong đợi**                                                                     |
| AC-01     | Danh sách tác giả trên tool phản ánh đúng danh sách user (author/editor) trên WordPress  |
| AC-02     | Khi import bài viết, tác giả trên WordPress khớp với tác giả đã chọn trên tool           |
| AC-03     | Khi thêm/xóa user trên WordPress, danh sách tác giả trên tool được cập nhật tương ứng   |
