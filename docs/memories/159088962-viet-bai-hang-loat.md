---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159088962
page_id: 159088962
title: Viết bài hàng loạt
space: VNXMKT
crawled_at: 2026-06-10
---

# Viết bài hàng loạt

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Sản xuất hàng loạt | 17.05.2026 |

2. **Link task**

3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **tạo nhiều bài viết cùng lúc bằng cách chọn keyword từ danh sách**, Để **tăng tốc độ sản xuất nội dung SEO hàng ngày**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền `Quản lý Viết bài tự động`. |
| • Đã cấu hình prompt AI, tác giả, nguồn dữ liệu. |

5. **Workflow**

|  |
| --- |
| **Basic Flow: Sản xuất hàng loạt** |
| **BF01:** Cấu hình chung (Site, model viết, model gen hình). |
| **BF02:** Thêm keyword (tối đa 5 keyword / lần). |
| **BF03:** Cấu hình mỗi keyword (keyword chính, sub keywords, tác giả, category). |
| **BF04:** Nhấn sản xuất → hệ thống tự động tạo outline + viết bài cho tất cả keyword. |
| **BF05:** Theo dõi tiến độ từng bài. |

6. **Mô tả chức năng**

**6.1. Thanh cấu hình chung**

|  |  |  |
| --- | --- | --- |
| **Thành phần** | **Loại** | **Mô tả** |
| CẤU HÌNH (label) | Nhãn | • Tiêu đề thanh cấu hình. |
| Site | Danh sách chọn | • Chọn site đích. VD: Vietnix. |
| Model viết | Danh sách chọn | • Model AI viết nội dung. VD: Claude Sonnet 4.6. |
| Model gen hình | Danh sách chọn | • Model AI gen hình ảnh. VD: GPT Image 2.0. |
| Sync categories | Nút | • Đồng bộ danh sách category từ WordPress site đã chọn. |

**6.2. Danh sách keyword**

Nút **"+ Thêm keyword"** — hiển thị counter: `N / 5` (số keyword hiện tại / tối đa mỗi lần).

Mỗi keyword là **1 card** gồm:

|  |  |  |
| --- | --- | --- |
| **Trường** | **Loại** | **Mô tả** |
| STT | Số | • Số thứ tự keyword (1, 2, 3...). |
| Tác giả | Danh sách chọn | • Chọn tác giả cho bài viết này. |
| Sync categories | Nút | • Đồng bộ category cho keyword này. |
| Keyword | Tìm kiếm + chọn | • **Chính**: Chọn từ danh sách "Từ khoá viết bài" (autocomplete). **Phụ**: Nhập thủ công. |
| Sub keywords | Nhập văn bản | • Tuỳ chọn. Placeholder: "Sub keywords...". |

**6.3. Giới hạn**

|  |  |
| --- | --- |
| **Giới hạn** | **Giá trị** |
| Số keyword / lần sản xuất | Tối đa **5** |
| Số bài viết / ngày | Tối đa **10** |
| Khi đạt giới hạn ngày | Hiển thị thông báo: "Đã đạt giới hạn 10 bài/ngày". Không cho thêm. |

**6.4. Sản xuất & theo dõi tiến độ**

Sau khi nhấn sản xuất, hệ thống xử lý tuần tự mỗi keyword:

|  |  |
| --- | --- |
| **Bước** | **Mô tả** |
| 1. Phân tích Google | Lấy 15 bài TOP → trích xuất outline đối thủ. |
| 2. AI tạo outline | Tạo outline từ dữ liệu đối thủ + prompt. |
| 3. AI viết bài | Viết nội dung từng section theo outline. |
| 4. AI gen hình | Gen hình ảnh minh hoạ. |

Hiển thị progress cho từng keyword: ⏳ Đang xử lý / ✅ Hoàn thành / ❌ Lỗi.

Bài viết hoàn thành → tự động xuất hiện trong **Quản lý bài viết** với nguồn = "Sản xuất hàng loạt".

7. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| **Cấu hình** | |
| AC-01 | Chọn Site, model viết, model gen hình hoạt động. |
| AC-02 | Sync categories từ WordPress hoạt động. |
| **Keyword** | |
| AC-03 | Thêm keyword (tối đa 5 / lần) hoạt động. Counter hiển thị đúng. |
| AC-04 | Keyword: chọn từ "Từ khoá viết bài" (autocomplete) hoặc nhập thủ công. |
| AC-05 | Xoá keyword khỏi danh sách hoạt động. |
| **Giới hạn** | |
| AC-06 | Không cho thêm quá 5 keyword / lần. |
| AC-07 | Không cho sản xuất quá 10 bài / ngày. Hiển thị thông báo khi đạt giới hạn. |
| **Sản xuất** | |
| AC-08 | Hệ thống tự động: phân tích Google → tạo outline → viết bài → gen hình cho mỗi keyword. |
| AC-09 | Hiển thị progress từng keyword (đang xử lý / hoàn thành / lỗi). |
| AC-10 | Bài viết hoàn thành tự động xuất hiện trong Quản lý bài viết với nguồn "Sản xuất hàng loạt". |
| AC-11 | Nếu 1 keyword lỗi, các keyword khác vẫn tiếp tục xử lý. |
