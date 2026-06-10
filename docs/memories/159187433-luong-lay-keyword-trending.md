---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159187433
page_id: 159187433
title: Luồng lấy keyword trending
space: VNXMKT
crawled_at: 2026-06-09
---

# Luồng lấy keyword trending

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Luồng lấy keyword trending | 17.05.2026 |

2. **Mục đích**

Mô tả luồng xử lý từ lúc dữ liệu trending được lấy từ DataForSEO cho đến khi keyword sẵn sàng hiển thị tại "Từ khoá viết bài".

3. **Tổng quan luồng**

DataForSEO (Google Trends)
│
▼
[1] Sync danh mục trending
│
▼
[2] Import sản phẩm tham chiếu
│
▼
[3] AI đối chiếu (danh mục ↔ sản phẩm)
│
▼
[4] Sinh keyword từ danh mục phù hợp
│
▼
[5] Hiển thị tại "Từ khoá viết bài"

4. **Chi tiết từng bước**

**Bước 1 — Sync danh mục trending**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Admin nhấn "Sync danh mục" (tab Nguồn DataForSEO). |
| Nguồn dữ liệu | DataForSEO API — danh mục Google Trends. |
| Xử lý | Upsert — danh mục mới thêm, danh mục cũ cập nhật search volume. |
| Kết quả | Danh sách danh mục trending được lưu vào hệ thống. |

**Bước 2 — Import sản phẩm tham chiếu**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Admin upload file (.xlsx, .docx) hoặc dán URL trang sản phẩm. |
| Xử lý | Upsert sản phẩm. URL → hệ thống trích xuất thông tin tự động. |
| Kết quả | Danh sách sản phẩm tham chiếu sẵn sàng cho AI đối chiếu. |

**Bước 3 — AI đối chiếu**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Admin nhấn "Chạy AI đối chiếu". |
| Xử lý | AI duyệt toàn bộ danh mục trending → so sánh với sản phẩm tham chiếu → đánh dấu `is_relevant`. |
| Kết quả | Mỗi danh mục có cờ phù hợp / không phù hợp. Chỉ danh mục phù hợp mới sinh keyword. |

**Bước 4 — Sinh keyword**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Tự động khi người dùng truy cập "Từ khoá viết bài" hoặc chọn danh mục. |
| Cách 1 | Chọn danh mục phù hợp → hệ thống sinh keyword từ danh mục đó. |
| Cách 2 | Nhập text tìm kiếm → hệ thống gợi ý keyword liên quan. |
| Cache | Kết quả cache **7 ngày**. Sau 7 ngày tự động làm mới. |
| Biến thể | Mỗi keyword sinh tối đa **30 biến thể** long-tail. Cache 7 ngày. |

**Bước 5 — Hiển thị**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Nơi hiển thị | Trang "Từ khoá viết bài". |
| Thông tin | Keyword · Search Volume · Danh mục · Độ cạnh tranh · Biến thể · Trạng thái. |
| Hành động tiếp | Người dùng chọn keyword → chuyển sang Tạo Outline. |

5. **Điều kiện làm mới dữ liệu**

|  |  |
| --- | --- |
| **Sự kiện** | **Hành động cần làm** |
| Thêm sản phẩm tham chiếu mới | Chạy lại "AI đối chiếu" để cập nhật danh mục phù hợp. |
| Sync danh mục mới | Chạy lại "AI đối chiếu" để đánh dấu danh mục mới. |
| Keyword cache hết hạn (7 ngày) | Hệ thống tự động làm mới khi người dùng truy cập. |

6. **Sơ đồ liên kết Function**

|  |  |
| --- | --- |
| **Bước** | **Function liên quan** |
| 1, 2, 3 | Cấu hình Nguồn dữ liệu |
| 4, 5 | Từ khoá viết bài |
| → Tiếp | Tạo Outline → Viết nội dung |
