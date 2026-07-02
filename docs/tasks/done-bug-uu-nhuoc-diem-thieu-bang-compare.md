---
task_id: TASK-050
title: "[Bug] Ưu nhược điểm chưa triển khai bảng compare"
type: Bug
priority: 🟠 Cao
module: Content > Format
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-040, TASK-010]
---

# [Bug] Ưu nhược điểm chưa triển khai bảng compare

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **phần ưu nhược điểm được triển khai bằng bảng compare (pros/cons table)**, Để **người đọc dễ so sánh và bài viết trông chuyên nghiệp**.

3. **Mô tả vấn đề**

Phần ưu nhược điểm trong bài viết chưa được triển khai theo bảng compare. Hiện tại nội dung đang viết dạng text paragraph hoặc bullet list thay vì bảng so sánh hai cột (ưu điểm | nhược điểm). Bảng compare giúp người đọc dễ so sánh và tạo visual break trong bài viết.

4. **Yêu cầu giải pháp**

Cập nhật prompt viết content: khi gặp heading ưu nhược điểm, tự động triển khai bằng bảng compare hai cột. Đảm bảo bảng được render đúng format trên editor và khi import sang WordPress.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Phần ưu nhược điểm được triển khai bằng bảng compare hai cột |
| AC-02     | Bảng compare hiển thị đúng trên cả editor và WordPress |
