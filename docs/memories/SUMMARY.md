---
generated_at: 2026-06-09
total_pages: 12
---

# Memories Summary

Tổng hợp 12 tài liệu Confluence.

---

## Viết bài tự động (ID: 124190721)

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

... [truncated]
---

## Quản lý bài viết (ID: 159088939)

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
---

## Viết bài hàng loạt (ID: 159088962)

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
---

## Luồng AI viết bài (ID: 159088986)

# Luồng AI viết bài

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Luồng AI viết bài | 17.05.2026 |

2. **Mục đích**

Mô tả luồng xử lý từ lúc outline sẵn sàng cho đến khi bài viết hoàn chỉnh (nội dung + hình ảnh), sẵn sàng xuất bản.

3. **Tổng quan luồng**

Outline hoàn chỉnh
│
▼
[1] Cấu hình viết (tác giả, model viết, model gen hình, category)
│
▼
[2] AI viết nội dung từng section (streaming)
│
▼
[3] AI gen hình ảnh minh hoạ
│
▼
[4] Preview & chỉnh sửa từng đoạn
│
├──→ Lưu nháp → "Quản lý bài viết" (Nháp)
└──→ Hoàn thành → "Quản lý bài viết" (Hoàn thành)

4. **Chi tiết từng bước**

**Bước 1 — Cấu hình viết**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Kích hoạt | Người dùng nhấn "Viết bài" từ Tạo Outline hoặc mở từ "Outline đã lưu". |
| Tác giả | Chọn từ danh sách đã cấu hình. Ảnh hưởng văn phong & giọng điệu. |
| Model viết | Chọn model AI. VD: Claude Sonnet 4.6, GPT-4o. |
| Model gen hình | Chọn model AI tạo hình. VD: GPT Image 2.0. |
| Category | Chọn category WordPress cho bài viết. |

**Bước 2 — AI viết nội dung**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Xử lý | AI viết **từng section** (H2/H3) theo thứ tự outline. |
| Input | Outline + keyword + prompt (Core + Structure + Structure Item) + tác giả. |
| Streaming | Mỗi section viết xong hiển thị ngay. Không chờ toàn bộ. |
| Auto-map | AI tự động chèn sản phẩm tham chiếu + internal links vào nội dung phù hợp. |

**Bước 3 — AI gen hình ảnh**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Tự động | AI tạo hình minh hoạ cho các section phù hợp (dựa trên nội dung). |
| Thủ công | Người dùng nhấn "Gen hình" tại section → nhập mô tả → AI tạo hình. |
| Thay thế | Upload hình mới hoặc gen lại hình. |

**Bước 4 — Preview & chỉnh sửa**

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Preview | Hiển thị bài viết đầy đủ dạng render. |
| Chỉnh sửa | Nhấn vào section → editor trực tiếp. |
| AI viết lại | Nút "Viết lại" → AI viết lại 1 section (giữ heading). |
| AI mở rộng | Nút "Mở rộng" → AI bổ sung nội dung cho section. |
| AI rút gọn | Nút "Rút gọn" → AI thu ngắn nội dung section. |
| Quay lại | Quay về chỉnh sửa outline (giữ nội dung đã viết). |

**Bước 5 — Lưu**

|  |  |
| --- | --- |
| **Hành động** | **Kết quả** |
| Lưu nháp | Bài viết lưu trạng thái 📝 Nháp trong "Quản lý bài viết". |
| Hoàn thành | Bài viết chuyển trạng thái ✅ Hoàn thành → sẵn sàng Xuất bản. |

5. **Luồng Viết bài hàng loạt**

Khi sử dụng "Viết bài hàng loạt", hệ thống tự động xử lý **Bước 1 → 3** cho mỗi keyword:

|  |  |
| --- | --- |
| **Hạng mục** | **Chi tiết** |
| Cấu hình chung | Site + model viết + model gen hình (áp dụng tất cả keyword). |
| Cấu hình riêng | Mỗi keyword: tác giả + category riêng. |
| Pipeline | Phân tích Google → Tạo outline → Viết bài → Gen hình (tự động, tuần tự). |
| Giới hạn | Tối đa 5 keyword / lần, 10 bài / ngày. |
| Kết quả | Bài viết tự động → "Quản lý bài viết" nguồn = "Viết bài hàng loạt". |

6. **Sơ đồ liên kết Function**

|  |  |
| --- | --- |
| **Bước** | **Function liên quan** |
| Input | Tạo Outline / Outline đã lưu |
| 1–5 | Viết nội dung |
| Hàng loạt | Viết bài hàng loạt |
| Output | Quản lý bài viết |
| → Tiếp | Xuất bản |
---

## Từ khoá viết bài (ID: 159154564)

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
---

