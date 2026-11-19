# Lenovo — Bàn giao vòng 1 trước thẻ sự cố

Đây là **bản lưu trạng thái vòng 1 trước nhận thẻ**, không phải trạng thái hiện tại. Sau đó nhóm đã xác nhận thẻ S1 và hoàn thiện vòng 2; xem final-handoff.md và Phiếu C. Thông tin thiếu thẻ bên dưới phản ánh đúng thời điểm vòng 1, không thay lịch sử bằng kết quả biết sau.

## Kết quả có thể tái kiểm

| Mục | Baseline | Prepared vòng 1 |
|---|---|---|
| Run ID | R-base-before-20261119-151011-bde05c | R-base-prepared-20261119-151711-260dc8 |
| Đúng | 109/110, pass^5=0,9545 | 110/110, pass^5=1,0 |
| Hoàn sai / lỗi hãng oan / PII | 20.000đ / 1 / 0 | 0đ / 0 / 0 |
| Chi phí / ROI | 4.203đ / 1,34 | 4.456đ / 1,24 |
| Ca ùn / coverage | 0 / 100% | 0 / 100% |

Public tests: 13/13 đạt. Hai adhoc khác đơn/lời khai ở B7.3 đều không tạo khoản hoàn/lỗi hãng khi tracking chưa đạt ngưỡng. Kho DN đắt nhất trong các kho định danh: 4.646đ/ticket; nhóm đơn không xác định kho (?) là 10.359đ/ticket và cần tuyến thủ công. Khoảng tin cậy [1;1] trên mock không chứng minh xác suất lỗi bằng 0 ngoài đời.

Guard G1: hiệu lực chính sách và tính nhất quán tracking. G2: quyền lợi/phê duyệt/sổ cái/trần trước ghi tiền. G3: đúng kiện/hãng và payload tối thiểu. Chỉ kiểm từ nguồn sự thật, không nhánh theo ticket ID/seed/nhãn/câu chữ. Giới hạn: DB vẫn có thể sai; kiểm sổ tuần tự không thay unique idempotency key và giao dịch nguyên tử trong hệ thống production.

Snapshot e0e28e3d đã niêm phong; không sửa guards_round1.py, operating_gates.round1.json hoặc round1.lock. Monitor mới sẽ xây theo sự cố được giao ở vòng 2; không coi escalation_rate có sẵn là đã làm xong yêu cầu monitor.

## Thủ tục cần Coach xác nhận

Tiêu chí được ký lúc 2026-11-19T15:05:24, hash 6903f01bf3853f2ee88234d6420105b047857b487fa9ecc9f38e3745929a9956. Commit gốc Sign acceptance criteria là 4b9d3708766e0de57f10378df4bf74ed49d24f8e, đã push trước baseline 15:10:11. Sau đó người dùng yêu cầu gỡ để tự commit; lịch sử nhánh hiện lưu tiêu chí ở 043e554 lúc 15:15:09, message LAB 10: cập nhật bài làm vòng 1. Do vậy máy check_submission không tìm được commit ký theo message bắt buộc. Không sửa timestamp, lock, journal, không backdate và không tạo giả bằng chứng trước đo. Cần trình bày sự việc với Coach để nhận quyết định xử lý; chất lượng kỹ thuật không bù điều kiện qua này.

V1: Cải tiến thêm, giữ ở PoC. Lý do: chưa có thẻ/kiểm độc lập, còn thủ tục ký và PRD/eval card Lab9 chưa xác nhận. Không mở pilot chỉ vì nền xanh. Xem B8 cho giả thuyết và hạn đánh giá lại 23/11/2026.

## Tự kiểm và commit

Chạy ở gốc repo PowerShell (python -X utf8 tránh lỗi mã hóa console):

```powershell
python -X utf8 -m unittest discover -s tests
python -X utf8 -m lab10.criteria verify
python -X utf8 -m lab10.checkpoint verify
python -X utf8 -m lab10.gate --run runs/R-base-prepared-20261119-151711-260dc8/report.json
```

Người dùng tự review và commit trên cuonglk. Không dùng git add .; chỉ stage file chủ động, giữ nguyên file khóa. Commit snapshot vòng1 và Phiếu B trước khi nhận thẻ. Chưa chạy grade vì chưa có đúng thẻ Coach giao.

Khi Coach phát thẻ, dùng đúng hướng dẫn incidents/README.md; chạy grade ngay sau nhận và trước sửa. Ghi đúng Thẻ đã bốc trong Phiếu C, đo base/prepared/after; sửa bản gốc guards/config, thêm monitor mới, điền C0–C12 và quyết định v2, gom lại đến ĐỦ THÀNH PHẦN. Không sửa bản snapshot để làm đẹp prepared. Sau cùng đưa bài về main và mỗi thành viên tự nộp link LMS theo yêu cầu lab.
