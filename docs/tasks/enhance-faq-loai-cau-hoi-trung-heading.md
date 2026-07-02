---
task_id: TASK-033
title: "[Enhance] FAQ loại câu hỏi trùng heading"
type: Enhance
priority: 🟠 Cao
module: Outline > FAQ
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-008]
---

# [Enhance] FAQ loại câu hỏi trùng heading

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **phần FAQ không chứa câu hỏi trùng nội dung với heading bên trên**, Để **FAQ bổ sung thông tin mới, không lặp lại nội dung đã có trong bài**.

3. **Mô tả vấn đề**

Ở bước tạo outline, phần FAQ chứa những câu hỏi có nội dung trùng với các heading trong bài viết. Ví dụ heading đã có "X là gì?" nhưng FAQ lại có câu hỏi "X là gì?". Điều này tạo nội dung trùng lặp, không bổ sung giá trị mới cho bài viết.

4. **Yêu cầu giải pháp**

Thêm bước kiểm tra sau khi tạo FAQ: so sánh nội dung câu hỏi FAQ với danh sách heading trong outline. Nếu câu hỏi FAQ trùng hoặc tương tự heading đã có → loại bỏ câu hỏi đó và thay bằng câu hỏi mới.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Không có câu hỏi FAQ nào trùng nội dung với heading trong bài viết |
| AC-02     | FAQ bổ sung thông tin mới, không lặp lại nội dung heading |
