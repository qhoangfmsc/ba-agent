---
task_id: TASK-016
title: "[Enhance] Thêm nút hủy liên kết nhanh"
type: Enhance
priority: 🟡 Trung bình
module: Editor > Link
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-017]
---

# [Enhance] Thêm nút hủy liên kết nhanh

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **có nút hủy liên kết (unlink) nhanh khi chỉnh sửa link**, Để **giảm số thao tác cần thực hiện khi xóa link**.

3. **Mô tả vấn đề**

Hiện tại thao tác xóa link khá cồng kềnh: phải xóa anchor, xóa link, rồi bấm tick xác nhận — tổng cộng nhiều bước. Các editor phổ biến (Google Docs, WordPress) đều có nút "Unlink" / "Hủy liên kết" một chạm để xóa link nhanh.

4. **Yêu cầu giải pháp**

Thêm nút "Hủy liên kết" (Unlink) vào toolbar hoặc popup chỉnh sửa link trong editor. Khi bấm, link bị xóa nhưng text anchor vẫn giữ nguyên. Tham khảo UX của Google Docs hoặc WordPress Gutenberg.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Có nút "Hủy liên kết" hiển thị khi click vào link trong editor |
| AC-02     | Bấm nút thì link bị xóa, text anchor giữ nguyên, chỉ cần 1 click |
