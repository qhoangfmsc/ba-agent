---
description: Tạo task BA từ feedback. Core workflow của BA Agent.
---

# /viet-task — Tạo task BA từ feedback

## Khi nào dùng

User cung cấp feedback, yêu cầu, hoặc mô tả vấn đề → Agent tạo task document hoàn chỉnh.

## Input

- **File .md**: path đến file trong `requirements/`
- **Google Docs URL**: link Google Docs chứa feedback
- **Text trực tiếp**: mô tả ngay trong chat

## Workflow

### Bước 1: Chuẩn bị input

Tuỳ loại input, thực hiện **đúng 1 hành động**:

**Nếu input là file .md** → đọc file đó.

- Nếu file chứa **Google Docs URLs** → chuyển sang xử lý Google Docs bên dưới.
- Nếu file chứa text feedback trực tiếp → dùng luôn.

**Nếu input chứa Google Docs URL** → xử lý:

1. **Xử lý tab**: Mỗi URL có thể chứa `?tab=t.xxx`. Export API **hỗ trợ export theo tab** — mỗi tab trả về nội dung riêng.
2. **Cùng doc_id, khác tab = fetch RIÊNG từng tab**:
   - Mỗi tab thường là feedback của 1 người khác nhau.
   - KHÔNG gộp fetch — mỗi URL fetch 1 lần, xuất ra file riêng.
   - Tên file output nên chứa tên người feedback nếu biết (VD: `feedback-chi-Lien.md`).
3. **Cùng doc_id, cùng tab (hoặc không có tab) → fetch 1 lần**. Thông báo user.
4. Chạy script cho mỗi URL (output vào file tạm `.agent/tmp/`):
   ```bash
   .venv/bin/python3 scripts/fetch-gdocs-to-md.py "<URL>" .agent/tmp/<tên-file>.md
   ```
5. Đọc file output → **xóa file tạm** sau khi đọc xong.

**Nếu input là text trực tiếp** → dùng luôn.

**Xử lý lỗi fetch**: Nếu script fail (exit code ≠ 0):

| Lỗi                    | Cách xử lý                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| Google Docs fetch fail | Thông báo user: kiểm tra URL, quyền truy cập.                              |
| File output rỗng       | Thông báo user: export thành công nhưng nội dung rỗng.                     |
| Lỗi khác               | Hiển thị error message cho user, KHÔNG tự sửa script.                      |

### Bước 2: Xác nhận nguồn feedback

Trước khi phân tích, xác nhận `feedback_by`:

- Nếu file input ghi rõ tên người kèm URL (VD: "Link feedback **chị Liên**: URL") → dùng tên đó luôn, KHÔNG hỏi lại.
- Nếu nội dung feedback ghi rõ người report → dùng luôn.
- Nếu không rõ ai feedback → hỏi user.

### Bước 3: Phân tích & nhóm feedback

Từ nội dung đã chuẩn bị:

1. Liệt kê tất cả issues/feedback riêng biệt
2. Nhóm theo chủ đề/module
3. Xác định loại (bug-fix / feature) và priority (🔴 Rất cao | 🟠 Cao | 🟡 Trung bình)

**Lưu ý multi-tab**: Nếu có nhiều tab (nhiều người feedback), phân tích TỪNG tab riêng. Feedback cùng chủ đề từ nhiều người có thể gộp vào 1 task nhưng phải ghi rõ nguồn từng issue.

### Bước 4: Viết từng task

Với mỗi nhóm, tạo 1 file `docs/tasks/YYYY-MM-DD-<slug>.md`.

**Format**: tuân thủ rule `task-format.md` — xem `.agent/rules/task-format.md`.

### Bước 5: Báo cáo

Hiển thị bảng:

```
| # | Task | Priority | Type | Feedback by | File |
```

Hỏi user có muốn chỉnh sửa không.

## Quy tắc

1. **Format tuân thủ rule** — `.agent/rules/task-format.md`. KHÔNG tự chế format mới.
2. **Dùng script có sẵn** — `fetch-gdocs-to-md.py`. KHÔNG tự fetch/curl.
3. **Output** — `docs/tasks/`, KHÔNG viết lên Confluence.
4. **Thiếu thông tin** → ghi `[Cần bổ sung]`, không tự giả định.
5. **Cùng doc_id, khác tab → fetch RIÊNG từng tab** — mỗi tab = 1 người feedback.
6. **Cùng doc_id, cùng tab → fetch 1 lần** — thông báo user.
7. **Script fail → thông báo user** — KHÔNG tự retry, KHÔNG sửa script.
8. **feedback_by bắt buộc** — tự extract từ mô tả URL nếu có, không thì hỏi user.

