---
description: Tạo task BA hoàn chỉnh từ feedback/requirements. Core workflow của BA Agent.
---

# /viet-task — Tạo task BA từ feedback

## Khi nào dùng

User cung cấp feedback, yêu cầu, hoặc mô tả tính năng → Agent tạo task document hoàn chỉnh.

## Input

- **File .md**: path đến file trong `requirements/`
- **Google Docs URL**: link Google Docs chứa feedback
- **Text trực tiếp**: mô tả ngay trong chat
- **Confluence page_id**: page ID trên Confluence

## Workflow

### Bước 1: Chuẩn bị input

Tuỳ loại input, thực hiện **đúng 1 hành động**:

**Nếu input là file .md** → đọc file đó.

**Nếu input chứa Google Docs URL** → xử lý:

1. **Detect trùng doc_id**: Nếu có nhiều URLs, trích doc_id từ mỗi URL. Nếu nhiều URLs cùng doc_id (chỉ khác tab) → **chỉ fetch 1 lần** vì Google Docs API export toàn bộ document, không filter theo tab. Thông báo user.
2. Chạy script cho mỗi doc_id DUY NHẤT:
   ```bash
   .venv/bin/python3 scripts/fetch-gdocs-to-md.py "<URL>" requirements/<tên-file>.md
   ```
3. Đọc file output.

**Nếu input là Confluence page_id** → chạy script:

```bash
cd scripts && ../.venv/bin/python3 crawl_confluence/run.py <PAGE_ID>
```

Sau đó đọc file memory vừa tạo.

**Nếu input là text trực tiếp** → dùng luôn.

**Xử lý lỗi fetch**: Nếu script fail (exit code ≠ 0):

| Lỗi                    | Cách xử lý                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------ |
| Google Docs fetch fail | Thông báo user: kiểm tra URL, quyền truy cập. Đề xuất thử mở URL trong browser.      |
| Confluence script fail | Thông báo user: kiểm tra credentials, page_id.                                       |
| File output rỗng       | Thông báo user: export thành công nhưng nội dung rỗng. Kiểm tra document có content. |
| Lỗi khác               | Hiển thị error message cho user, KHÔNG tự sửa script.                                |

### Bước 2: Đọc memories

Đọc file `docs/memories/SUMMARY.md`.

- File này chứa tổng hợp tất cả memories (1 file duy nhất).
- Nếu chưa có SUMMARY.md → chạy:
  ```bash
  cd scripts && ../.venv/bin/python3 -c "from crawl_confluence.build_memory_index import build_summary; build_summary()"
  ```
- Dùng memories làm reference cho: **văn phong, cấu trúc document, User Story style, AC style**.
- **QUAN TRỌNG**: Format task phải bám sát style trong memories. Xem kỹ phần "Format task chuẩn" bên dưới.

### Bước 3: Phân tích & nhóm feedback

Từ nội dung đã chuẩn bị ở Bước 1:

1. Liệt kê tất cả issues/feedback riêng biệt theo các chủ đề
2. Nhóm theo chủ đề/module
3. Xác định loại (bug-fix / feature) và priority (🔴 Rất cao | 🟠 Cao | 🟡 Trung bình) cho mỗi nhóm

### Bước 4: Viết từng task

Với mỗi nhóm, tạo 1 file `docs/tasks/YYYY-MM-DD-<slug>.md`.
Tạo task cần độc lập và riêng biệt, KHÔNG dùng "và" hay "&" để gộp các task.

#### Format task chuẩn

**Nguyên tắc format — BẮT BUỘC tuân thủ:**

- **Title ngắn gọn** (3-6 từ): style giống memories (VD: "Quản lý bài viết", "Xuất bản", "Cấu hình viết bài"). KHÔNG viết câu mô tả dài. KHÔNG gộp các task vào cùng nhau bằng "và" hay "&".
- **Sections dùng numbered list** (`1.`, `2.`, `3.`...) — KHÔNG dùng `## 1.`, `## 2.`.
- **Sub-sections dùng bold** (`**6.1. Tên mục**`) — KHÔNG dùng `### 4.1.`.
- **Chỉ dùng H1 cho title, H2 không cần** — toàn bộ structure nằm trong numbered list.
- **Mô tả vấn đề**: dùng bảng `| **Vấn đề** | **Mô tả** |` — đồng nhất style memories.
- **Workflow/Yêu cầu**: dùng bảng — KHÔNG chia nhiều sub-section.
- **Tối đa 1 bảng yêu cầu + 1 bảng AC** — gộp hết vào, không tách.

```markdown
---
task_id: TASK-YYYY-MMDD-<số>
title: <Tiêu đề ngắn 3-6 từ>
type: <bug-fix | feature>
priority: <🔴 Rất cao | 🟠 Cao | 🟡 Trung bình>
module: Viết bài tự động > <Sub-module>
created_at: YYYY-MM-DD
source: <Nguồn feedback>
confluence_ref: <Page IDs liên quan từ memories>
---

# <Tiêu đề ngắn>

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | DD.MM.YYYY |

2. **User Story**

Là một **<role>**, Tôi muốn **<action>**, Để **<benefit>**.

3. **Mô tả vấn đề**

<Mô tả ngắn gọn bối cảnh chung trong 1-2 câu>

|                   |                     |
| ----------------- | ------------------- |
| **Vấn đề**        | **Mô tả**           |
| <Vấn đề cụ thể 1> | <Chi tiết vấn đề 1> |
| <Vấn đề cụ thể 2> | <Chi tiết vấn đề 2> |

4. **Yêu cầu chi tiết**

|             |              |
| ----------- | ------------ |
| **Yêu cầu** | **Mô tả**    |
| <Yêu cầu 1> | <Mô tả ngắn> |
| <Yêu cầu 2> | <Mô tả ngắn> |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01     | <Kết quả testable>   |
| AC-02     | <Kết quả testable>   |
```

**Quy tắc viết**:

- Tiếng Việt, technical terms giữ tiếng Anh
- Văn phong BA/PO chuyên nghiệp, ngắn gọn
- Không để trống section — thiếu info ghi `[Cần bổ sung]`
- Mỗi AC phải testable
- Vấn đề mô tả bằng bảng (`| Vấn đề | Mô tả |`), đồng nhất style memories
- Yêu cầu gộp 1 bảng duy nhất, KHÔNG chia sub-section

### Bước 5: Báo cáo

Hiển thị bảng:

```
| # | Task | Priority | Type | File |
```

Hỏi user có muốn chỉnh sửa không.

## Quy tắc

1. **Dùng script có sẵn** — `fetch-gdocs-to-md.py`, `crawl_confluence/run.py`. KHÔNG tự fetch/curl
2. **Đọc SUMMARY.md** — 1 file duy nhất, không đọc từng memory file
3. **Output ở local** — `docs/tasks/`, KHÔNG viết lên Confluence
4. **Thiếu thông tin** → ghi `[Cần bổ sung]`, không tự giả định
5. **Format bám sát memories** — style Confluence, KHÔNG tự chế format mới
6. **Google Docs cùng doc_id** — chỉ fetch 1 lần, dù nhiều URLs khác tab
7. **Script fail → thông báo user** — KHÔNG tự retry, KHÔNG sửa script
