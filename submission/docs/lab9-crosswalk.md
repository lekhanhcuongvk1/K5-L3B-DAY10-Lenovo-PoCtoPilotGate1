# Đối chiếu Lab 9 → Lab 10 · Trần Quang Minh

Nguồn là bài Day9 của Trần Quang Minh (2A202603929), thư mục `K5-L3B-DAY09-TranQuangMinh-2A202603929-EvaluationandFailureAnalysis/docs`. Hai bản nguồn được giữ nguyên trong [PRD v1.1](lab9/PRD_v1.1.md) và [eval card](lab9/eval_card.md) để người chấm có thể kiểm tra độc lập với thư mục Day9 trên máy.

| Nội dung | Bằng chứng Day9 | Áp dụng khi xét Gate 1 ở Lab10 |
|---|---|---|
| Phạm vi | Một claim cho một đơn; ngoài phạm vi có thanh toán và rollout người dùng thật | Kết quả Lab10 là mô phỏng; coverage 100% của bộ test không phải phê duyệt triển khai thật |
| Độ đúng và độ ổn định | Core: pass_rate ≥0,85 và pass_5 ≥0,8; Advanced v2: pass_hat_5 blocking ≥0,85 | Lab10 đã ký pass_rate ≥0,99 và pass_k ≥0,98. Đây là yêu cầu của nhóm cho Gate 1 trên bộ Lab10, không phải ngưỡng hoặc kết quả kế thừa từ Day9; không sửa tiêu chí đã ký |
| Sự thật và quyền ghi tiền | FM-03 ticket_trust; approval_bypass=0; chấm tiền bằng code | Kiểm DB/policy/approval trước ghi; lời khai không được thay tracking. Lab10 còn xét lỗi hãng oan và PII bằng 0 |
| Lỗi chưa làm tiền rời hệ thống | proposal_amount_correct phát hiện đề xuất sai dù host chặn; FM-08 kiểm reply sai khi ledger đúng | Không coi chỉ ledger sạch là đủ. Cần kiểm kết luận từ chối/hoàn và nội dung reply, liên hệ ca S1-07 trong phân tích sự cố |
| Chi phí | cost_per_success và max_increase 0,1 so với baseline của Day9 | Lab10 tính chi phí mỗi ticket gồm trợ lý, duyệt và trực, kèm ROI. Khác mẫu số và khoản mục nên không so trực tiếp số tiền của hai lab |
| Phân khúc | slice_regression bị chặn vì money_movement dù pass_rate tổng còn trên sàn | Xem riêng kho CT: after 7.053đ/ticket; kiểm kịch bản công đối soát ở C5, tránh để trung bình toàn gói che phân khúc kém hiệu quả |
| Giới hạn | MockLLM, mẫu nhỏ, chưa có pilot thật; CI GitHub/merge chỉ xác nhận khi thực sự chạy | PASS-VISIBLE chưa chứng minh test ẩn, nguồn tracking thật, năng lực ACK hay chi phí held thực tế |

Đề xuất giữ **Cải tiến thêm**: phần mô phỏng đạt nhưng cần đo công held theo kho, khả năng nhận việc và lịch sử lỗi hãng 7 ngày. PRD/eval card đã có để đối chiếu; cả nhóm vẫn cần xác nhận lựa chọn chúng làm bản chung. Việc này không xác nhận thủ tục snapshot trước nhận thẻ đã được Coach chấp thuận.

Codex hỗ trợ đọc hai tài liệu nguồn, lập bảng đối chiếu và cập nhật hồ sơ theo yêu cầu của Minh. Không nhận là đã chạy lại Lab9 hoặc đã được giảng viên phê duyệt.
