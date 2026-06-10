---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159154639
page_id: 159154639
title: Outline đã lưu
space: VNXMKT
crawled_at: 2026-06-10
---

# Outline đã lưu

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Outline đã lưu | 17.05.2026 |

2. **Link task:**
3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **xem danh sách các outline đã lưu nháp**, Để **tiếp tục chỉnh sửa hoặc bắt đầu viết bài từ outline đã tạo trước đó**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền `Xem Viết bài tự động` hoặc `Quản lý Viết bài tự động`. |

5. **Workflow**

|  |
| --- |
| **Basic Flow: Outline đã lưu** |
| **BF01:** Xem danh sách outline đã lưu. |
| **BF02:** Tìm kiếm outline theo keyword / tiêu đề. |
| **BF03:** Lọc outline theo trạng thái. |
| **BF04:** Nhấn outline → tiếp tục chỉnh sửa hoặc chuyển sang Viết bài. |

6. **Mô tả chức năng**

**6.1. Thanh tìm kiếm & bộ lọc**

|  |  |  |
| --- | --- | --- |
| **Thành phần** | **Loại** | **Mô tả** |
| Tìm kiếm | Nhập văn bản | • Tìm outline theo keyword chính hoặc tiêu đề. |
| Trạng thái | Danh sách chọn | • Tất cả / Nháp / Đã viết bài. |
| Sắp xếp | Danh sách chọn | • Mới nhất / Cũ nhất. |

**6.2. Bảng danh sách outline**

|  |  |  |
| --- | --- | --- |
| **Trường thông tin** | **Loại thông tin** | **Mô tả và ràng buộc** |
| Keyword chính | Văn bản | • Từ khoá đã dùng để tạo outline. |
| Site | Nhãn | • Site đích đã chọn khi tạo outline. |
| Số heading | Số | • Tổng số H2/H3 trong outline. |
| Trạng thái | Nhãn | • 📝 Nháp / ✍️ Đang viết / ✅ Đã viết bài. |
| Ngày tạo | Ngày giờ | • Thời gian tạo / lưu outline. |
| Ngày cập nhật | Ngày giờ | • Lần chỉnh sửa gần nhất. |

**6.3. Thao tác**

|  |  |
| --- | --- |
| **Thao tác** | **Mô tả** |
| Chỉnh sửa outline | Nhấn → mở lại màn hình Tạo Outline với dữ liệu đã lưu. |
| Viết bài | Chuyển sang Viết nội dung với outline đã chọn. |
| Xoá | Xoá outline (yêu cầu xác nhận). |

7. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| **Danh sách** | |
| AC-01 | Bảng hiển thị đúng: keyword, site, số heading, trạng thái, ngày tạo, ngày cập nhật. |
| AC-02 | Outline lưu nháp từ Tạo Outline tự động xuất hiện trong danh sách. |
| **Tìm kiếm & lọc** | |
| AC-03 | Tìm theo keyword / tiêu đề hoạt động. |
| AC-04 | Lọc theo trạng thái hoạt động. |
| AC-05 | Sắp xếp (Mới nhất / Cũ nhất) hoạt động. |
| **Thao tác** | |
| AC-06 | Nhấn outline → mở lại Tạo Outline với dữ liệu đã lưu. |
| AC-07 | Chuyển sang Viết bài hoạt động. |
| AC-08 | Xoá outline (có xác nhận) hoạt động. |
