---
task_id: TASK-037
title: "[Bug] H2 gộp nhiều nội dung cần tách riêng"
type: Bug
priority: 🟠 Cao
module: Outline > Structure
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-028, TASK-035]
---

# [Bug] H2 gộp nhiều nội dung cần tách riêng

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **mỗi H2 chỉ focus vào một nội dung chính**, Để **bài viết có cấu trúc rõ ràng, mỗi phần tập trung vào một chủ đề**.

3. **Mô tả vấn đề**

Một số heading H2 gộp nhiều nội dung khác nhau vào cùng một heading. Ví dụ: "GEO SEO là gì? Định nghĩa, nguyên tắc và ứng dụng" — thực tế nên tách thành 3 H2 riêng biệt. Mỗi H2 cần focus vào một nội dung chính duy nhất.

4. **Yêu cầu giải pháp**

Cải thiện logic tạo heading: khi phát hiện H2 chứa nhiều concept (dấu hiệu: dùng "và", dấu phẩy liệt kê, nhiều keyword), tự động tách thành nhiều H2 riêng biệt. Mỗi H2 focus vào 1 concept chính.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Mỗi H2 trong outline chỉ focus vào 1 nội dung chính, không gộp nhiều concept |
| AC-02     | Heading chứa nhiều concept được tách thành nhiều H2 riêng biệt |
