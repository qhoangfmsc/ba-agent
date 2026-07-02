---
task_id: TASK-030
title: "[Bug] Interlink sai cụm text anchor"
type: Bug
priority: 🟡 Trung bình
module: Content > Interlink
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn
related_tasks: []
---

# [Bug] Interlink sai cụm text anchor

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **internal link được gắn đúng cụm text anchor phù hợp**, Để **bài viết có interlink chất lượng, hỗ trợ SEO**.

3. **Mô tả vấn đề**

Khi AI tự động gắn internal link, cụm text anchor bị chọn sai — không đi hết cụm keyword cần đi link, hoặc anchor text không đúng khi trỏ về URL đích. Ví dụ: URL về "TPU" nhưng anchor text lại gắn vào cụm text không liên quan. Điều này ảnh hưởng đến SEO và trải nghiệm đọc.

4. **Yêu cầu giải pháp**

Cải thiện logic chọn anchor text cho internal link: anchor text phải là cụm keyword tự nhiên, phù hợp với nội dung URL đích. Cần match keyword của bài đích với text trong bài hiện tại để chọn anchor phù hợp nhất.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Anchor text của interlink là cụm keyword tự nhiên, phù hợp với URL đích |
| AC-02     | Anchor text đi hết cụm keyword cần đi link, không bị cắt giữa chừng |