## Outline đã lưu (ID: 159154639)

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
---

## Luồng xuất bản WordPress (ID: 159154697)

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
---

## Cấu hình viết bài (ID: 159187096)

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
---

## Viết bài (ID: 159187337)

# Viết bài

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Viết bài | 17.05.2026 |

2. **Link task:**
3. **User Story:** Là một **thành viên Marketing**, Tôi muốn **tạo outline từ phân tích đối thủ, sau đó AI viết bài dựa trên outline**, Để **nhanh chóng tạo bài viết SEO chất lượng**.

4. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| • Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). |
| • Người dùng được cấp quyền `Quản lý Viết bài tự động`. |
| • Đã cấu hình prompt AI, tác giả, internal links, nguồn dữ liệu. |

5. **Workflow**

|  |
| --- |
| **Basic Flow: Viết bài** |
| **BF01:** Chọn từ khoá → Tạo outline (phân tích đối thủ + AI tạo outline). |
| **BF02:** Cấu hình viết bài (tác giả, model AI, model gen hình, category). |
| **BF03:** AI viết bài theo từng section dựa trên outline. |
| **BF04:** Người dùng chỉnh sửa / viết lại theo đoạn. |
| **BF05:** Lưu bài viết. |

6. **Mô tả chức năng**

Gồm **2 bước chính**, mỗi bước có trang chi tiết riêng:

|  |  |  |
| --- | --- | --- |
| **Bước** | **Nội dung** | **Trang chi tiết** |
| **Bước 1: Tạo Outline** | Chọn Site + keyword → phân tích Google → AI tạo outline → chỉnh sửa. | Tạo Outline |
| **Bước 2: Viết nội dung** | Cấu hình (tác giả, model, category) → AI viết từng section → chỉnh sửa → lưu. | Viết nội dung |

7. **Acceptance Criteria**

|  |  |
| --- | --- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Luồng viết bài hoàn chỉnh: Tạo Outline → Viết nội dung → Lưu. |
| AC-02 | Có thể quay lại chỉnh sửa outline trong quá trình viết. |
| AC-03 | Chi tiết AC từng bước: xem trang con tương ứng. |
---

## Xuất bản (ID: 159187398)

# Xuất bản

1. **Lịch sử thay đổi**

|  |  |  |  |
| --- | --- | --- | --- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày** |
| v1.0 | Cao Lê Viết Tiến | Tạo mới Function Xuất bản | 17-05-2026 |
| v1.1 🆕 | Cao Lê Viết Tiến | Thêm Lịch đăng bài (calendar view, hàng đợi) + API WordPress scheduled post | 08-06-2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **xuất bản bài viết đã hoàn thành lên WordPress site, bao gồm hẹn giờ đăng bài và quản lý lịch đăng bài trên giao diện calendar** [v1.1], Để **bài viết được đăng tải đúng thời điểm tối ưu và kiểm soát nội dung xuất bản theo kế hoạch** [v1.1].

3. **Precondition**

|  |
| --- |
| **Điều kiện tiên quyết** |
| * Người dùng đã đăng nhập thành công vào hệ thống MKTOPS (SSO Workplace). * Người dùng được cấp quyền `Quản lý Viết bài tự động`. * Bài viết ở trạng thái **Hoàn thành**. * Hệ thống đã kết nối với WordPress site (WP REST API v2). |

4. **Workflow**

|  |
| --- |
| **Basic Flow: Xuất bản** |
| * **BF01:** Chọn bài viết cần xuất bản (từ Quản lý bài viết). * **BF02:** Xác nhận thông tin xuất bản (category, tác giả, slug, thumbnail). * **BF03:** Chọn hình thức xuất bản: **Đăng ngay** / **Lưu nháp** / **Hẹn giờ**. [v1.1] * **BF04:** Nếu chọn **Hẹn giờ** → Chọn ngày giờ đăng bài → Hệ thống gửi API WordPress với status `future` + `date` tương ứng. [v1.1] * **BF05:** Nhấn "Xuất bản" → import bài viết lên WordPress. * **BF06:** Hệ thống trả về URL bài viết đã đăng / đã lên lịch. [v1.1] * **BF07:** Bài viết hẹn giờ xuất hiện trong Lịch đăng bài (calendar). [v1.1] * **BF08:** Người dùng có thể xem, sửa giờ, hoặc huỷ lịch từ calendar. [v1.1] * **EF01:** Xuất bản thất bại → hiển thị thông báo lỗi chi tiết (lỗi API, lỗi kết nối). [v1.1] * **EF02:** Ngày hẹn đăng trong quá khứ → hiển thị cảnh báo, không cho lưu. [v1.1] |

5. **Mô tả chức năng**

Giao diện gồm 2 Tab: [v1.1]

