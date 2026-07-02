---
task_id: TASK-024
title: "[Bug] Outline thiếu bôi đậm và thừa ký tự"
type: Bug
priority: 🟡 Trung bình
module: Outline > Format
created_at: 2026-06-15
source: Feedback SEO Content (Google Docs) — Ngày 08/06/2026
feedback_by: Chị Túc Văn
related_tasks: [TASK-023]
---

# [Bug] Outline thiếu bôi đậm và thừa ký tự

1. **Lịch sử thay đổi**

|             |                |                       |            |
| ----------- | -------------- | --------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi** | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback   | 15.06.2026 |

2. **User Story**

Là một **Content Writer**, Tôi muốn **outline có format đúng chuẩn — bôi đậm đúng chỗ và không thừa ký tự đặc biệt**, Để **outline sạch sẽ, chuyên nghiệp và dùng được ngay**.

3. **Mô tả vấn đề**

Outline sinh ra bị thiếu bôi đậm phần tên thương hiệu Vietnix (theo rule phải bôi đậm), và có thừa ký tự "?" ở cuối heading không phải dạng câu hỏi. Các lỗi format nhỏ này ảnh hưởng đến chất lượng chuyên nghiệp của outline.

4. **Yêu cầu giải pháp**

Cập nhật prompt hoặc post-processing: đảm bảo tên thương hiệu Vietnix luôn được bôi đậm trong outline, và loại bỏ dấu "?" ở cuối heading không phải câu hỏi. Thêm rule validation cho format heading.

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | Tên Vietnix được bôi đậm trong outline theo rule |
| AC-02     | Không có dấu "?" thừa ở heading không phải câu hỏi |
