---
task_id: TASK-056
title: "[Enhance] Import WP hỗ trợ import thẳng draft site chính"
type: Enhance
priority: 🟠 Cao
module: Import WP > Flow
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Liên
related_tasks: []
---

# [Enhance] Import WP hỗ trợ import thẳng draft site chính

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **import bài viết thẳng từ tool sang draft site chính (production)**, Để **giảm bớt thao tác phải import qua staging rồi publish lên site chính**.

3. **Mô tả vấn đề**

Hiện tại bài viết được import sang môi trường staging (stag.vietnix.dev), sau đó cần thực hiện thêm bước publish từ staging lên site chính. Quy trình này có nhiều thao tác và chưa có hướng dẫn rõ ràng cách publish từ staging lên site chính. Cần xem xét import thẳng vào draft site chính để giảm bước.

4. **Yêu cầu giải pháp**

Bổ sung tùy chọn import trực tiếp vào draft trên site chính (vietnix.vn) bên cạnh tùy chọn import staging hiện tại. Bài viết import vào site chính ở trạng thái Draft để vẫn cần review trước khi publish. Hoặc ít nhất cung cấp hướng dẫn cách publish bài từ staging lên site chính.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Có tùy chọn import trực tiếp vào draft site chính hoặc có hướng dẫn publish từ staging |
| AC-02     | Bài import vào site chính ở trạng thái Draft (chưa public) |
