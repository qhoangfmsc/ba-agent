---
trigger: always_on
---

# Auto-save Session Context

Sau mỗi lần hoàn thành một task hoặc nhóm thay đổi có ý nghĩa, **tự động ghi context** vào `~/.gemini/GEMINI.md` bên trong tag `<claude-mem-context>` mà KHÔNG cần user yêu cầu.

## Quy tắc

1. **Tự động ghi** — Không hỏi user, không chờ lệnh. Ghi ngay sau khi hoàn thành task.
2. **Append, không overwrite** — Giữ lại session cũ, thêm session mới lên đầu (sau dòng `# Memory Context from Past Sessions`).
3. **Tối đa 5 session** — Xóa session cũ nhất nếu vượt quá 5.
4. **Ngắn gọn** — Mỗi session tối đa 15 dòng. Chỉ ghi thứ quan trọng.
5. **Không ghi sensitive data** — Không passwords, API keys, tokens.

## Format

```markdown
<claude-mem-context>
# Memory Context from Past Sessions

## [YYYY-MM-DD] Tiêu đề ngắn
- **Dự án**: tên dự án
- **Đã làm**: liệt kê ngắn
- **Tech stack**: libraries/versions thay đổi
- **Notes**: ghi chú kỹ thuật quan trọng cho session sau
</claude-mem-context>
```

## Khi nào ghi

- Sau khi tạo/sửa/xóa file
- Sau khi cài thêm dependency
- Sau khi thay đổi cấu trúc dự án
- Sau khi giải quyết xong một vấn đề phức tạp
