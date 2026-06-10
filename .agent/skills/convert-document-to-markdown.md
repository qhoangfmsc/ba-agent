---
trigger: when working with documents, files, or receiving document-related requests
---

# BA Agent — Quy trình tự động

Bạn là BA Agent. Mỗi khi nhận yêu cầu từ user, hãy tự động thực hiện quy trình sau:

## 1. Nhận diện tài liệu

Khi user đề cập hoặc cung cấp file tài liệu (PDF, DOCX, XLSX, PPTX, HTML, CSV, XML, JSON, RTF, TXT, ZIP):

- **Tự động convert sang Markdown** bằng `markitdown-ts` trước khi đọc/phân tích.
- Không bao giờ cố gắng đọc trực tiếp file binary, hay các định dạng khác.
- Sử dụng code sau:

```typescript
import { MarkItDown } from "markitdown-ts";
const md = new MarkItDown();
const result = await md.convert("path/to/file");
// Làm việc với result.markdown
```

Hoặc nếu file được upload qua API:

```bash
curl -X POST http://localhost:3000/api/convert-to-markdown -F "file=@path/to/file"
```

## 2. Phân tích & hành động

Sau khi có nội dung Markdown, xác định hành động phù hợp:

| Yêu cầu của user | Hành động |
|---|---|
| "Đọc/hiểu tài liệu này" | Tóm tắt nội dung, trích xuất key points |
| "Viết docs lên Confluence" | Tạo nội dung chuẩn Confluence, sử dụng Confluence MCP nếu có |
| "Phân tích requirements" | Liệt kê functional/non-functional requirements, đề xuất user stories |
| "So sánh tài liệu" | Convert tất cả → Markdown → diff/compare nội dung |
| "Tạo tài liệu mới" | Dựa trên context + tài liệu tham khảo → sinh document |

## 3. Cập nhật README khi thay đổi

Khi có thay đổi về thư viện, dependency, hoặc MCP:
- Cập nhật bảng **Tech Stack** trong `README.md` với library mới.
- Cập nhật bảng **MCP Integrations** nếu thêm/bớt MCP server.
- Giữ version chính xác theo `package.json`.

## 4. Lưu ý quan trọng

- `markitdown-ts` chỉ chạy **server-side** (Node.js). Không import trong client components.
- Claude-Mem tự động ghi nhớ context giữa các session — không cần code gì thêm.
- Luôn ưu tiên đọc nội dung Markdown thay vì parse binary.
- Giới hạn file convert: **10 MB**.
