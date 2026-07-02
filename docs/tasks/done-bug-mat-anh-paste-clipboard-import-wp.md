---
task_id: TASK-013
title: "[Bug] Mất ảnh paste clipboard khi import WP"
type: Bug
priority: 🟡 Trung bình
module: Import WP > Ảnh
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-009, TASK-022]
---

# [Bug] Mất ảnh paste clipboard khi import WP

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **ảnh chèn bằng cách chụp màn hình và paste vào editor được giữ lại khi import sang WordPress**, Để **không phải upload lại ảnh thủ công**.

3. **Mô tả vấn đề**

Khi người dùng chụp màn hình rồi paste trực tiếp vào editor, ảnh hiển thị bình thường trên tool. Tuy nhiên khi import sang WordPress, các ảnh paste từ clipboard bị mất hoàn toàn. Chỉ ảnh upload qua tính năng "Chèn ảnh" mới được import thành công. Nguyên nhân có thể do ảnh paste được lưu dạng base64/blob và không được xử lý khi export.

4. **Yêu cầu giải pháp**

Khi import sang WordPress, cần detect và xử lý các ảnh dạng base64/blob (từ clipboard paste). Convert chúng thành file ảnh thực, upload lên WordPress Media Library, và thay thế reference trong nội dung bài viết.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Ảnh paste từ clipboard hiển thị đúng trên WordPress sau khi import |
| AC-02     | Ảnh được convert từ base64 thành file và upload vào Media Library |
