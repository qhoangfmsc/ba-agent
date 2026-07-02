---
task_id: TASK-005
title: "[Bug] H3 mục lục không scroll tới nội dung"
type: Bug
priority: 🟡 Trung bình
module: Editor > Mục lục
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-007]
---

# [Bug] H3 mục lục không scroll tới nội dung

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **bấm vào H3 trong mục lục thì trang tự động scroll tới phần nội dung tương ứng**, Để **dễ dàng điều hướng trong bài viết dài**.

3. **Mô tả vấn đề**

Khi bấm vào các mục H3 trong mục lục (Table of Contents), trang không nhảy tới phần nội dung H3 tương ứng trong bài viết. Trong khi đó, bấm vào H2 thì scroll bình thường. Lỗi này khiến mục lục mất tác dụng điều hướng cho các heading cấp 3.

4. **Yêu cầu giải pháp**

Kiểm tra lại logic anchor link của mục lục, đảm bảo tất cả các cấp heading (H2, H3, H4...) đều có anchor ID đúng và scroll-to-element hoạt động chính xác khi click.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Bấm vào H3 trong mục lục, trang scroll tới đúng vị trí nội dung H3 tương ứng |
| AC-02     | Tất cả các cấp heading (H2, H3, H4) trong mục lục đều có chức năng scroll-to hoạt động |
