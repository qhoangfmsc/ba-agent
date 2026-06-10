---
source: https://vietnixvn.atlassian.net/wiki/spaces/VNXMKT/pages/159088986
page_id: 159088986
title: Luồng AI viết bài
space: VNXMKT
crawled_at: 2026-06-09
---

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
