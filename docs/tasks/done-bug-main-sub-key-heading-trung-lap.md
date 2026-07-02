---
task_id: TASK-035
title: "[Bug] Main key và sub key sinh heading trùng lặp"
type: Bug
priority: 🟠 Cao
module: Outline > Structure
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-028, TASK-037]
---

# [Bug] Main key và sub key sinh heading trùng lặp

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline không sinh ra các heading trùng lặp nội dung từ main keyword và sub keywords**, Để **bài viết có cấu trúc rõ ràng, không lặp**.

3. **Mô tả vấn đề**

Tool đang nhận định main keyword và sub keywords là hai vấn đề khác nhau, dẫn đến sinh ra 2 heading có nội dung trùng lặp nhau. Ví dụ: "GEO SEO là gì?" và "Generative Engine Optimization là gì?" — thực chất là cùng một khái niệm. Điều này tạo bài viết bị lặp nội dung.

4. **Yêu cầu giải pháp**

Cải thiện logic phân tích keyword: nhận diện main key và sub key là cùng một concept (synonym, viết tắt, mở rộng) thì gộp thành 1 heading duy nhất. Có thể dùng semantic similarity để detect trùng lặp.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Không có 2 heading trùng lặp nội dung từ main key và sub key trong cùng một outline |
| AC-02     | Main key và sub key cùng concept được gộp thành 1 heading |
