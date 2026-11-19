# Lenovo — Hồ sơ S1 sau xử lý

**Cập nhật khôi phục lịch sử Git:** nhánh mới `cuonglk-restored-signing` kế thừa nguyên commit ký gốc `4b9d370` lúc 15:06:11 trước baseline 15:10:11. Kiểm lịch sử ký đã đạt; không ký lại, không backdate, không đổi file tiêu chí/lock hoặc snapshot. Nhánh `cuonglk` cũ được giữ để đối chiếu. Mục nói thiếu commit phía dưới ghi nhận tình trạng trước khôi phục; phần đó không còn là lỗi checker ở nhánh mới. Vẫn cần nhóm xác nhận thông tin thành viên và thủ tục snapshot trước nhận thẻ. Chưa commit/push phần bài làm trên nhánh khôi phục.

## Kết quả

Nguồn thẻ S1: https://github.com/minhhai203/K5_L3_Day10_PoC-to-Pilot_Gate1_cards/tree/main/incidents/S1 . Cả 4 file khớp SHA-256 trong MANIFEST của lab; thẻ, nhãn, dữ liệu và engine giữ nguyên.

Grade cuối: R-S1-grade-20261119-161212-5110cc — **PASS-VISIBLE**, test ẩn chưa có. Integrity, criteria, visible, regression, monitor đều đạt. Bộ nền110/110, S1 65/65, public13/13.

| Chỉ số S1 | base | prepared | after |
|---|---:|---:|---:|
| pass_rate / pass^5 | 0,3077 | 0,9231 | 1,0 |
| Hoàn sai (VND, tổng5 seed) | 985.000 | 0 | 0 |
| Lỗi hãng oan (tổng5 seed) | 30 | 0 | 0 |
| Chi phí/ticket (VND) | 2.964 | 6.616 | 5.870 |
| ROI | -2,74 | 0,51 | 0,70 |
| CT chi phí/ticket | 662 | 10.320 | 7.053 |
| Độ phủ | 100% | 100% | 100% |

Vòng1 đã chặn toàn bộ tác hại an toàn nhìn thấy trước biết thẻ. Vòng2 sửa kiểm cả kết luận âm và tách trần trách nhiệm hãng khỏi hoàn tiền đúng. Thêm4 monitor dựa trên telemetry không nhãn; không dùng ticket ID/seed/câu chữ để xử lý riêng. Snapshot e0e28e3d và tiêu chí6903f01b giữ nguyên.

## Quyết định và giới hạn

V1/v2 đều **Cải tiến thêm**, nhưng lý do khác: v1 thiếu kiểm thẻ; v2 đã đạt phần nhìn thấy, còn nguồn lỗi7ngày theo hợp đồng, task/ACK của2 ca held/ngày và công review này chưa nằm trong mô hình queue/TCO. NhánhCT có thể lại vượt làm tay nếu tính thêm công đối soát. Hạn tái quyết23/11/2026. Xem C9–C12 cho giả thuyết, người phụ trách, sensitivity và ba câu bắt buộc.

Hai vấn đề thủ tục **chưa được tự ý coi là đạt**: commit ký gốc đã bị yêu cầu gỡ rồi nhóm tự commit lại sau baseline; snapshot vòng1 chưa được nhóm commit/push trước khi nhận thẻ. Giữ nguyên lock/journal và mô tả trung thực A5/B8/C12, cần Coach xác nhận. Không backdate, amend giả lịch sử, đổi tiêu chí hoặc làm giả report để qua checker.

## Còn cần nhóm làm

1. Bổ sung họ tên/MSSV4 người và mục cá nhân trong TEAM.md; members trong submission.json phải khớp dạng HoVaTen-MSSV. Chỉ MSSV trưởng nhóm2A202603999 đã được cung cấp; không bịa danh tính/đóng góp.
2. Trình Coach vấn đề thủ tục ở trên và đối chiếu PRD/eval card Lab9 còn thiếu trong repo.
3. Demo ba mốc, giải thích S1-01/S1-20/S1-07 và loạtS1-40…43; dùng hai adhoc B7.3 để phản biện. Không đổi snapshot.
4. Sau khi bổ sung thông tin, chạy lại check_submission --collect. Nếu đổi code/config thì grade S1 trước khi collect. Hiện thiếu dữ liệu thành viên và commit ký theo message, chưa thể in ĐỦ THÀNH PHẦN.
5. Người dùng tự review/commit/push lên cuonglk; đưa bài hoàn chỉnh về main trước khi nộp. Mỗi thành viên tự nộp link LMS và exit ticket.

## Lệnh tái kiểm

```powershell
python -X utf8 -m unittest discover -s tests
python -X utf8 -m lab10.criteria verify
python -X utf8 -m lab10.checkpoint verify
python -X utf8 -m lab10.grade --incident S1
python -X utf8 -m lab10.check_submission --collect
```

Không chạy criteria sign hay checkpoint lần nữa. Không sửa bản copy trong submission/docs; sửa templates và collect lại. Một phần cuối grade xanh không thay kiểm thủ tục git và việc con người xác nhận trách nhiệm.
