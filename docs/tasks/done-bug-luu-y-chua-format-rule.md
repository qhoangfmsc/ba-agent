---
task_id: TASK-053
title: "[Bug] Lưu ý chưa format theo rule"
type: Bug
priority: 🟡 Trung bình
module: Content > Rule
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-052, TASK-043, TASK-032]
---

# [Bug] Lưu ý chưa format theo rule

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **phần lưu ý trong bài viết được format đúng theo rule**, Để **người đọc dễ nhận ra các thông tin quan trọng cần chú ý**.

3. **Mô tả vấn đề**

Phần lưu ý (note/warning) trong bài viết chưa được format theo rule viết content. Lưu ý cần có format riêng biệt (box, icon cảnh báo, màu sắc khác biệt) để nổi bật so với nội dung chính, nhưng hiện tại đang viết như text bình thường.

4. **Yêu cầu giải pháp**

Cập nhật prompt viết content: khi có phần lưu ý, áp dụng đúng format theo rule (callout box, warning box). Đảm bảo AI nhận diện đúng đoạn nào là lưu ý để áp dụng format phù hợp.

5. **Acceptance Criteria**

|           |                                                                            |
| --------- | -------------------------------------------------------------------------- |
| **AC ID** | **Kết quả mong đợi**                                                       |
| AC-01     | Phần lưu ý trong bài viết được format đúng theo rule (callout/warning box) |
| AC-02     | Format lưu ý đồng nhất giữa các bài viết                                   |
