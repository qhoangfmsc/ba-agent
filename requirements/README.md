# Requirements

Folder này chứa các yêu cầu/feedback từ user viết bằng **ngôn ngữ tự nhiên**.

## Cách dùng

1. Tạo file `.md` mới trong folder này, đặt tên theo nội dung
2. Viết yêu cầu bằng ngôn ngữ bình thường — không cần format chuẩn
3. Chạy `/viet-task` và point đến file requirement
4. Agent sẽ đọc, phân tích, và tạo task chuyên nghiệp theo phong cách BA/PO

## Ví dụ

### File: `them-dark-mode.md`

```markdown
Trang dashboard hiện tại chỉ có giao diện sáng, nhiều user
phản hồi là dùng ban đêm bị chói mắt. Muốn thêm dark mode,
có toggle switch ở header để chuyển qua lại. Nhớ lưu preference
của user để lần sau vào không cần chọn lại.
```

### Sau khi chạy `/viet-task requirements/them-dark-mode.md`

Agent sẽ tạo task hoàn chỉnh tại `docs/tasks/` với:
- User Story chuẩn format
- Acceptance Criteria chi tiết
- Technical Notes
- Tham chiếu memories (nếu có docs liên quan đã crawl)
