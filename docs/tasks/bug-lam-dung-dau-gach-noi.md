---
task_id: TASK-054
title: "[Bug] Lạm dụng dấu gạch nối viết câu thành đoạn"
type: Bug
priority: 🟡 Trung bình
module: Content > Format
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-051]
---

# [Bug] Lạm dụng dấu gạch nối viết câu thành đoạn

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **bài viết không sử dụng quá nhiều dấu gạch nối và viết đoạn văn hoàn chỉnh**, Để **bài viết đọc tự nhiên, không bị AI-like**.

3. **Mô tả vấn đề**

Bài viết đang sử dụng quá nhiều dấu gạch nối (dash/hyphen), viết mỗi ý thành một dòng ngắn thay vì viết thành đoạn văn hoàn chỉnh. Cách viết này rất AI-like và không tự nhiên. Cần fix hình thức viết một câu thành một đoạn liền mạch.

4. **Yêu cầu giải pháp**

Cập nhật prompt viết content: yêu cầu AI viết thành đoạn văn hoàn chỉnh, hạn chế sử dụng dấu gạch nối để liệt kê. Mỗi đoạn nên là 2-4 câu liền mạch, không phải bullet list ngắn.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Bài viết không lạm dụng dấu gạch nối, viết thành đoạn văn hoàn chỉnh |
| AC-02     | Mỗi đoạn có ít nhất 2 câu liền mạch, không viết 1 câu 1 dòng |
