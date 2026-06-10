---
task_id: TASK-2026-0609-4
title: Lỗi UX editor
type: bug-fix
priority: 🟠
module: Viết bài tự động > Viết nội dung
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159187337, 159088986
---

# Lỗi UX editor

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **thao tác xóa link và quản lý hyperlink trong editor dễ dàng hơn**, Để **tiết kiệm thời gian chỉnh sửa nội dung bài viết**.

3. **Mô tả vấn đề**

Editor có 2 vấn đề UX liên quan đến xử lý hyperlink.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Xóa link cồng kềnh | Thao tác xóa link hiện tại quá nhiều bước (xóa anchor → xóa link → bấm tick). Cần có nút "Hủy liên kết" (unlink) nhanh. |
| Tự động link text dạng .md | Hệ thống tự động tạo hyperlink cho các text có dạng `abc.md` — hành vi không mong muốn, chưa xác định nguyên nhân. |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Thêm nút "Hủy liên kết" | Bổ sung nút Unlink trên toolbar hoặc context menu khi chọn text có link. Click 1 lần → xóa hyperlink, giữ lại text. |
| Sửa auto-link .md | Tắt hoặc sửa logic tự động tạo hyperlink cho text dạng `*.md`. Chỉ auto-link khi text là URL hợp lệ (http/https). |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Chọn text có link → hiển thị nút "Hủy liên kết". Click → xóa link, giữ text gốc. |
| AC-02 | Text dạng `abc.md` không bị tự động tạo hyperlink. |
| AC-03 | Text dạng URL hợp lệ (http/https) vẫn auto-link bình thường (nếu có tính năng này). |
