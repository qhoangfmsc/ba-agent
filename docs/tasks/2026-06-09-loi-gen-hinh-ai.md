---
task_id: TASK-2026-0609-5
title: Lỗi gen hình AI
type: bug-fix
priority: 🟠
module: Viết bài tự động > Viết nội dung
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159088986
---

# Lỗi gen hình AI

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **sử dụng tính năng tự tạo hình ảnh AI trong bài viết không bị lỗi**, Để **minh họa nội dung bài viết bằng hình ảnh phù hợp**.

3. **Mô tả vấn đề**

Tính năng gen hình AI trong editor bị lỗi khi sử dụng.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Gen hình AI lỗi | Sử dụng tính năng tự tạo ảnh AI trong editor gặp lỗi (không có thông tin chi tiết từ feedback — cần reproduce). |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Reproduce lỗi | Xác định chính xác lỗi khi gen hình AI: lỗi API call, lỗi render hình, hay lỗi insert vào editor. |
| Sửa gen hình | Đảm bảo flow gen hình hoạt động: nhập mô tả → AI tạo hình → hình hiển thị trong editor. |
| Error handling | Nếu gen hình fail → hiển thị thông báo lỗi rõ ràng cho user (không fail silent). |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Tính năng gen hình AI hoạt động: nhập mô tả → AI tạo hình → hình xuất hiện trong editor. |
| AC-02 | Nếu gen hình fail → hiển thị thông báo lỗi cụ thể (không blank/crash). |
| AC-03 | Hình gen xong có thể thay thế hoặc gen lại. |
