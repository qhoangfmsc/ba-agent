---
task_id: TASK-2026-0609-2
title: Lỗi format editor nội dung
type: bug-fix
priority: 🔴
module: Viết bài tự động > Viết nội dung
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159187337, 159088986
---

# Lỗi format editor nội dung

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **editor hiển thị đúng format, tự động lưu nội dung, và đồng bộ mục lục khi chỉnh sửa**, Để **tránh mất dữ liệu và đảm bảo bài viết hiển thị chính xác**.

3. **Mô tả vấn đề**

Editor viết nội dung gặp nhiều lỗi về format, thiếu tính năng auto-save, và mục lục không đồng bộ khi chỉnh sửa heading.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Format in đậm lỗi | Nội dung bài viết bị lỗi format: chỗ in đậm chỗ không, không nhất quán. |
| Thiếu format văn bản bình thường | Chỉ có format heading (H2, H3), chưa có format chuyển thành văn bản bình thường (paragraph). WordPress có format này nhưng tool chưa có. |
| H3 không nhảy đến nội dung | Khi bấm vào H3 trong mục lục không nhảy đến phần nội dung tương ứng (H2 thì nhảy được). |
| Mục lục không update khi sửa H2 | Sửa H2 trong bài viết (đã lưu) nhưng khi load lại, mục lục không cập nhật H2 mới. |
| FAQ thiếu câu trả lời | Phần FAQ gặp lỗi: có câu hỏi nhưng không có câu trả lời. |
| Chưa có auto-save | Nội dung bài viết thường rất dài nhưng chưa có tính năng tự động lưu, rủi ro mất dữ liệu khi viết bài. |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Sửa format in đậm | Đảm bảo format bold/italic nhất quán trong toàn bộ nội dung AI viết ra. |
| Thêm format paragraph | Bổ sung option "Văn bản bình thường" trong toolbar format (tương tự WordPress editor). |
| Sửa anchor H3 | Gắn anchor cho H3 trong mục lục, đảm bảo click nhảy đến đúng section. |
| Đồng bộ mục lục | Khi user sửa heading (H2/H3) → mục lục tự động cập nhật real-time hoặc khi load lại trang. |
| Sửa FAQ | Đảm bảo phần FAQ luôn render cả câu hỏi lẫn câu trả lời từ dữ liệu AI. |
| Thêm auto-save | Bổ sung tính năng tự động lưu nháp (interval hoặc on-change) trong giao diện chỉnh sửa nội dung. |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Format bold/italic hiển thị nhất quán trong nội dung bài viết. |
| AC-02 | Toolbar editor có option "Văn bản bình thường" (paragraph format). |
| AC-03 | Click vào H3 trong mục lục → scroll đến đúng section H3 tương ứng. |
| AC-04 | Sửa heading trong bài → mục lục cập nhật đúng khi load lại hoặc real-time. |
| AC-05 | FAQ hiển thị đầy đủ câu hỏi + câu trả lời. |
| AC-06 | Hệ thống tự động lưu nháp bài viết trong quá trình chỉnh sửa. Có indicator cho user biết trạng thái lưu. |
