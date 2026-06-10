---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159187456
page_id: 159187456
title: Luồng phân tích đối thủ & tạo outline
space: VNXMKT
crawled_at: 2026-06-09
---

# Luồng phân tích đối thủ & tạo outline

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Luồng phân tích đối thủ & tạo outline | 17.05.2026 |

2. **Mục đích**

Mô tả luồng xử lý từ lúc người dùng chọn keyword cho đến khi có outline bài viết hoàn chỉnh, sẵn sàng chuyển sang viết nội dung.

3. **Tổng quan luồng**

Keyword (từ "Từ khoá viết bài" hoặc nhập thủ công)
│
▼
[1] Chọn Site đích + keyword + sub keywords
│
▼
[2] Phân tích Google — lấy 15 bài TOP
│
▼
[3] Trích xuất outline đối thủ (H1, H2, H3)
│
▼
[4] AI tổng hợp + áp dụng prompt → Outline gợi ý
│
▼
[5] Người dùng chỉnh sửa outline
│
├──→ Lưu nháp → "Outline đã lưu"
│
└──→ Viết bài → Chuyển sang "Viết nội dung"

4. **Chi tiết từng bước**

**Bước 1 — Thiết lập**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Người dùng nhấn "Tạo Outline" từ keyword hoặc truy cập trực tiếp. |
| Site đích | Chọn site output (VD: Vietnix). Quyết định category + tác giả WP khả dụng. |
| Keyword chính | **Chính**: Chọn từ "Từ khoá viết bài" (autocomplete). **Phụ**: Nhập thủ công. |
| Sub keywords | Tuỳ chọn. Giúp AI mở rộng phạm vi nội dung outline. |

**Bước 2 — Phân tích Google**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Người dùng nhấn nút "Phân tích". |
| Xử lý | Hệ thống tìm kiếm Google theo keyword → lấy **15 bài viết TOP** (SERP). |
| Kết quả | Danh sách 15 URL bài đối thủ kèm tiêu đề. |

**Bước 3 — Trích xuất outline đối thủ**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Xử lý | Hệ thống truy cập từng URL → phân tích cấu trúc heading (H1, H2, H3). |
| Kết quả | Outline đối thủ hiển thị bên **trái** (chỉ đọc). Nhấn từng bài để xem chi tiết. |

**Bước 4 — AI tạo outline gợi ý**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Xử lý | AI tổng hợp 15 outline đối thủ → áp dụng prompt (Core + Structure) → tạo outline gợi ý. |
| Input AI | Outline đối thủ + keyword + sub keywords + prompt đã cấu hình. |
| Kết quả | Outline gợi ý hiển thị bên **phải** (có thể chỉnh sửa). |

**Bước 5 — Chỉnh sửa & lưu**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Chỉnh sửa | Thêm / sửa / xoá heading, kéo thả sắp xếp, chuyển cấp H2 ↔ H3. |
| AI tạo lại | Nút "Tạo lại" → AI tạo outline mới (giữ dữ liệu đối thủ). |
| Lưu nháp | Lưu → xuất hiện trong "Outline đã lưu". Quay lại chỉnh sửa bất cứ lúc nào. |
| Viết bài | Lưu + chuyển sang "Viết nội dung" với outline đã tạo. |

5. **Dữ liệu đầu vào & đầu ra**

|  |  |
| --- | --- |
| **Đầu vào** | **Đầu ra** |
| Keyword chính + sub keywords | Outline bài viết (danh sách H2/H3) |
| 15 bài đối thủ TOP Google | Outline đối thủ (tham khảo) |
| Prompt cấu hình (Core + Structure) | Outline gợi ý do AI tạo |

6. **Sơ đồ liên kết Function**

|  |  |
| --- | --- |
| **Bước** | **Function liên quan** |
| Input | Từ khoá viết bài |
| 1–5 | Tạo Outline |
| Lưu nháp | Outline đã lưu |
| → Tiếp | Viết nội dung |
