---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159154564
page_id: 159154564
title: Từ khoá viết bài
space: VNXMKT
crawled_at: 2026-06-10
---

# Từ khoá viết bài

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Từ khoá viết bài | 17.05.2026 |

2. **Link task:**
3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **xem danh sách từ khoá được tổng hợp từ nguồn dữ liệu đã cấu hình**, Để **chọn từ khoá phù hợp và bắt đầu tạo outline viết bài**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền `Xem Viết bài tự động` hoặc `Quản lý Viết bài tự động`. |
| • Đã cấu hình danh mục theo dõi tại "Cấu hình Nguồn dữ liệu". |

5. **Workflow**

|  |
| --- |
| **Basic Flow: Từ khoá viết bài** |
| **BF01:** Xem danh sách từ khoá (tổng hợp từ nguồn dữ liệu). |
| **BF02:** Lọc từ khoá theo danh mục (tab đầu trang). |
| **BF03:** Tìm kiếm từ khoá. |
| **BF04:** Xem biến thể (long-tail) của từ khoá. |
| **BF05:** Chọn từ khoá → chuyển sang Tạo Outline. |

6. **Mô tả chức năng**

**6.1. Bộ lọc danh mục (đầu trang)**

Hiển thị các **tab danh mục** lấy từ cấu hình (Cấu hình Nguồn dữ liệu > Quản lý danh mục). Tab đầu tiên là **"Tất cả"**, sau đó là các danh mục đang theo dõi. Mỗi tab hiển thị số lượng keyword tương ứng.

VD: `Tất cả (186)` · `AI (135)` · `nhanhoa (37)` · `Sản phẩm (14)`

Nhấn tab → lọc bảng từ khoá theo danh mục đó.

**6.2. Thanh tìm kiếm**

|  |  |  |
| --- | --- | --- |
| **Thành phần** | **Loại** | **Mô tả** |
| Tìm từ khoá | Nhập văn bản | Nhập text → hệ thống gợi ý từ khoá liên quan từ DataForSEO. |
| Nút "Tìm kiếm" | Nút | Tìm từ khoá theo text đã nhập. Kết quả cache 7 ngày. |

**6.3. Bảng từ khoá**

|  |  |  |
| --- | --- | --- |
| **Trường thông tin** | **Loại thông tin** | **Mô tả và ràng buộc** |
| Từ khoá | Văn bản | Từ khoá chính. Dưới dòng: nguồn danh mục · seed. |
| Volume | Số | Lượt tìm kiếm/tháng. Hỗ trợ sắp xếp (mặc định: desc). |
| KD % | Số + Nhãn | Keyword Difficulty (%). Hiển thị màu: 🟢 dễ / 🟠 TB / 🔴 khó. |
| CPC | Số | Cost Per Click ($). |
| Xu hướng | Biểu đồ mini | Sparkline thể hiện xu hướng tìm kiếm. % tăng/giảm so với kỳ trước. |
| Cơ hội SEO | Thanh + Số | Điểm cơ hội SEO (0-2). Thanh màu: 🟢 cao / 🟡 TB / 🔴 thấp. |

**6.4. Bộ lọc & sắp xếp**

|  |  |  |
| --- | --- | --- |
| **Bộ lọc** | **Loại** | **Mô tả** |
| Danh mục | Tab (đầu trang) | Lọc chính theo danh mục đã cấu hình. |
| Volume | Sắp xếp | Sắp xếp tăng/giảm. |
| KD % | Sắp xếp | Sắp xếp tăng/giảm. |
| Xu hướng | Sắp xếp | Sắp xếp tăng/giảm. |
| Cơ hội SEO | Sắp xếp | Sắp xếp tăng/giảm. |

**6.5. Popup biến thể từ khoá**

Khi nhấn cột **Biến thể** → mở popup hiển thị danh sách long-tail:

|  |  |  |
| --- | --- | --- |
| **Trường thông tin** | **Loại thông tin** | **Mô tả** |
| Từ khoá biến thể | Văn bản | VD: "vps là gì", "cách dùng vps", "vps giá rẻ". |
| Search Volume | Số | Lượt tìm kiếm/tháng của biến thể. |
| Thao tác | Nút | **Tạo Outline** — dùng biến thể này làm từ khoá chính. |

Tối đa **30 biến thể** mỗi từ khoá. Cache 7 ngày.

**6.6. Phân trang**

|  |  |
| --- | --- |
| **Thông số** | **Giá trị** |
| Số dòng/trang | 20 |
| Hiển thị tổng | "Từ khoá (N)" |
| Điều hướng | Trang trước / trang sau / nhập số trang |

7. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| **Bộ lọc danh mục** | |
| AC-01 | Hiển thị tab danh mục lấy từ cấu hình. Tab "Tất cả" + các danh mục đang theo dõi. |
| AC-02 | Mỗi tab hiển thị số lượng keyword tương ứng. Nhấn tab → lọc bảng. |
| **Bảng từ khoá** | |
| AC-03 | Hiển thị đúng: Từ khoá (+ nguồn), Volume, KD%, CPC, Xu hướng, Cơ hội SEO. |
| AC-04 | Sắp xếp theo Volume, KD%, Xu hướng, Cơ hội SEO hoạt động. |
| **Tìm kiếm** | |
| AC-05 | Nhập text → gợi ý từ khoá liên quan từ DataForSEO. |
| AC-06 | Kết quả tìm kiếm cache 7 ngày. |
| **Biến thể** | |
| AC-07 | Nhấn biến thể → popup hiển thị tối đa 30 biến thể long-tail. |
| AC-08 | Từ biến thể có thể nhấn "Tạo Outline" trực tiếp. |
| **Chuyển flow** | |
| AC-09 | Nhấn "Tạo Outline" → chuyển sang function Tạo Outline với từ khoá đã chọn. |
| AC-10 | Phân trang 20 dòng/trang hoạt động. |
