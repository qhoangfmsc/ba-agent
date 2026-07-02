---
task_id: TASK-049
title: "[Enhance] Heading dài cần thêm hình minh họa H3"
type: Enhance
priority: 🟡 Trung bình
module: Content > Ảnh
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Bạn Ngân
related_tasks: []
---

# [Enhance] Heading dài cần thêm hình minh họa H3

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **các heading có nội dung dài được tự động bổ sung hình minh họa cho vài H3**, Để **tránh tình trạng đoạn text quá dài không có hình, người đọc dễ chán**.

3. **Mô tả vấn đề**

Đối với các heading có nội dung quá dài, bài viết chỉ có text liên tục mà thiếu hình minh họa. Một đoạn text quá dài không có hình ảnh xen kẽ khiến người đọc dễ mệt mỏi và bounce rate cao. Cần thêm hình minh họa cho vài H3 trong các heading dài.

4. **Yêu cầu giải pháp**

Thêm logic detect heading dài (word count > threshold) và tự động suggest hoặc tạo hình minh họa cho một số H3 bên trong. Có thể dùng AI tạo ảnh minh họa hoặc suggest placeholder để người dùng tự thêm ảnh.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Heading có nội dung dài (> threshold) tự động có hình minh họa xen kẽ |
| AC-02     | Không có đoạn text quá dài (> 500 từ) liên tục mà không có hình ảnh |
