---
task_id: TASK-017
title: "[Bug] Tự động gắn link sai cho text dạng abc.md"
type: Bug
priority: 🟡 Trung bình
module: Editor > Link
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-016]
---

# [Bug] Tự động gắn link sai cho text dạng abc.md

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **editor không tự động gắn link cho các text bình thường**, Để **bài viết không bị thêm link sai ngoài ý muốn**.

3. **Mô tả vấn đề**

Editor đang tự động gắn hyperlink cho các text có dạng "abc.md" hoặc tương tự (chứa dấu chấm và extension). Người dùng không chủ đích tạo link nhưng editor tự nhận diện và convert thành link. Điều này tạo ra các link sai, ảnh hưởng đến nội dung bài viết.

4. **Yêu cầu giải pháp**

Kiểm tra lại logic auto-link detection trong editor. Chỉ auto-link cho các URL hợp lệ (bắt đầu bằng http://, https://) chứ không auto-link cho các text chứa dấu chấm nhưng không phải URL. Tham khảo auto-link behavior của Google Docs.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Text dạng "abc.md" không bị tự động gắn link |
| AC-02     | Chỉ URL hợp lệ (http/https) mới được auto-link |
