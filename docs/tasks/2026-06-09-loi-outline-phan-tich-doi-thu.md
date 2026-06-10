---
task_id: TASK-2026-0609-1
title: Lỗi outline & phân tích đối thủ
type: bug-fix
priority: 🔴
module: Viết bài tự động > Tạo Outline
created_at: 2026-06-09
source: Feedback SEO Content (chị Liên, chị Túc Văn, bạn Ngân) — 08.06.2026
confluence_ref: 159187456, 159187337
---

# Lỗi outline & phân tích đối thủ

1. **Lịch sử thay đổi**

|             |                |                         |            |
| ----------- | -------------- | ----------------------- | ---------- |
| **Version** | **Created by** | **Nội dung thay đổi**   | **Ngày**   |
| v1.0        | BA Agent       | Tạo mới từ feedback SEO | 09.06.2026 |

2. **User Story**

Là một **thành viên Marketing**, Tôi muốn **hệ thống phân tích đúng và đầy đủ heading đối thủ, đồng thời loại trừ nguồn không phù hợp khi tạo outline**, Để **outline gợi ý chính xác, chất lượng và không bị ảnh hưởng bởi dữ liệu nhiễu**.

3. **Mô tả vấn đề**

Khi phân tích đối thủ để tạo outline, hệ thống crawl sai/thiếu heading và không lọc nguồn tham khảo không phù hợp.

|  |  |
| --- | --- |
| **Vấn đề** | **Mô tả** |
| Crawl sai/thiếu heading đối thủ | Phần tham khảo đối thủ crawl sai hoặc thiếu các heading trong bài viết. VD: bài `vieclam24h.vn/nghe-nghiep/tram-sac-ky-nang/lovable-la-gi` bị thiếu heading, trong khi dùng SEOquake vẫn ra đủ. |
| Không loại trừ web từ điển | Phần tạo outline cần loại trừ các website từ điển (không phải bài viết SEO) khỏi danh sách đối thủ phân tích, vì nội dung từ điển không phù hợp làm tham chiếu outline. |

4. **Yêu cầu chi tiết**

|              |              |
| ------------ | ------------ |
| **Yêu cầu** | **Mô tả** |
| Sửa crawl heading | Rà soát logic trích xuất heading (H1, H2, H3) từ URL đối thủ. Đảm bảo kết quả trùng khớp với các tool chuẩn (SEOquake, Screaming Frog). |
| Loại trừ web từ điển | Thêm cơ chế lọc/loại trừ các URL thuộc nhóm web từ điển (VD: wiktionary, dictionary.com, vi.wikipedia.org...) khỏi danh sách 15 bài TOP. |
| Fallback khi crawl fail | Nếu không crawl được heading từ 1 URL → bỏ qua URL đó và lấy URL tiếp theo trong SERP để đảm bảo đủ số lượng bài tham khảo. |

5. **Acceptance Criteria**

|           |                      |
| --------- | -------------------- |
| **AC ID** | **Kết quả mong đợi** |
| AC-01 | Hệ thống trích xuất đúng và đầy đủ H1/H2/H3 từ bài đối thủ (so sánh với SEOquake cho cùng URL). |
| AC-02 | Các URL thuộc nhóm web từ điển bị loại khỏi danh sách 15 bài TOP phân tích. |
| AC-03 | Nếu 1 URL crawl fail hoặc bị loại → hệ thống tự động lấy URL tiếp theo trong SERP. |
| AC-04 | Outline gợi ý từ AI phản ánh đúng cấu trúc heading đã trích xuất. |
