---
task_id: TASK-036
title: "[Enhance] H3 liệt kê cần đánh số thứ tự"
type: Enhance
priority: 🟡 Trung bình
module: Outline > Format
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-028]
---

# [Enhance] H3 liệt kê cần đánh số thứ tự

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **các H3 dạng liệt kê (top phần mềm, các gói dịch vụ) được đánh số thứ tự**, Để **người đọc dễ quan sát và theo dõi danh sách**.

3. **Mô tả vấn đề**

Với các heading H2 dạng liệt kê (ví dụ: "Top 10 phần mềm...", "Các gói dịch vụ..."), các H3 bên dưới không được đánh số thứ tự. Người đọc khó biết đang xem item thứ mấy trong danh sách, đặc biệt khi bài viết dài và có nhiều item.

4. **Yêu cầu giải pháp**

Cập nhật logic tạo outline: khi H2 là dạng liệt kê (detect keyword "top", "các", "danh sách", "so sánh"), các H3 bên dưới tự động đánh số thứ tự (1., 2., 3...). Số thứ tự đặt ở đầu heading H3.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Các H3 dưới heading liệt kê được đánh số thứ tự (1., 2., 3...) |
| AC-02     | Chỉ áp dụng đánh số cho heading dạng liệt kê, không áp dụng cho heading thông thường |
