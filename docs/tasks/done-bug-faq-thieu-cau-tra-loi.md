---
task_id: TASK-008
title: "[Bug] FAQ có câu hỏi nhưng thiếu câu trả lời"
type: Bug
priority: 🟠 Cao
module: Content > FAQ
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên, Bạn Ngân
related_tasks: [TASK-033]
---

# [Bug] FAQ có câu hỏi nhưng thiếu câu trả lời

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **phần FAQ hiển thị đầy đủ cả câu hỏi và câu trả lời**, Để **bài viết hoàn chỉnh và hỗ trợ SEO schema FAQ**.

3. **Mô tả vấn đề**

Phần FAQ trong bài viết bị lỗi: có câu hỏi nhưng không có câu trả lời tương ứng. Lỗi này xuất hiện cả trên editor lẫn sau khi import sang WordPress. Điều này ảnh hưởng trực tiếp đến chất lượng bài viết và schema FAQ cho SEO.

4. **Yêu cầu giải pháp**

Kiểm tra lại logic sinh nội dung FAQ từ AI, đảm bảo mỗi câu hỏi luôn có câu trả lời đi kèm. Nếu AI không sinh được câu trả lời, cần hiển thị placeholder hoặc thông báo để người dùng bổ sung.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Mỗi câu hỏi trong FAQ luôn có câu trả lời đi kèm |
| AC-02     | Không xuất hiện trường hợp FAQ chỉ có question mà thiếu answer |
