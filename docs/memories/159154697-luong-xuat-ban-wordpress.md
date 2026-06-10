---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159154697
page_id: 159154697
title: Luồng xuất bản WordPress
space: VNXMKT
crawled_at: 2026-06-09
---

# Luồng xuất bản WordPress

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Luồng xuất bản WordPress | 17.05.2026 |

2. **Mục đích**

Mô tả luồng xử lý từ lúc bài viết hoàn thành cho đến khi được xuất bản lên WordPress site.

3. **Tổng quan luồng**

Bài viết (trạng thái Hoàn thành)
│
▼
[1] Chọn bài viết cần xuất bản
│
▼
[2] Xác nhận thông tin (site, title, slug, category, tác giả WP)
│
▼
[3] Preview + kiểm tra SEO
│
▼
[4] Xuất bản → WordPress API
│
├──→ Publish (đăng ngay)
├──→ Draft (nháp trên WP)
└──→ Scheduled (hẹn giờ)
│
▼
[5] URL bài viết + trạng thái "Đã đăng"

4. **Chi tiết từng bước**

**Bước 1 — Chọn bài viết**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Từ "Quản lý bài viết" → nhấn "Xuất bản" trên bài viết trạng thái Hoàn thành. |
| Điều kiện | Chỉ bài viết trạng thái ✅ Hoàn thành mới cho phép xuất bản. |

**Bước 2 — Xác nhận thông tin**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Site đích | Kế thừa từ Site đã chọn khi tạo outline. Cho phép đổi. |
| Tiêu đề | Tiêu đề bài viết. Cho phép chỉnh sửa trước khi xuất bản. |
| Slug | Tự động sinh từ tiêu đề. Cho phép sửa thủ công. |
| Category | Kế thừa từ cấu hình viết bài. Cho phép đổi. |
| Tác giả WP | Map tác giả hệ thống → tác giả WordPress. |
| Thumbnail | Ảnh đại diện. Cho phép thay đổi. |
| Trạng thái WP | Publish / Draft / Scheduled. |
| Ngày hẹn đăng | Hiển thị khi chọn Scheduled. |

**Bước 3 — Preview & kiểm tra SEO**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Preview | Xem bài viết dạng render (như trên WordPress). |
| SEO check | Title tag · Meta description · Slug · Word count. |

**Bước 4 — Xuất bản**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Xử lý | Import bài viết lên WordPress qua REST API. Hiển thị progress. |
| Publish | Bài viết đăng ngay, live trên site. |
| Draft | Lưu nháp trên WordPress, chưa public. |
| Scheduled | Hẹn giờ, WordPress tự đăng vào thời gian chỉ định. |

**Bước 5 — Xác nhận kết quả**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Thành công | Hiển thị URL bài viết (mở tab mới). Trạng thái → 🚀 Đã đăng. |
| Thất bại | Hiển thị thông báo lỗi. Cho phép thử lại. |

5. **Sơ đồ liên kết Function**

|  |  |
| --- | --- |
| **Bước** | **Function liên quan** |
| Input | Quản lý bài viết |
| 1–5 | Xuất bản |
| Output | WordPress site |
