---
task_id: TASK-002
title: "[Enhance] Loại trừ web từ điển khi tạo outline"
type: Enhance
priority: 🟠 Cao
module: Outline > Crawl
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: [TASK-003]
---

# [Enhance] Loại trừ web từ điển khi tạo outline

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **phần tạo outline tự động loại trừ các website từ điển khỏi danh sách đối thủ**, Để **outline chỉ tham khảo từ các bài viết chất lượng, đúng intent**.

3. **Mô tả vấn đề**

Khi tool crawl đối thủ để tạo outline, các website từ điển (dictionary sites) cũng được crawl và sử dụng làm nguồn tham khảo. Các trang này thường có cấu trúc heading khác biệt hoàn toàn so với bài viết SEO, dẫn đến outline sinh ra không phù hợp với intent của keyword.

4. **Yêu cầu giải pháp**

Thêm danh sách blacklist các domain từ điển phổ biến (như dictionary.cambridge.org, oxfordlearnersdictionaries.com, vi.wiktionary.org...) vào bước crawl đối thủ. Khi gặp URL thuộc blacklist, tool tự động bỏ qua và không đưa vào nguồn tham khảo cho outline.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Các website từ điển không xuất hiện trong danh sách đối thủ tham khảo khi tạo outline |
| AC-02     | Outline sinh ra chỉ dựa trên các bài viết SEO thực tế của đối thủ |
