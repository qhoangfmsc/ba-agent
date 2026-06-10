---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159088939
page_id: 159088939
title: Quản lý bài viết
space: VNXMKT
crawled_at: 2026-06-10
---

# Quản lý bài viết

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Quản lý bài viết | 17.05.2026 |

2. **Link task:**
3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **xem danh sách tất cả bài viết SEO đã tạo, lọc theo trạng thái và nguồn**, Để **theo dõi tiến độ và quản lý nội dung hiệu quả**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền `Xem Viết bài tự động` hoặc `Quản lý Viết bài tự động`. |

5. **Workflow**

|  |
| --- |
| **Basic Flow: Quản lý bài viết** |
| **BF01:** Xem danh sách bài viết SEO. |
| **BF02:** Tìm kiếm bài viết theo tiêu đề. |
| **BF03:** Lọc bài viết theo trạng thái / nguồn / thời gian. |
| **BF04:** Nhấn bài viết → xem chi tiết / chỉnh sửa. |

6. **Mô tả chức năng**

Tên trang: **Bài viết SEO** (sidebar: Danh sách bài viết).

**6.1. Thanh tìm kiếm & bộ lọc**

|  |  |  |
| --- | --- | --- |
| **Thành phần** | **Loại** | **Mô tả** |
| Tìm theo tiêu đề | Nhập văn bản | • Tìm kiếm bài viết theo tiêu đề. |
| Trạng thái | Danh sách chọn | • Tất cả / Nháp / Hoàn thành / Đã đăng. |
| Nguồn | Danh sách chọn | • Tất cả nguồn / Tạo thủ công / Sản xuất hàng loạt. |
| Sắp xếp | Danh sách chọn | • Mới nhất / Cũ nhất / Theo tên. |

**6.2. Bảng danh sách bài viết**

|  |  |  |
| --- | --- | --- |
| **Trường thông tin** | **Loại thông tin** | **Mô tả và ràng buộc** |
| Thumbnail | Hình ảnh | • Ảnh đại diện bài viết (auto gen hoặc upload). |
| Tiêu đề | Văn bản | • Tiêu đề bài viết SEO. Nhấn → mở chi tiết / chỉnh sửa. |
| Tác giả | Văn bản | • Tác giả đã chọn khi viết bài. |
| Nguồn | Nhãn | • Tạo thủ công / Sản xuất hàng loạt. |
| Trạng thái | Nhãn | • 📝 Nháp / ✅ Hoàn thành / 🚀 Đã đăng. |
| Ngày tạo | Ngày giờ | • Thời gian tạo bài viết. Hỗ trợ sắp xếp. |

Trạng thái mặc định khi chưa có bài: *"No data"*.

**6.3. Thao tác với bài viết**

|  |  |
| --- | --- |
| **Thao tác** | **Mô tả** |
| Xem chi tiết | Nhấn tiêu đề → mở preview bài viết đầy đủ. |
| Chỉnh sửa | Mở lại editor → chỉnh sửa nội dung, outline. |
| Đăng bài | Chuyển sang function Đăng bài (import WordPress). |
| Xoá | Xoá bài viết (yêu cầu xác nhận). |

7. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| **Danh sách** | |
| AC-01 | Bảng hiển thị đúng: thumbnail, tiêu đề, tác giả, nguồn, trạng thái, ngày tạo. |
| AC-02 | Bài viết mới tạo tự động xuất hiện trong danh sách. |
| **Tìm kiếm & lọc** | |
| AC-03 | Tìm theo tiêu đề hoạt động. |
| AC-04 | Lọc theo trạng thái (Nháp / Hoàn thành / Đã đăng) hoạt động. |
| AC-05 | Lọc theo nguồn (Tạo thủ công / Sản xuất hàng loạt) hoạt động. |
| AC-06 | Sắp xếp (Mới nhất / Cũ nhất / Theo tên) hoạt động. |
| AC-07 | Các bộ lọc kết hợp được với nhau. |
| **Thao tác** | |
| AC-08 | Nhấn tiêu đề → mở preview bài viết. |
| AC-09 | Chỉnh sửa bài viết hoạt động. |
| AC-10 | Xoá bài viết (có xác nhận) hoạt động. |
| AC-11 | Chuyển sang Đăng bài hoạt động. |
