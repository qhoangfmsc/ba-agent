---
task_id: TASK-040
title: "[Bug] Heading ưu nhược điểm không cần tách H3"
type: Bug
priority: 🟡 Trung bình
module: Outline > Structure
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-028, TASK-039, TASK-050]
---

# [Bug] Heading ưu nhược điểm không cần tách H3

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **heading ưu nhược điểm không bị chia ra 2 H3**, Để **phần này được viết bằng bảng compare gọn gàng**.

3. **Mô tả vấn đề**

Heading ưu nhược điểm đang bị tách thành 2 H3 riêng biệt ("Ưu điểm", "Nhược điểm"), trong khi phần này nên viết bằng bảng compare (pros/cons table) dưới 1 H2 duy nhất. Việc tách H3 khiến format không phù hợp với bảng compare.

4. **Yêu cầu giải pháp**

Cập nhật rule outline: heading ưu nhược điểm (chứa "ưu điểm", "nhược điểm", "pros", "cons") chỉ làm 1 H2, triển khai bằng bảng compare, không tách H3.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Heading ưu nhược điểm chỉ có 1 H2, không tách 2 H3 |
| AC-02     | Nội dung ưu nhược điểm được triển khai bằng bảng compare |
