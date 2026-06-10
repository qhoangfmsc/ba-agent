---
name: crawl-confluence
description: Crawl nội dung từ Confluence về lưu vào docs/memories/ làm reference cho viết task.
---

# /crawl-confluence — Crawl Confluence về làm memories

## Khi nào dùng

User muốn crawl Confluence pages về local. Output dùng làm reference cho `/viet-task`.

## Input

- **Page ID**: `124190721`
- **"folder"** hoặc **"--children"** = crawl parent + tất cả children
- **Page URL**: trích xuất page_id từ URL

## Workflow

### Bước 1: Parse input

- Lấy `page_id` từ input user (số hoặc trích từ URL Confluence)
- Validate: page_id phải là số. Nếu không phải → hỏi lại user.
- URL Confluence format: `https://<domain>/wiki/spaces/<SPACE>/pages/<PAGE_ID>/<title>` → lấy PAGE_ID
- Nếu user nói "folder", "--children", "tất cả" → thêm flag `--children`

### Bước 2: Chạy script crawl

```bash
cd scripts && ../.venv/bin/python3 crawl_confluence/run.py <PAGE_ID> [--children]
```

Script tự động xử lý toàn bộ:
- `fetch_confluence_pages.py` → fetch HTML từ Confluence REST API
- `convert_html_to_md.py` → convert HTML → Markdown (markitdown)
- `save_as_memory.py` → lưu thành `docs/memories/<page_id>-<slug>.md`
- `build_memory_index.py` → cập nhật INDEX.md + SUMMARY.md

### Bước 3: Xử lý lỗi

Nếu script exit code ≠ 0, đọc error output và xử lý:

| Lỗi | Cách xử lý |
| --- | --- |
| `401 Unauthorized` / credentials | Thông báo user: token Confluence hết hạn, cần cập nhật `.gemini/settings.json` |
| `404 Not Found` | Thông báo: page_id không tồn tại hoặc bị xóa. Hỏi lại page_id đúng. |
| `ConnectionError` / timeout | Thông báo: lỗi mạng. Đề xuất user thử lại. |
| Lỗi khác | Hiển thị error message cho user, KHÔNG tự sửa script. |

### Bước 4: Báo cáo kết quả

Đọc output của script và trình bày cho user:
- Số pages đã crawl
- Danh sách tên pages
- Lưu ý: nếu crawl lại cùng pages → file cũ bị ghi đè
- Gợi ý: "Dùng `/viet-task` để tạo task — agent sẽ tham chiếu memories này"

## Quy tắc

1. **KHÔNG tự viết script** — chỉ dùng `scripts/crawl_confluence/run.py` có sẵn
2. **KHÔNG dùng curl hay MCP** — script xử lý hết
3. **Confluence = READ-ONLY** — chỉ đọc, không tạo/sửa/xóa
4. **Script fail → thông báo user** — KHÔNG tự retry, KHÔNG sửa script
