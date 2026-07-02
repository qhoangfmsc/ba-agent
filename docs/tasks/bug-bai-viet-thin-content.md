---
task_id: TASK-038
title: "[Bug] Bài viết thin content so với đối thủ"
type: Bug
priority: 🟠 Cao
module: Content > AI Writing
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-031, TASK-027]
---

# [Bug] Bài viết thin content so với đối thủ

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **bài viết AI sinh ra có đủ depth và chi tiết so với đối thủ**, Để **bài viết có thể cạnh tranh ranking trên SERP**.

3. **Mô tả vấn đề**

Bài viết hiện tại đang bị thin content — nội dung ngắn, thiếu nhiều ý so với đối thủ. Cấu trúc đoạn văn cũng cần chỉnh sửa: một đoạn cần có ít nhất 2 câu để đủ depth. Bài viết quá mỏng sẽ khó rank trên Google.

4. **Yêu cầu giải pháp**

Cải thiện prompt viết content: yêu cầu AI viết chi tiết hơn, mỗi đoạn ít nhất 2-3 câu. Tham khảo độ dài và depth của bài đối thủ để đặt yêu cầu word count phù hợp cho từng heading. Có thể thêm bước so sánh word count với đối thủ sau khi viết xong.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Mỗi đoạn văn có ít nhất 2 câu, không có đoạn chỉ 1 câu ngắn |
| AC-02     | Bài viết không bị thin content, có depth tương đương hoặc hơn đối thủ top 5 |
