# Hướng dẫn sử dụng Claude-Mem

> **Claude-Mem** là hệ thống persistent memory cho AI agent — tự động lưu trữ và inject context giữa các session.

## Tổng quan

Claude-Mem hoạt động **hoàn toàn tự động**. Bạn không cần viết code gì — nó chạy qua hooks được cài vào Gemini CLI / Claude Code.

```
Session 1: Bạn làm việc → Claude-Mem ghi lại observations
                                    ↓
                            Lưu vào ~/.claude-mem/memory
                                    ↓
Session 2: Claude-Mem inject context → Agent "nhớ" dự án
```

## Cài đặt

Đã cài trong project:

```bash
# Cài cho Gemini CLI
npx claude-mem install --ide gemini-cli

# Hoặc cài cho Claude Code
npx claude-mem install
```

## Khởi động

```bash
# Khởi động worker service (chạy nền)
npx claude-mem start

# Dừng worker
npx claude-mem stop

# Kiểm tra trạng thái
npx claude-mem status
```

## Web Viewer

Sau khi start, mở browser tại:

```
http://localhost:37777
```

Tại đây bạn có thể:
- Xem **real-time memory stream** — mọi thứ agent đang làm
- Duyệt **observations** từ các session trước
- Xem **citations** với ID cụ thể

## Tìm kiếm trong memory

```bash
# Tìm kiếm semantic
npx claude-mem search "authentication flow"

# Xem observation cụ thể
# Truy cập: http://localhost:37777/api/observation/{id}
```

## File & thư mục quan trọng

```
~/.claude-mem/
├── memory/          # Toàn bộ memory data
├── config.json      # Cấu hình Claude-Mem
└── ...

~/.gemini/
├── settings.json    # Hooks đã được merge vào đây
└── GEMINI.md        # Context injection point
```

## Cách hoạt động chi tiết

### 1. Capture (tự động)

Khi agent làm việc, Claude-Mem capture các sự kiện:

| Event | Mô tả |
|-------|-------|
| `SessionStart` | Inject context từ session trước |
| `BeforeAgent` | Khởi tạo session |
| `AfterAgent` | Ghi observation sau khi agent phản hồi |
| `BeforeTool` | Ghi observation trước khi tool chạy |
| `AfterTool` | Ghi observation sau khi tool hoàn thành |
| `PreCompress` | Tóm tắt & nén memory |

### 2. Summarize (tự động)

Memory được nén bằng semantic summarization:
- Giữ lại **key decisions**, **code changes**, **architecture notes**
- Loại bỏ noise (repeated errors, trivial file reads)
- Progressive disclosure — inject context theo layers

### 3. Inject (tự động)

Khi bắt đầu session mới:
- Context từ session trước được inject vào `~/.gemini/GEMINI.md`
- Agent đọc file này và "nhớ" dự án

## Privacy

```xml
<!-- Dùng tag <private> để exclude nội dung khỏi memory -->
<private>
  API_KEY=sk-secret-key-123
  DATABASE_PASSWORD=mypassword
</private>
```

Bất kỳ nội dung nào trong tag `<private>` sẽ **không được lưu** vào memory.

## Cấu hình nâng cao

File `~/.claude-mem/config.json`:

```json
{
  "memoryPath": "~/.claude-mem/memory",
  "port": 37777,
  "contextInjection": {
    "enabled": true,
    "maxTokens": 4000
  }
}
```

## Troubleshooting

| Vấn đề | Giải pháp |
|--------|----------|
| Agent không "nhớ" session trước | Chạy `npx claude-mem start` và restart IDE |
| Web viewer không mở | Kiểm tra port 37777 có bị chiếm không |
| Memory quá lớn | Claude-Mem tự compress, hoặc xóa `~/.claude-mem/memory` |
| Hooks không hoạt động | Chạy `npx claude-mem install --ide gemini-cli` lại |

## Lệnh hay dùng

```bash
npx claude-mem install     # Cài đặt
npx claude-mem start       # Khởi động worker
npx claude-mem stop        # Dừng worker
npx claude-mem status      # Xem trạng thái
npx claude-mem search "x"  # Tìm kiếm trong memory
npx claude-mem reset       # Xóa toàn bộ memory (cẩn thận!)
```

## Tham khảo

- GitHub: https://github.com/thedotmack/claude-mem
- Docs: https://docs.claude-mem.ai/
- Installation: https://docs.claude-mem.ai/installation
- Search Tools: https://docs.claude-mem.ai/usage/search-tools
