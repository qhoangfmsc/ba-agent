---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/124190721
page_id: 124190721
title: Viết bài tự động
space: VNXMKT
crawled_at: 2026-06-10
---

# Viết bài tự động

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới US Viết bài tự động | 15.05.2026 |
| v1.1 | Cao Lê Viết Tiến | Cập nhật toàn bộ functions + basic flow chính | 17.05.2026 |

2. **Link task**

3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **hệ thống tự động lấy keyword trending, phân tích đối thủ, tạo outline và viết bài bằng AI**, Để **nhanh chóng tạo nội dung SEO chất lượng và xuất bản lên WordPress tự động**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền sử dụng tính năng Viết bài tự động. |
| • Hệ thống đã kết nối với DataForSEO API. |
| • Hệ thống đã kết nối với WordPress site (để xuất bản). |
| • Hệ thống đã cấu hình AI model (viết nội dung + gen hình ảnh). |

5. **Basic Flow — Luồng chạy chính**

[CẤU HÌNH]
Nguồn DataForSEO · Sản phẩm tham chiếu · Prompt AI · Tác giả · Internal Links
│
▼
[TỪ KHOÁ]
Sync danh mục trending → AI đối chiếu sản phẩm → Sinh keyword
│
▼
[TẠO OUTLINE]
Chọn Site + keyword → Phân tích Google (15 bài TOP) → AI tạo outline → Chỉnh sửa
│
├──→ Lưu nháp → "Outline đã lưu"
▼
[VIẾT NỘI DUNG]
Chọn tác giả + model → AI viết từng section (streaming) → AI gen hình → Chỉnh sửa
│
▼
[QUẢN LÝ BÀI VIẾT]
Danh sách bài viết · Lọc theo trạng thái / nguồn · Tìm kiếm
│
▼
[XUẤT BẢN]
Xác nhận thông tin → Preview + SEO check → Import WordPress → URL bài viết

**Luồng phụ — Viết bài hàng loạt:**

Cấu hình chung (Site + model) → Thêm keyword (tối đa 5/lần, 10 bài/ngày)
→ Hệ thống tự động: Phân tích → Outline → Viết → Gen hình
→ Kết quả → "Quản lý bài viết" (nguồn: Viết bài hàng loạt)

6. **Mô tả chức năng**

**Nhóm 1 — Cấu hình**

|  |  |  |
| --- | --- | --- |
| **Khối chức năng** | **Mô tả** | **Trang chi tiết** |
| **Cấu hình viết bài** | Trang tổng hợp 4 tab cấu hình: Prompt AI, Tác giả, Internal Links, Nguồn dữ liệu. | Cấu hình viết bài |
| ├ Prompt AI | Cấu hình prompt cho AI: Core, Structure, Structure Item. | Prompt AI |
| ├ Tác giả | Quản lý tác giả viết bài (CRUD + phong cách viết). | Tác giả |
| ├ Internal Links | Quản lý danh sách internal links tự động chèn vào bài viết. | Internal Links |
| └ Nguồn dữ liệu | Nguồn DataForSEO (danh mục trending) + Sản phẩm tham chiếu. | Nguồn dữ liệu |

**Nhóm 2 — Viết bài**

|  |  |  |
| --- | --- | --- |
| **Khối chức năng** | **Mô tả** | **Trang chi tiết** |
| **Từ khoá viết bài** | Keyword tổng hợp từ nguồn dữ liệu. Lọc, tìm kiếm, xem biến thể long-tail. | Từ khoá viết bài |
| **Viết bài** | Function cha: bao gồm Tạo Outline + Viết nội dung. | Viết bài |
| ├ Tạo Outline | Chọn Site + keyword → phân tích Google → AI tạo outline → chỉnh sửa. | Tạo Outline |
| └ Viết nội dung | Cấu hình (tác giả, model, category) → AI viết từng section → chỉnh sửa → lưu. | Viết nội dung |
| **Viết bài hàng loạt** | Tạo nhiều bài cùng lúc (tối đa 5/lần, 10 bài/ngày). Tự động pipeline. | Viết bài hàng loạt |
| **Outline đã lưu** | Danh sách outline lưu nháp. Tiếp tục chỉnh sửa hoặc viết bài. | Outline đã lưu |

