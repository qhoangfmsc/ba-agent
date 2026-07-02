---
task_id: TASK-029
title: "[Bug] Outline thêm heading định nghĩa dư cho keyword hướng dẫn"
type: Bug
priority: 🟠 Cao
module: Outline > Intent
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn
related_tasks: [TASK-026]
---

# [Bug] Outline thêm heading định nghĩa dư cho keyword hướng dẫn

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline không thêm heading định nghĩa "X là gì" cho keyword dạng hướng dẫn khi site đã có bài định nghĩa**, Để **tránh trùng lặp nội dung nội bộ (keyword cannibalization)**.

3. **Mô tả vấn đề**

Với keyword dạng hướng dẫn (ví dụ: "gỡ cài đặt openclaw"), tool vẫn tự thêm heading định nghĩa "Openclaw là gì?" vào outline, trong khi site Vietnix đã có bài viết riêng về định nghĩa (vietnix.vn/openclaw-la-gi/). Bài hướng dẫn nên tập trung vào nội dung hướng dẫn, không cần nêu lại định nghĩa.

4. **Yêu cầu giải pháp**

Thêm logic kiểm tra intent keyword trước khi tạo outline: nếu keyword là dạng hướng dẫn (chứa "cách", "hướng dẫn", "gỡ cài đặt"...) và site đã có bài định nghĩa tương ứng, không thêm heading định nghĩa vào outline. Thay vào đó, đặt internal link về bài định nghĩa.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Keyword hướng dẫn không có heading định nghĩa dư trong outline khi site đã có bài định nghĩa |
| AC-02     | Outline tập trung đúng vào nội dung hướng dẫn của keyword |
