---
task_id: TASK-2026-0609-6
title: Lỗi Preview WP
type: bug-fix
priority: 🟠
module: Viết bài tự động > Xuất bản
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159187398, 159154697
---

# Lỗi Preview WP

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **xem preview bài viết trên WordPress trực tiếp từ tool**, Để **kiểm tra bài viết trước khi publish chính thức**.

3. **Mô tả vấn đề**

Tính năng Preview WP không hoạt động, user không xem được bài viết đã import.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Preview WP không xem được | Bấm vào nút Preview WP trên tool không xem được bài viết. Link trỏ tới WP admin (`vietnix.vn/wp-admin/post.php?post=475185&action=edit`). Dùng tài khoản Growth Marketing không truy cập được, trong khi các post khác xem bình thường. |
| Lỗi quyền truy cập | Có thể liên quan đến quyền truy cập post cụ thể trên WordPress (post được tạo bởi user khác hoặc quyền không đủ). |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Kiểm tra quyền WP | Xác minh tài khoản dùng để import bài → post owner trên WP. Đảm bảo tài khoản Growth Marketing có quyền xem/edit post đã import. |
| Sửa link Preview | Link Preview nên trỏ đến URL preview public (không phải WP admin edit) hoặc đảm bảo user có quyền truy cập. |
| Fallback preview | Nếu không truy cập được WP preview → hiển thị preview nội dung ngay trên tool (đã có sẵn tính năng này). |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Bấm Preview WP → mở được bài viết preview (không lỗi 403/404). |
| AC-02 | Tài khoản Growth Marketing có thể xem preview bài viết đã import. |
| AC-03 | Nếu preview WP không khả dụng → có fallback hiển thị trên tool. |
