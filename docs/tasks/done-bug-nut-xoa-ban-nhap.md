---
task_id: TASK-034
title: "[Bug] Nút xóa bản nháp không hoạt động"
type: Bug
priority: 🟠 Cao
module: Editor > Draft
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: []
---

# [Bug] Nút xóa bản nháp không hoạt động

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **bấm nút xóa bản nháp thì bản nháp bị xóa thật và không hiện lại**, Để **quản lý bản nháp sạch sẽ**.

3. **Mô tả vấn đề**

Nút xóa bản nháp bấm được nhưng khi reload lại trang, các bản nháp đã xóa vẫn hiện. Dữ liệu không thực sự bị xóa khỏi database hoặc có lỗi trong logic xóa. Điều này khiến danh sách bản nháp ngày càng dài và không thể dọn dẹp.

4. **Yêu cầu giải pháp**

Kiểm tra lại logic xóa bản nháp: đảm bảo API delete thực sự xóa record khỏi database (hoặc soft delete đúng cách). Sau khi xóa, cập nhật lại danh sách trên frontend mà không cần reload. Kiểm tra cả response từ API để xác nhận xóa thành công.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Bấm xóa bản nháp → bản nháp biến mất khỏi danh sách ngay lập tức |
| AC-02     | Reload trang → bản nháp đã xóa không hiện lại |
