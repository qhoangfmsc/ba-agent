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

### Bước 3: Phân tích & tách từng issue

Từ nội dung đã chuẩn bị:

1. **Liệt kê tất cả issues riêng biệt** — mỗi vấn đề/feedback là 1 item độc lập.
2. **Gán prefix cho từng issue** theo bảng dưới:

| Prefix | Khi nào gán |
|---|---|
| `[Bug]` | Hệ thống hoạt động sai so với mong đợi, có lỗi cần sửa |
| `[Enhance]` | Tính năng đã có nhưng cần cải tiến, nâng cấp |
| `[Feature]` | Tính năng mới hoàn toàn chưa tồn tại |
| `[Hotfix]` | Bug nghiêm trọng, ảnh hưởng production, cần fix gấp |
| `[Refactor]` | Cần tái cấu trúc code, không thay đổi hành vi |

3. **Xác định priority** cho từng issue: 🔴 Rất cao | 🟠 Cao | 🟡 Trung bình
4. **Xác định module** cho từng issue

**Nguyên tắc tách:**
- KHÔNG gộp nhiều vấn đề vào 1 task. Mỗi dòng feedback mô tả 1 vấn đề riêng = 1 task riêng.
- Nếu 1 dòng feedback chứa nhiều vấn đề khác nhau (dùng "và", "&", liệt kê) → tách thành nhiều task.
- Các issue cùng nhóm liên kết qua trường `related_tasks`.

**Lưu ý multi-tab**: Nếu có nhiều tab (nhiều người feedback), phân tích TỪNG tab riêng. Cùng 1 vấn đề được nhiều người report → vẫn tạo 1 task, ghi tất cả người report vào `feedback_by`.

**Checkpoint — Hiển thị bảng tóm tắt trước khi tạo file:**

Sau khi phân tích xong, PHẢI hiển thị bảng tóm tắt tất cả issues cho user xem trước:

```
| # | Prefix | Title dự kiến | Priority | Module | Feedback by |
```

Kèm tổng số issues và thông báo: "Sẽ tạo N tasks trong X batch (mỗi batch 5 files). Bắt đầu batch 1..."

### Bước 4: Viết từng task (batch processing)

Với **mỗi issue**, tạo 1 file `docs/tasks/<prefix>-<slug>.md` (prefix = `bug`/`enhance`/`feature`/`hotfix`/`refactor`).

**Format**: tuân thủ rule `task-format.md` — xem `.agent/rules/task-format.md`.

**⚠️ Quy tắc batch processing (BẮT BUỘC):**

KHÔNG tạo tất cả files cùng lúc. Chia thành các batch nhỏ:

1. **Mỗi batch tối đa 5 files** — tạo song song 5 files trong 1 lượt.
2. **Báo cáo tiến trình sau mỗi batch** — hiển thị:
   ```
   ✅ Batch X xong: Y/Z tasks — TASK-AAA → TASK-BBB
   ```
3. **Tiếp tục batch tiếp theo ngay** — KHÔNG chờ user confirm giữa các batch.
4. **Nếu batch lỗi** → báo cáo files lỗi, tiếp tục batch tiếp theo với các files còn lại.

Ví dụ: 43 tasks → 9 batch (8 batch × 5 files + 1 batch × 3 files).

**Lưu ý quan trọng:**
- Title BẮT BUỘC có prefix: `[Bug]`, `[Enhance]`, `[Feature]`, `[Hotfix]`, hoặc `[Refactor]`.
- Section 3 (Mô tả vấn đề) và Section 4 (Yêu cầu giải pháp) viết **đoạn văn ngắn 2-4 câu**, KHÔNG dùng bảng.
- Tối đa 1-3 AC vì chỉ giải quyết 1 vấn đề.
- Điền `related_tasks` liên kết các task cùng nhóm feedback.

### Bước 5: Báo cáo

Hiển thị bảng:

```
| # | Task ID | Type | Title | Priority | Module | Feedback by | File |
```

Hỏi user có muốn chỉnh sửa không.

## Quy tắc

1. **Format tuân thủ rule** — `.agent/rules/task-format.md`. KHÔNG tự chế format mới.
2. **1 issue = 1 task** — KHÔNG gộp nhiều vấn đề vào 1 task.
3. **Prefix bắt buộc** — Title PHẢI bắt đầu bằng `[Bug]`, `[Enhance]`, `[Feature]`, `[Hotfix]`, hoặc `[Refactor]`.
4. **Dùng script có sẵn** — `fetch-gdocs-to-md.py`. KHÔNG tự fetch/curl.
5. **Output** — `docs/tasks/`, KHÔNG viết lên Confluence.
6. **Thiếu thông tin** → ghi `[Cần bổ sung]`, không tự giả định.
7. **Cùng doc_id, khác tab → fetch RIÊNG từng tab** — mỗi tab = 1 người feedback.
8. **Cùng doc_id, cùng tab → fetch 1 lần** — thông báo user.
9. **Script fail → thông báo user** — KHÔNG tự retry, KHÔNG sửa script.
10. **feedback_by bắt buộc** — tự extract từ mô tả URL nếu có, không thì hỏi user.
