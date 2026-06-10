---
task_id: TASK-2026-0609-7
title: Cải tiến import flow
type: feature
priority: 🟡
module: Viết bài tự động > Xuất bản
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159187398, 159154697
---

# Cải tiến import flow

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **import bài viết thẳng lên draft site chính thay vì qua stag**, Để **giảm bớt thao tác thủ công và rút ngắn quy trình publish bài viết**.

3. **Mô tả vấn đề**

Hiện tại bài viết được import sang môi trường stag trước, sau đó cần thao tác thủ công để đưa lên site chính. Quy trình này tốn thời gian và chưa có hướng dẫn rõ ràng.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Import qua stag | Bài viết hiện import vào stag (`stag.vietnix.dev`), cần thêm bước thủ công để đưa lên site chính (`vietnix.vn`). |
| Thiếu hướng dẫn publish | Chưa có hướng dẫn cách publish bài từ stag lên site chính. User phải tự tìm cách. |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Import thẳng site chính | Cho phép user chọn import bài viết thẳng vào draft trên site chính (`vietnix.vn`) thay vì stag. |
| Giữ option stag | Vẫn giữ option import sang stag cho trường hợp cần review trước. User chọn site đích khi xuất bản. |
| Hướng dẫn flow | [Cần bổ sung] Nếu vẫn giữ flow qua stag → bổ sung hướng dẫn chi tiết cách publish từ stag lên site chính. |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | User có thể chọn site đích khi xuất bản: stag hoặc site chính. |
| AC-02 | Import thẳng draft site chính hoạt động (bài viết xuất hiện dạng Draft trên `vietnix.vn`). |
| AC-03 | Vẫn giữ option import sang stag cho review trước. |
| AC-04 | [Cần bổ sung] Nếu giữ flow stag → có tài liệu hướng dẫn publish từ stag lên site chính. |
