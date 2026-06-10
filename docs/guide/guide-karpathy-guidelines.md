# Hướng dẫn Karpathy Coding Guidelines

> **Source**: [Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876) — co-founder OpenAI, ex-Tesla AI Director
> **Adapted from**: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)

## Vấn đề Karpathy chỉ ra

Karpathy quan sát rằng LLM (AI agent) khi code hay mắc các lỗi sau:

> "Chúng tự giả định thay bạn rồi chạy theo mà không kiểm tra. Chúng không quản lý sự nhầm lẫn, không hỏi lại, không chỉ ra mâu thuẫn, không đưa ra tradeoffs."

> "Chúng rất thích overcomplicate code — phình abstractions, không dọn dead code... viết 1000 dòng khi 100 dòng là đủ."

> "Đôi khi chúng sửa/xóa comments và code mà chúng không hiểu — dù không liên quan gì đến task."

## 4 Nguyên tắc

### 1. Think Before Coding — Nghĩ trước khi code

**Không giả định. Không giấu nhầm lẫn. Đưa ra tradeoffs.**

| LLM thường làm | Karpathy muốn |
|---|---|
| Tự chọn 1 cách hiểu rồi code luôn | Nêu rõ assumptions, hỏi nếu không chắc |
| Chọn giải pháp đầu tiên nghĩ ra | Đưa nhiều options, để user chọn |
| Ngại nói "tôi không biết" | Dừng lại, nói rõ chỗ nào confusing |

**Ví dụ thực tế**:

```
❌ "Tôi sẽ dùng Redux cho state management."

✅ "Có 3 cách tiếp cận:
   1. Redux — full-featured nhưng boilerplate nhiều
   2. Zustand — nhẹ hơn, đủ cho project nhỏ
   3. React Context — đơn giản nhất nhưng limited
   
   Bạn muốn dùng cách nào?"
```

### 2. Simplicity First — Đơn giản trước

**Code tối thiểu giải quyết vấn đề. Không code dự phòng.**

| Không nên | Nên |
|---|---|
| Thêm feature chưa ai yêu cầu | Chỉ code đúng thứ được hỏi |
| Tạo abstraction cho code dùng 1 lần | Viết trực tiếp |
| Thêm config cho "linh hoạt sau này" | Hardcode nếu chưa cần flexible |
| Handle lỗi không thể xảy ra | Chỉ handle lỗi thực tế |
| 200 dòng code | 50 dòng code (rewrite nếu cần) |

**Test đơn giản**: Hỏi "Senior engineer có nói cái này overcomplicated không?" — nếu có, simplify.

**Ví dụ thực tế**:

```typescript
// ❌ Overcomplicated — factory pattern cho 1 case
class NotificationFactory {
  create(type: string) {
    switch(type) {
      case 'email': return new EmailNotification();
      // chỉ có 1 case, nhưng "để sau mở rộng"
    }
  }
}

// ✅ Simple — giải quyết đúng vấn đề
function sendEmail(to: string, body: string) {
  await mailer.send({ to, body });
}
```

### 3. Surgical Changes — Thay đổi chính xác

**Chỉ sửa đúng chỗ cần sửa. Chỉ dọn mess do mình tạo.**

| Không nên | Nên |
|---|---|
| "Tiện tay" format lại code xung quanh | Chỉ sửa code liên quan đến task |
| Refactor code đang chạy tốt | Để yên, đề cập nếu muốn |
| Dùng coding style khác project | Match style hiện có |
| Xóa dead code sẵn có | Đề cập — không tự xóa |

**Khi code MỚI tạo orphans** (import/variable/function thừa do bạn sửa):
- ✅ Xóa — vì BẠN tạo ra
- ❌ Xóa dead code có từ trước — không phải việc của task

**Test đơn giản**: Mỗi dòng thay đổi trong diff phải trace về yêu cầu của user.

**Ví dụ thực tế**:

```diff
  // User yêu cầu: "đổi tên function getUserName thành getDisplayName"
  
  // ❌ Sửa thêm thứ không liên quan
- function getUserName(user: User) { // TODO: add cache
+ function getDisplayName(user: User) {
-   return user.name // this is a simple getter
+   return user.name; // Added semicolon for consistency
  }
- 
- // Xóa function cũ không ai dùng (có từ trước)
- function legacyGetUser() { ... }

  // ✅ Chỉ sửa đúng thứ được yêu cầu
- function getUserName(user: User) { // TODO: add cache
+ function getDisplayName(user: User) { // TODO: add cache
    return user.name // this is a simple getter
  }
```

### 4. Goal-Driven Execution — Thực thi hướng mục tiêu

**Định nghĩa tiêu chí thành công. Lặp cho đến khi verify.**

Chuyển task mơ hồ → goal cụ thể:

| Task mơ hồ | Goal cụ thể |
|---|---|
| "Thêm validation" | "Viết test cho invalid inputs, rồi make chúng pass" |
| "Fix bug" | "Viết test reproduce bug, rồi make nó pass" |
| "Refactor X" | "Đảm bảo tests pass trước và sau khi refactor" |

Với task nhiều bước, lập plan:
```
1. Tạo test file → verify: test fails đúng chỗ
2. Implement logic → verify: test passes
3. Clean up → verify: không break test khác
```

## Khi nào áp dụng, khi nào không

| Áp dụng nghiêm ngặt | Có thể nới lỏng |
|---|---|
| Code production | Prototype nhanh |
| Sửa code người khác | Dự án cá nhân |
| PR review / merge | Script 1 lần |
| API / interface design | Spike / exploration |

## Cách kiểm tra guidelines có hoạt động

✅ Guidelines **đang hoạt động** khi:
- Diffs gọn hơn — ít thay đổi thừa
- Ít phải rewrite vì overcomplicated
- Agent hỏi trước khi code — thay vì code sai rồi sửa

❌ Guidelines **chưa hoạt động** khi:
- Agent vẫn tự giả định và code luôn
- Code vẫn dài và phức tạp hơn cần thiết
- Diff chứa nhiều thay đổi không liên quan đến task

## Tham khảo

- Andrej Karpathy's post: https://x.com/karpathy/status/2015883857489522876
- GitHub repo: https://github.com/forrestchang/andrej-karpathy-skills
- File trong project: `.agent/rules/karpathy-guidelines.md`
