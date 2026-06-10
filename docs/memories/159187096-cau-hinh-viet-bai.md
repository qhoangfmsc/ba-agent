---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159187096
page_id: 159187096
title: Cấu hình viết bài
space: VNXMKT
crawled_at: 2026-06-09
---

# Cấu hình viết bài

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Cấu hình viết bài | 15.05.2026 |

2. **Link task:**
3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **cấu hình prompt AI, tác giả, internal links và nguồn dữ liệu sản phẩm**, Để **hệ thống có đủ dữ liệu đầu vào cho việc tạo outline và viết bài tự động**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền `Quản lý Viết bài tự động`. |

5. **Workflow**

|  |
| --- |
| **Basic Flow: Cấu hình viết bài** |
| **BF01:** Tuỳ chỉnh prompt AI: Tạo outline / Viết bài / Góc tiếp cận. |
| **BF02:** Quản lý tác giả viết bài (tên, đặc điểm tính cách, lĩnh vực, văn phong). |
| **BF03:** Quản lý internal links (link sản phẩm + link bài viết). |
| **BF04:** Cấu hình nguồn dữ liệu (DataForSEO, sản phẩm tham chiếu). |

6. **Mô tả chức năng**

Giao diện gồm **4 tab**, mỗi tab có trang chi tiết riêng:

|  |  |  |
| --- | --- | --- |
| **Tab** | **Nội dung** | **Trang chi tiết** |
| **Tab 1: Prompt AI** | 2 tab con (Prompt AI, Góc tiếp cận). 3 lớp prompt: Core → Structure → Structure Item. | Cấu hình Prompt AI |
| **Tab 2: Tác giả** | Quản lý tác giả: tên, đặc điểm tính cách, lĩnh vực chuyên môn, văn phong & giọng điệu. | Cấu hình Tác giả |
| **Tab 3: Internal Links** | 2 tab con: Link sản phẩm (Topic, Product, Keyword, Search Volume, Link LDP) + Link bài viết (URL, Keyword, Subcategory, Parent Category). | Cấu hình Internal Links |
| **Tab 4: Nguồn dữ liệu** | 2 tab con: Nguồn DataForSEO (sync + AI đối chiếu) + Sản phẩm tham chiếu (upload / URL). | Cấu hình Nguồn dữ liệu |

7. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Giao diện hiển thị đúng 4 tab. |
| AC-02 | Chuyển đổi giữa các tab hoạt động mượt. |
| AC-03 | Chỉ quyền `Quản lý Viết bài tự động` mới truy cập trang Cấu hình. |
| AC-04 | Chi tiết AC từng tab: xem trang con tương ứng. |
