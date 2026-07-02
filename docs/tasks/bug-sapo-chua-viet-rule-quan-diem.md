---
task_id: TASK-043
title: "[Bug] Sapo chưa viết theo rule quan điểm cá nhân"
type: Bug
priority: 🟡 Trung bình
module: Content > Rule
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: [TASK-032, TASK-052, TASK-053]
---

# [Bug] Sapo chưa viết theo rule quan điểm cá nhân

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **sapo bài viết được viết theo rule quan điểm cá nhân**, Để **bài viết có tính cá nhân hóa, không bị AI-like**.

3. **Mô tả vấn đề**

Sapo (đoạn mở đầu) bài viết chưa được viết theo rule quan điểm cá nhân theo tài liệu hướng dẫn. Rule yêu cầu sapo phải thể hiện góc nhìn/trải nghiệm cá nhân của tác giả, nhưng hiện tại sapo đang viết theo kiểu generic, thiếu tính cá nhân.

4. **Yêu cầu giải pháp**

Cập nhật prompt viết sapo: tham khảo rule quan điểm cá nhân trong tài liệu hướng dẫn và đảm bảo sapo thể hiện góc nhìn cá nhân, trải nghiệm, hoặc nhận định của tác giả. Mỗi sapo cần unique, không dùng template cứng.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Sapo bài viết thể hiện quan điểm/trải nghiệm cá nhân theo rule |
| AC-02     | Sapo không viết theo kiểu generic/template AI |
