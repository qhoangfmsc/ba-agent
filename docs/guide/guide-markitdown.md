# Hướng dẫn sử dụng markitdown-ts

> **markitdown-ts** là bản TypeScript của [Microsoft MarkItDown](https://github.com/microsoft/markitdown) — convert file tài liệu sang Markdown.

## Trong BA Agent

Agent sử dụng markitdown-ts khi cần convert file tài liệu (PDF, DOCX, XLSX...) sang Markdown để phân tích. Đây là skill tự động — agent sẽ tự convert khi gặp file non-text.

Skill file: `.agent/skills/convert-document-to-markdown.md`

## Định dạng hỗ trợ

| Định dạng | Extension | Ghi chú |
|-----------|-----------|---------| 
| PDF | `.pdf` | Trích xuất text từ PDF |
| Word | `.docx` | Microsoft Word documents |
| Excel | `.xlsx` | Chuyển bảng → Markdown table |
| PowerPoint | `.pptx` | Trích xuất text từ slides |
| HTML | `.html`, `.htm` | Convert HTML → Markdown |
| CSV | `.csv` | Chuyển thành Markdown table |
| XML | `.xml` | Parse và format lại |
| JSON | `.json` | Format readable |
| Rich Text | `.rtf` | Convert RTF → Markdown |
| Plain Text | `.txt` | Giữ nguyên nội dung |

## Tham khảo

- GitHub: https://github.com/nicobailon/markitdown-ts
- Original (Python): https://github.com/microsoft/markitdown