|  |  |  |
| --- | --- | --- |
| **Khối chức năng** | **Tab** | **Mô tả** |
| **Xuất bản bài viết** | Tab 1 | Form xác nhận thông tin và xuất bản bài viết lên WordPress. |
| **Lịch đăng bài** [v1.1] | Tab 2 | Calendar view hiển thị toàn bộ bài viết đã lên lịch (Scheduled) và đã đăng (Published). |

6. **Chi tiết: Tab 1 — Xuất bản bài viết**

**6.1. Thông tin xuất bản**

|  |  |  |
| --- | --- | --- |
| **Trường thông tin** | **Loại** | **Mô tả** |
| Site đích | Danh sách chọn | * WordPress site để xuất bản. Kế thừa từ Site đã chọn khi tạo outline. |
| Tiêu đề | Nhập văn bản | * Tiêu đề bài viết. Có thể chỉnh sửa trước khi xuất bản. |
| Slug | Nhập văn bản | * Tự động sinh từ tiêu đề. Cho phép sửa. |
| Category | Danh sách chọn | * Category trên WordPress. Kế thừa từ cấu hình viết bài. |
| Tác giả WP | Danh sách chọn | * Tác giả trên WordPress (map với tác giả đã chọn khi viết). |
| Thumbnail | Hình ảnh | * Ảnh đại diện bài viết. Cho phép thay đổi. |
| Hình thức xuất bản [v1.1] | Danh sách chọn | * **Đăng ngay** (Publish) / **Lưu nháp** (Draft) / **Hẹn giờ** (Scheduled). Mặc định: Đăng ngay. |
| Ngày hẹn đăng [v1.1] | Chọn ngày giờ | * Hiển thị khi chọn "Hẹn giờ". Chọn ngày giờ đăng bài. Không được chọn thời gian trong quá khứ (EF02). |

**6.2. Preview trước khi xuất bản**

|  |  |
| --- | --- |
| **Thành phần** | **Mô tả** |
| Preview nội dung | Xem toàn bộ bài viết dạng render (như trên WordPress). |
| Kiểm tra SEO | Hiển thị: title tag, meta description, slug, word count. |

**6.3. Hành động**

|  |  |
| --- | --- |
| **Nút** | **Mô tả** |
| **Xuất bản** | Import bài viết lên WordPress qua API. Hiển thị progress. |
| **Quay lại** | Quay về Quản lý bài viết. |

**6.4. Kết quả xuất bản**

Sau khi xuất bản thành công:

|  |  |
| --- | --- |
| **Thông tin** | **Mô tả** |
| URL bài viết | Link trực tiếp đến bài viết trên WordPress. Nhấn để mở tab mới. |
| Trạng thái [v1.1] | • Đăng ngay → 🚀 **Đã đăng** trong Quản lý bài viết. • Hẹn giờ → 📅 **Đã lên lịch** (kèm ngày giờ). • Lưu nháp → 📝 **Nháp trên WP**. |
| Thông báo | Hiển thị thông báo thành công kèm URL. |

7. **Chi tiết: Tab 2 — Lịch đăng bài [v1.1]**

**7.1. Calendar View**

|  |  |
| --- | --- |
| **Thành phần** | **Mô tả** |
| Chế độ xem | • **Tháng** / **Tuần** / **Ngày**. Mặc định: Tháng. |
| Hiển thị bài viết | • Mỗi ô ngày hiển thị danh sách bài viết đã lên lịch / đã đăng trong ngày đó. |
| Mã màu | • 📅 **Xanh dương**: Đã lên lịch (Scheduled). • 🚀 **Xanh lá**: Đã đăng (Published). • 📝 **Xám**: Nháp (Draft). |
| Click vào bài | • Mở popup chi tiết: Tiêu đề, Site, Category, Tác giả, Ngày giờ đăng, Trạng thái. |

**7.2. Danh sách hàng đợi (Upcoming)**

|  |  |  |
| --- | --- | --- |
| **Trường thông tin** | **Loại** | **Mô tả** |
| Tiêu đề | Văn bản | • Tiêu đề bài viết. |
| Site | Văn bản | • WordPress site đích. |
| Ngày giờ đăng | Ngày giờ | • Thời gian dự kiến đăng bài. |
| Trạng thái | Nhãn | • 📅 Đã lên lịch / 🚀 Đã đăng. |
| Thao tác | Nút | • **Sửa giờ** / **Đăng ngay** / **Huỷ lịch**. |

**Sắp xếp:** Theo ngày giờ đăng (gần nhất trước)

**Bộ lọc:**

... [truncated]
---

## Luồng lấy keyword trending (ID: 159187433)

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
---

## Luồng phân tích đối thủ & tạo outline (ID: 159187456)

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