**Nhóm 3 — Quản lý & xuất bản**

|  |  |  |
| --- | --- | --- |
| **Khối chức năng** | **Mô tả** | **Trang chi tiết** |
| **Quản lý bài viết** | Bảng danh sách bài viết SEO. Tìm kiếm, lọc theo trạng thái / nguồn. | Quản lý bài viết |
| **Xuất bản** | Xuất bản bài viết lên WordPress (Publish / Draft / Scheduled). | Xuất bản |

7. **Luồng xử lý**

|  |  |  |
| --- | --- | --- |
| **Luồng** | **Mô tả** | **Trang chi tiết** |
| **Luồng lấy keyword trending** | DataForSEO → Sync danh mục → AI đối chiếu sản phẩm → Sinh keyword. | Luồng lấy keyword trending |
| **Luồng phân tích đối thủ & tạo outline** | Keyword → Google 15 bài TOP → Trích xuất heading → AI tạo outline. | Luồng phân tích đối thủ & tạo outline |
| **Luồng AI viết bài** | Outline + cấu hình → AI viết từng section (streaming) + gen hình → Preview. | Luồng AI viết bài |
| **Luồng xuất bản WordPress** | Chọn bài → Xác nhận thông tin → Preview + SEO → Import WordPress. | Luồng xuất bản WordPress |

8. **Timeline hoàn thành**

**Deadline phát triển: 29.05.2026**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **#** | **Function** | **Độ ưu tiên** | **BRD** | **Dev** |
| 1 | Cấu hình viết bài (Prompt AI · Tác giả · Internal Links · Nguồn dữ liệu) | 🔴 Rất cao | ✅ | ⏳ |
| 2 | Từ khoá viết bài | 🔴 Rất cao | ✅ | ⏳ |
| 3 | Tạo Outline | 🔴 Rất cao | ✅ | ⏳ |
| 4 | Viết nội dung | 🔴 Rất cao | ✅ | ⏳ |
| 5 | Outline đã lưu | 🟠 Cao | ✅ | ⏳ |
| 6 | Quản lý bài viết | 🟠 Cao | ✅ | ⏳ |
| 7 | Xuất bản | 🟡 Trung bình | ✅ | ⏳ |
| 8 | Viết bài hàng loạt | 🟡 Trung bình | ✅ | ⏳ |

9. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| **Cấu hình** | |
| AC-01 | Cấu hình nguồn DataForSEO + sản phẩm tham chiếu thành công. |
| AC-02 | Cấu hình Prompt AI (Core, Structure, Structure Item) hoạt động. |
| AC-03 | CRUD tác giả viết bài thành công. |
| AC-04 | Quản lý Internal Links thành công. |
| **Từ khoá** | |
| AC-05 | Hệ thống lấy keyword trending từ DataForSEO thành công. |
| AC-06 | AI đối chiếu danh mục → sản phẩm phù hợp. |
| AC-07 | Hiển thị keyword + biến thể long-tail, lọc/tìm kiếm hoạt động. |
| **Outline** | |
| AC-08 | Chọn keyword → phân tích Google → lấy 15 bài TOP. |
| AC-09 | AI tạo outline gợi ý. Chỉnh sửa (thêm/sửa/xoá/kéo thả) hoạt động. |
| AC-10 | Lưu nháp outline → "Outline đã lưu". |
| **Viết bài** | |
| AC-11 | AI viết bài từng section (streaming) theo outline + prompt + tác giả. |
| AC-12 | AI gen hình ảnh minh hoạ. Auto-map sản phẩm + internal links. |
| AC-13 | Chỉnh sửa / viết lại / mở rộng / rút gọn từng section. |
| AC-14 | Viết bài hàng loạt: tối đa 5/lần, 10 bài/ngày, pipeline tự động. |
| **Quản lý** | |
| AC-15 | Bảng bài viết: tìm kiếm, lọc trạng thái/nguồn, sắp xếp. |
| **Xuất bản** | |
| AC-16 | Xuất bản lên WordPress (Publish / Draft / Scheduled) thành công. |
| AC-17 | Trả về URL bài viết. Cập nhật trạng thái "Đã đăng". |
| **Phân quyền** | |
| AC-18 | Chỉ người dùng có quyền mới truy cập tính năng Viết bài tự động. |
