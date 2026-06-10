---
task_id: TASK-2026-0609-3
title: Lỗi import WordPress
type: bug-fix
priority: 🔴
module: Viết bài tự động > Xuất bản
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159187398, 159154697
---

# Lỗi import WordPress

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **import bài viết sang WordPress với đầy đủ nội dung, hình ảnh và các block đặc biệt**, Để **bài viết trên WordPress giống chính xác với bản preview trên tool**.

3. **Mô tả vấn đề**

Khi import bài viết từ tool sang WordPress (stag), nhiều thành phần bị mất hoặc hiển thị sai.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Mất ảnh đại diện | Ảnh đại diện (thumbnail) không truy xuất được sau khi import sang WordPress. |
| Bảng compare rỗng | Bảng compare (ưu-nhược điểm) chỉ có định dạng/khung, không có nội dung bên trong. Tự chèn tay block vẫn chỉ hiện format, không có data. |
| Mất tác giả | Phần tác giả không có trên WordPress mặc dù đã chọn tác giả ngay từ khi bắt đầu viết bài. |
| Mất block "Những điểm chính" | Block "Những điểm chính" (key takeaways) bị mất hoàn toàn sau import. |
| Mất ảnh paste | Ảnh chèn bằng cách chụp màn hình + paste vào editor bị mất sau import. Ảnh upload qua tính năng "Chèn ảnh" thì import được. |
| FAQ lỗi trên WordPress | Block FAQ bị lỗi trên WordPress. Bấm "Thử khôi phục" thì mất hết nội dung. |
| Block CTA lỗi | Block CTA (Call to Action) chuyển sang WordPress bị lỗi hiển thị. |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Sửa import thumbnail | Đảm bảo ảnh đại diện được set đúng Featured Image trên WordPress khi import. |
| Sửa import bảng compare | Map đúng data nội dung vào block ưu-nhược điểm WordPress (không chỉ khung format). |
| Sửa import tác giả | Map tác giả hệ thống → tác giả WordPress đúng khi import. |
| Sửa import block "Những điểm chính" | Đảm bảo block key takeaways được convert đúng sang Gutenberg block tương ứng. |
| Xử lý ảnh paste (base64/blob) | Convert ảnh paste (base64/blob) thành file ảnh thực → upload lên WordPress Media Library trước khi import nội dung. |
| Sửa import FAQ | Convert FAQ thành Gutenberg block hoặc schema markup chuẩn trên WordPress. |
| Sửa import CTA | Convert block CTA thành Gutenberg block tương ứng trên WordPress. |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Ảnh đại diện hiển thị đúng trên WordPress sau import (Featured Image). |
| AC-02 | Bảng compare hiển thị đầy đủ nội dung (không chỉ khung rỗng). |
| AC-03 | Tác giả WordPress đúng với tác giả đã chọn trên tool. |
| AC-04 | Block "Những điểm chính" xuất hiện đầy đủ trên WordPress. |
| AC-05 | Ảnh paste (chụp màn hình) hiển thị đúng trên WordPress sau import. |
| AC-06 | Block FAQ hiển thị đúng trên WordPress, không lỗi khi mở editor. |
| AC-07 | Block CTA hiển thị đúng trên WordPress. |
| AC-08 | Toàn bộ nội dung trên WordPress khớp với bản preview trên tool (so sánh visual). |
