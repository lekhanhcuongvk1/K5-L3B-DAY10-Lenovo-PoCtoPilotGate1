# Team

**Cập nhật lịch sử ký:** nhánh khôi phục `cuonglk-restored-signing` hiện kế thừa đúng commit gốc `4b9d370` (`Sign acceptance criteria`, 19/11/2026 15:06:11), trước baseline 15:10:11. File tiêu chí và lock không đổi; không tạo lại thời điểm ký. Nhánh `cuonglk` cũ vẫn giữ nguyên. Các đoạn mô tả thiếu commit bên dưới ghi nhận sự cố trước khôi phục; lỗi checker này đã được xử lý ở nhánh khôi phục. Snapshot vòng 1 chưa commit/push trước nhận thẻ và thông tin ba thành viên vẫn cần xác nhận riêng.

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): Lenovo
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Lenovo-PoCtoPilotGate1`
- Thẻ sự cố: **S1**; nguồn repo minhhai203, 4 file khớp hash đề gốc.

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Lê Khánh Cường | 2A202603999 | Nhóm trưởng · Kỹ sư cổng 1: điều phối, tích hợp guards, kiểm chứng và quản lý repo | Có |
|   2 | Mai Danh Hiếu | 2A202603948 | Kỹ sư cổng 2: trace, behavioral test, monitor và bằng chứng đánh giá | Không |
|   3 | Trần Quang Minh | 2A202603929 | Sản phẩm và kinh doanh: tiêu chí, cách đo, chi phí/ROI và quyết định Gate 1 | Không |
|   4 | Nguyễn Hải Quang | 2A202603936 | Vận hành và pháp lý: HAZOP, checklist, runbook, risk register và kiểm bài nộp | Không |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công và sản phẩm cần bàn giao

Phân công bao gồm kiểm chứng, giải thích và trình bày phần việc được giao. Kết quả chạy trong hồ sơ là bằng chứng chung của nhóm; đóng góp cá nhân được xác nhận theo công việc thực tế. Quyết định v1/v2 cần cả nhóm thống nhất.

| Người | Phạm vi phụ trách | Việc cần thực hiện trước demo/nộp | Bằng chứng cần bàn giao |
|---|---|---|---|
| Lê Khánh Cường | Điều phối CP1–CP5; Phiếu B B7.1; Phiếu C C7/C9; guards và tích hợp repo | Đọc và giải thích G1/G2/G3, kiểm mối liên hệ nguyên nhân→cổng; nhận bản rà soát của ba người; chạy/xem lại kết quả kiểm cuối, tự review commit/push; trình Coach vấn đề lịch sử ký và snapshot | Bảng rà soát guards theo hàm/nhánh; commit tích hợp thực tế; kết quả kiểm cuối; ghi nhận hướng xử lý của Coach |
| Mai Danh Hiếu | Phiếu A A2 offline metric; B0–B2, B7.2–B7.3; C0/C2/C8; monitors.py | Dò S1-01/S1-20/S1-07 và loạt S1-40…43; tái chạy hai adhoc; giải thích 4 monitor, mẫu số/ngưỡng/điểm mù; đối chiếu report ba mốc và regression | Bảng ticket@seed + bước sai đầu tiên; output adhoc; giá trị monitor nền/S1; ghi rõ lệnh tự chạy và run ID mới nếu có |
| Trần Quang Minh | Phiếu A A1–A5; B1/B3/B6 lăng kính kinh doanh, B7.4/B8; C5/C12; business | Đối chiếu PRD/eval card Lab9; giải thích ngưỡng đã ký và pass_rate/pass^5/pass@5; so chi phí/ROI theo kho; kiểm sensitivity công held; đề xuất và trình cả nhóm xác nhận v2 | Lý do từng ngưỡng; bảng base/prepared/after; phép tính 5.870đ→khoảng7.408đ khi cộng công giả định; lý do giữ Cải tiến thêm và hạn23/11 |
| Nguyễn Hải Quang | B4–B5/B6 lăng kính người/pháp lý, B7.5–B7.6; C1/C3.5/C4/C6/C10/C11; operations/legal và submission | Rà HAZOP đủ dòng và nhánh ngoài code; xác minh PIC/quyền hạn/SLA; diễn giải trần2/ngày so hợp đồng3/7ngày; lập cách nhận task held/ACK; kiểm TEAM/members/manifest, deadline và LMS | Checklist9 nhóm có PIC; fault tree có bằng chứng lá; risk register; runbook có ai/ngưỡng/hành động/hạn; danh sách mục thiếu khi collect |

Quy tắc phối hợp: người phụ trách đề xuất sửa, Cường tích hợp. Không sửa tiêu chí đã ký, snapshot, file khóa hoặc nhật ký. Nếu đổi guards/monitors/operating_gates thì chạy lại public tests, grade S1 và collect trước commit; các run ID trong phiếu phải cập nhật theo bản thực tế. Mỗi người tự nộp link repo lên LMS.

## Cá nhân

**Khai báo sử dụng AI:** Codex hỗ trợ đọc đề, soạn Phiếu A/B/C và tiêu chí, triển khai cổng G1–G3, cấu hình vận hành, monitor và chạy kiểm tra. Nhóm chịu trách nhiệm kiểm chứng các ngưỡng, số liệu và quyết định. PRD v1.1/eval card Lab9 chưa có trong repo để đối chiếu, cần bổ sung trước khi xác nhận hồ sơ.

**Thông tin cần hoàn thiện:** danh tính của ba thành viên còn lại tại bảng thành viên, tiêu đề mục cá nhân và `submission/submission.json`. Báo cáo cá nhân và exit ticket cần được từng thành viên đọc, xác nhận theo phần việc và hiểu biết thực tế trước khi nộp.

## LeKhanhCuong-2A202603999

### Phần việc phụ trách

Tôi là nhóm trưởng Lenovo, phụ trách điều phối và tích hợp kỹ thuật ở vai Kỹ sư cổng 1. Phạm vi của tôi gồm quản lý repo, phân công và tổng hợp hồ sơ CP1–CP5; cổng G1/G2/G3 trong `lab10/guards.py`; liên kết giữa biện pháp và bằng chứng ở Phiếu B B7.1, Phiếu C C7/C9. Tôi điều phối việc cả nhóm xác nhận quyết định ở B8/C12, không thay quyền đánh giá của từng vai.

Tôi phụ trách kiểm chứng và tích hợp kết quả kỹ thuật, có sử dụng Codex hỗ trợ triển khai, soạn tài liệu và chạy kiểm tra.

### Đóng góp cụ thể

1. Tôi yêu cầu rà soát toàn bộ hướng dẫn, quy tắc, checkpoint, rubric và yêu cầu nộp trước khi làm bài; sau đó yêu cầu triển khai hồ sơ lab và giữ phần thông tin thành viên để nhóm tự bổ sung.
2. Tôi cung cấp danh tính trưởng nhóm, xác nhận tên Lê Khánh Cường/MSSV2A202603999, cung cấp repo thẻ và xác nhận nhóm được giao card1. Nhờ đó phần sự cố được xử lý đúng S1, không tự chọn hoặc làm thẻ của nhóm khác.
3. Tôi yêu cầu giữ quyền tự commit/push và làm việc trên nhánh `cuonglk`. Lịch sử hiện tại có các commit `17ef9fb` và `043e554` mang danh tính MSSV của tôi; đây là bằng chứng quản lý/tích hợp repo, không chứng minh tôi đã tự viết từng dòng code.
4. Tôi điều phối việc sử dụng AI hỗ trợ đọc đề/code, soạn báo cáo, đề xuất tiêu chí, triển khai cổng/monitor và đánh giá; phân công các thành viên kiểm chứng phần chuyên môn tương ứng.
5. Về lịch sử ký: commit ký gốc do AI thực hiện đã được yêu cầu gỡ để tôi tự commit lại. Việc này khiến checker hiện không tìm thấy commit đúng message và lịch sử trước đo. Tôi ghi nhận đây là vấn đề cần trình Coach, giữ nguyên lock/journal/snapshot và không thay đổi thời điểm để tạo bằng chứng giả.

**Việc tôi còn phải hoàn tất trước nộp:** giải thích được từng nhánh guard và các ca S1-07/S1-20/S1-42; cùng nhóm đọc lại quyết định v2; nhận bản kiểm tra từ ba vai; xác nhận với Coach cách xử lý thủ tục; tự review, commit/push bản cuối và nộp LMS. Các việc này chưa được ghi là đã hoàn thành trong report này.

### Bằng chứng

- **Repo:** nhánh `cuonglk`; commit `17ef9fb` và `043e554` có author2A202603999. Các thay đổi sau đó còn chờ tôi review/commit, không gán hash chưa tồn tại.
- **Nguồn thẻ:** `incidents/S1/`, xác nhận card1 từ repo minhhai203; 4 file đã được công cụ kiểm khớp MANIFEST gốc.
- **Bằng chứng đánh giá chung:** grade `R-S1-grade-20261119-161212-5110cc`; S1 65/65, nền110/110, public13/13, PASS-VISIBLE; chi phí5.870đ/ticket,ROI0,70,coverage100%; hoàn sai/lỗi oan/PII đều0. Test ẩn chưa chạy.
- **Bằng chứng hồ sơ:** Phiếu B B7.1/B8; Phiếu C C7/C9/C12; `submission/docs/final-handoff.md`. Snapshot vòng1 hash`e0e28e3d`, tiêu chí hash`6903f01b` còn nguyên; A5 ghi vấn đề lịch sử commit.
- **Quyết định đề xuất:** Cải tiến thêm ở cả v1/v2; v2 vẫn thiếu công xử lý task held, lịch sử lỗi7ngày và xác nhận thủ tục. Cần nhóm thống nhất trước khi nộp.

### Exit ticket

- **Điều rút ra từ hồ sơ:** một report xanh chưa đủ quyết định pilot. Cần kiểm cả trường hợp AI từ chối sai (S1-07), chi phí phát sinh cho con người và giới hạn của dữ liệu; cổng bảo vệ bên thứ ba phải đặt đúng hành động để không giữ cả quyền lợi hợp lệ của khách.
- **Điều còn chưa chắc:** công và thời gian xử lý2 ca lỗi hãng giữ/ngày trong vận hành thật, cùng dữ liệu lỗi7ngày, có làm CT vượt chi phí thủ công hoặc chạm ngưỡng ngưng tuyến hay không. Nhóm cần đo thêm và có Coach xác nhận thủ tục trước khi kết luận đủ điều kiện pilot.

## MaiDanhHieu-2A202603948

### Phần việc phụ trách

Vai được phân công: **Kỹ sư cổng 2**, phụ trách bằng chứng đánh giá, trace và chỉ số theo dõi. Phạm vi gồm Phiếu A A2; Phiếu B B0–B2, B7.2–B7.3; Phiếu C C0, C2, C8; `lab10/monitors.py` và các report ba mốc. Trách nhiệm cá nhân là giải thích bước sai đầu tiên, kiểm cách tính monitor, phân biệt kết quả offline với tín hiệu production và trình bày bằng chứng khi demo.

### Đóng góp cụ thể

Nội dung chuyên môn của phần việc:

1. **Phân tích trace theo nguyên nhân.** `S1-01@11` có tracking 2 ngày nhưng model dùng lời khai 5 ngày, dẫn đến hoàn 20.000đ và ghi lỗi GHSH. `S1-20@11` có trạng thái DELIVERED nhưng ngày giao null; helper dùng ngày xử lý tạo độ trễ 6 ngày. Hai lỗi cùng gây lỗi hãng oan nhưng có nguồn khác nhau: đặt sai trọng số lời khai và dữ liệu thiếu.
2. **Nhận diện bỏ sót của vòng 1.** `S1-07@11` có tracking 4 ngày, lời khai 2 ngày, proposal bằng 0 nên không gọi `issue_refund`. Chỉ kiểm lệnh hoàn sẽ không phát hiện câu từ chối sai. Bản sau kiểm trước `send_reply` và chuyển người khi quyền lợi DB dương, không thông báo đã hoàn nếu sổ cái trống.
3. **Thiết kế kiểm tra tính chất.** Hai adhoc ở B7.3 thay số ngày khách khẳng định thành 99 và 100 trên hai đơn khác nhau. Khi DB chưa đạt ngưỡng hoàn, cả hai đều không tạo khoản hoàn, lỗi hãng hoặc thông báo hãng. Kiểm tra theo tính chất dữ liệu giúp hạn chế viết cổng khớp riêng một mã ticket.
4. **Theo dõi bằng dữ liệu không nhãn.** Bốn monitor là `model_override_rate`, `incomplete_tracking_rate`, `carrier_strike_peak_per_day`, `held_carrier_strikes`. Hai tỷ lệ dùng tổng trial làm mẫu số; đỉnh lỗi nhóm theo ngày/seed/hãng, không cộng 5 seed thành một ngày; số ca giữ lấy trung bình qua seed. Không đọc nhãn hoặc pass/fail để làm tín hiệu production.
5. **Diễn giải giới hạn.** Override vẫn cao sau sửa vì monitor đo ý định model thay số, không đo số tiền đã ghi sai. PASS-VISIBLE chưa chứng minh đạt test ẩn; một ca chuyển người được chấp nhận không có nghĩa khách đã nhận tiền.

**Sử dụng AI:** Codex hỗ trợ code monitor, trace và kiểm tra. Trách nhiệm cá nhân được phân công là kiểm chứng công thức, diễn giải kết quả và trình bày bằng chứng; kết quả công cụ không được coi là bằng chứng đã tự thực hiện từng thao tác.

### Bằng chứng

- Grade chung: `R-S1-grade-20261119-161212-5110cc`; S1 đạt 65/65, bộ nền 110/110; các mục integrity, criteria, visible, regression và monitor đều đạt; test ẩn chưa chạy.
- Report S1 sau sửa: `R-S1-after-20261119-161213-5110cc`. Giá trị monitor lần lượt 0,461538; 0,153846; 2; 2. Bộ nền tương ứng 0,045455; 0; 1; 0.
- Vị trí phân tích: Phiếu C C2/C8; code `lab10/monitors.py`; hai adhoc và kết quả tại Phiếu B B7.3.
- Kết quả public tests được công cụ chạy: 13/13 đạt. Không gán một commit hoặc lần chạy riêng cho tôi khi chưa có bằng chứng như vậy.

### Exit ticket

- **Điều rút ra từ hồ sơ:** phải theo dõi cả quyết định không hành động và quyết định ghi tiền. Cổng kiểm lệnh hoàn có thể đúng nhưng hệ thống vẫn từ chối sai; monitor có báo động không đồng nghĩa tác hại đã xảy ra.
- **Điều còn chưa chắc:** tỷ lệ cảnh báo giả và khả năng mất telemetry khi triển khai thật. Cần đo lại theo cửa sổ thời gian, số lượng ticket và nguồn dữ liệu trước khi dùng ngưỡng mock để trực vận hành.

## TranQuangMinh-2A202603929

### Phần việc phụ trách

Vai được phân công: **Sản phẩm và kinh doanh**. Phạm vi gồm Phiếu A A1–A5; Phiếu B B3, B6, B7.4, B8; Phiếu C C5/C12; giải thích `acceptance_criteria.json` đã ký và phần `business` trong `operating_gates.json`. Trách nhiệm là gắn mục tiêu với khách, kế toán, người duyệt và đối tác; đánh giá hiệu quả kinh tế theo phân khúc; trình cả nhóm quyết định Gate 1 có căn cứ.

### Đóng góp cụ thể

Nội dung chuyên môn của phần việc:

1. **Mục tiêu cấp hệ thống.** Thành công phải đồng thời bảo đảm đúng quyền lợi, không ghi oan hãng/không lộ dữ liệu, tiết kiệm chi phí và không đẩy quá tải sang người duyệt. Chị Oanh cần đối soát được sổ, chị Hạnh cần giữ quyền duyệt ngoại lệ và đủ năng lực nhận ca.
2. **Giải thích tiêu chí.** Ngưỡng pass_rate là 0,99 và pass^5 là 0,98; pass^5 đòi đúng cả 5 lần, khác pass@5 chỉ cần đúng ít nhất một lần. Các ngưỡng hoàn sai, lỗi hãng oan và PII bằng 0. Chi phí tối đa 8.000đ/ticket so với làm tay 10.000đ tạo biên 20%; nếu không mất tiền, ROI tương ứng là (10.000−8.000)/8.000 = 0,25. Tiêu chí được ký trước đo và không sửa để khớp kết quả.
3. **Giải thích cổng kinh doanh.** Trần ngày 1.600.000đ bằng 80% Finance 2.000.000đ; ngân sách ticket 1.200đ chừa phần dự phòng dưới trần 1.500đ. Phạm vi mô phỏng giữ 100%, không loại ticket xấu để tăng điểm. ROI tối thiểu 0,25 khớp tiêu chí.
4. **So sánh ba mốc S1.** Chi phí/ticket là 2.964đ → 6.616đ → 5.870đ; ROI −2,74 → 0,51 → 0,70. Base rẻ nhưng có 985.000đ hoàn sai trên 5 seed nên không phải phương án có lợi. Kho CT giảm từ 10.320đ prepared xuống 7.053đ after; vẫn cần xem riêng phân khúc này.
5. **Phân tích chi phí chưa được mô hình hóa.** Bổ sung bảng đối chiếu ở Phiếu C C5: 8.304đ công trợ lý + 38.000đ công duyệt + 30.000đ trực = 76.304đ/ngày. Với giả định công riêng cho 2 ca held là 20.000đ/ngày ngoài công đã tính, tổng là 96.304đ, tương đương khoảng 7.408đ/ticket và ROI 0,35. Biên công bổ sung tối đa theo ngưỡng đã ký là 27.696đ/ngày (13.848đ/ca nếu đúng 2 ca). Nếu toàn bộ 20.000đ phát sinh ở CT thì chi phí CT khoảng 13.720đ/ticket, cao hơn làm tay. Đây là các kịch bản giả định; cần đo công thật và tránh cộng trùng công duyệt đã có.
6. **Cơ sở quyết định.** V2 giữ Cải tiến thêm dù mọi ngưỡng report đạt, vì còn thiếu lịch sử lỗi 7 ngày, đường nhận ca giữ và chi phí đầy đủ; hạn xem lại 23/11/2026. Việc đối chiếu PRD/eval card Lab9 và xác nhận của cả nhóm còn cần thực hiện; không nhận là đã hoàn thành khi tài liệu chưa có trong repo.

**Sử dụng AI:** Codex hỗ trợ tiêu chí, phân tích số liệu và quyết định đề xuất. Trong lần rà soát này, tôi yêu cầu Codex đối chiếu chi phí từ report cuối, bổ sung bảng tính và kịch bản công held vào C5, cập nhật bằng chứng trong mục cá nhân. Đây là phần tài liệu có AI hỗ trợ, không phải tuyên bố tôi đã tự chạy grade hoặc đo công vận hành thực tế. Tôi phụ trách giải thích phép tính và trình nhóm xác nhận; giữ nguyên tiêu chí đã niêm phong.

### Bằng chứng

- Phiếu A A1/A2/A4; Phiếu B B3/B7.4/B8; Phiếu C C5/C12; `config/acceptance_criteria.json` và `config/operating_gates.json`.
- Grade chung cuối trong gói nộp: `R-S1-grade-20261119-173049-5110cc`; report after S1 `R-S1-after-20261119-173049-5110cc` có chi phí 5.870đ, ROI 0,70, coverage 1,0 và không vượt trần. Bảng tính C5 dùng `ops.cost` và `ops.segments` của chính report này; không tạo lần grade mới cho thay đổi tài liệu.
- Quyết định `Cải tiến thêm` khớp Phiếu C C12 và `submission/submission.json`; ba câu bắt buộc đã trùng nội dung.
- Checker đã xác nhận commit ký gốc `4b9d370` lúc 15:06:11 trước lần đo đầu 15:10:11; tiêu chí và lock còn nguyên. Vấn đề snapshot vòng 1 chưa commit/push trước nhận thẻ vẫn cần Coach xác nhận riêng. PRD v1.1/eval card Lab9 đã được bổ sung và đối chiếu tại `submission/docs/lab9-crosswalk.md`, kèm hai bản nguồn trong `submission/docs/lab9/`. Các ghi chú thiếu Lab9 trước đó phản ánh thời điểm chưa bổ sung tài liệu. Nhóm còn cần xác nhận chọn bản này làm nguồn chung; không coi đây là phê duyệt của giảng viên.

### Exit ticket

- **Điều rút ra từ hồ sơ:** pass cao và chi phí máy thấp chưa chứng minh có hiệu quả kinh tế; phải tính tiền mất, công người, phí trực và phân khúc yếu nhất. Quyết định Cải tiến thêm có thể đúng dù report cho phép cân nhắc Tiếp tục.
- **Điều còn chưa chắc:** chi phí đối soát thật và phân bố tải theo kho có làm thay đổi ROI hay không. Trước pilot cần đo TCO, thời gian xử lý và độ phủ hữu ích thay vì suy rộng trực tiếp từ mock.

## NguyenHaiQuang-2A202603936

### Phần việc phụ trách

Vai được phân công: **Vận hành và pháp lý**. Phạm vi gồm Phiếu B B4/B5/B7.5/B7.6; Phiếu C C1/C3.5/C4/C6/C10/C11; phần `operations`/`legal`, checklist 9 nhóm, HAZOP, fault tree, risk register, runbook và tính đầy đủ của bài nộp. Trách nhiệm là nối tín hiệu với người chịu trách nhiệm, ngưỡng, hành động và thời hạn; lưu ý tác hại với hãng, tài xế và người nhận không trực tiếp dùng trợ lý.

### Đóng góp cụ thể

Nội dung chuyên môn của phần việc:

1. **Rủi ro ngoài model.** HAZOP xét dữ liệu thiếu, người duyệt quá tải, ngân sách, phạm vi và PII; fault tree nối tác hại với lời khai sai, ngày giao thiếu và quyền áp chế tài tích lũy. Mỗi nhánh có ticket@seed, trường dữ liệu hoặc số report, không chỉ nói chung là model sai.
2. **Nguồn sự thật theo kiện.** DELIVERED nhưng delivered_date null không đủ kết luận số ngày trễ; delay_cause null không chứng minh hãng có lỗi. Cần chứng từ giao hàng/POD và đối soát trước chế tài, không dùng ngày xử lý để lấp dữ liệu thiếu.
3. **Phân quyền và vận hành.** NV-TUNG là PIC/đầu mối dừng; NV-HANH duyệt hoàn và ca thiếu chứng từ; NV-OANH đối soát hãng/shop. Cấu hình giữ 1 người, 6 ca/giờ, SLA 60 phút, kiểm mẫu 10%, có decision_note. Chờ 30 phút hoặc ít nhất 3 ca chưa nhận phải điều phối; vi phạm an toàn dừng thao tác ảnh hưởng trong 5 phút theo kế hoạch.
4. **Trách nhiệm hãng khác quyền lợi khách.** Trần tự động 2 lỗi/hãng/ngày phải giữ riêng lệnh ghi lỗi từ lần thứ 3; khoản hoàn đúng của khách vẫn được xử lý. S1-42/43 tạo tín hiệu giữ cho NV-OANH. Tuy nhiên log chưa là task bền vững và trần ngày không thay kiểm hợp đồng ngưng tuyến sau 3 lỗi/7 ngày.
5. **Runbook và risk register.** Đề xuất task có PIC, thời hạn xác nhận nhận việc 30 phút và chứng từ đối soát; mô tả cách báo GHSH trước 17h theo tình huống thẻ, xử lý dữ liệu đã gửi và điều kiện bật lại. Đây là quy trình mô phỏng, không phải email đã gửi hoặc diễn tập production đã hoàn thành.
6. **Bài nộp và quyền lợi thành viên.** Hồ sơ phải có TEAM và report từng người, `members` khớp danh tính, ba phiếu, code/config hai vòng, report ba mốc, journal và manifest. Mỗi người tự nộp link LMS. Kiểm đủ thành phần không thay kiểm chất lượng hoặc tự xác nhận vấn đề lịch sử Git đã được Coach chấp thuận.

**Sử dụng AI:** Codex hỗ trợ phân tích, runbook và kiểm bài. Trách nhiệm cá nhân được phân công là rà soát và xác nhận tính khả thi; liên hệ đối tác, phê duyệt của Coach và diễn tập vẫn là các việc chưa có bằng chứng hoàn thành.

### Bằng chứng

- Phiếu B B4/B5/B7.5/B7.6; Phiếu C C3.5/C4/C6/C9/C10/C11; `config/operating_gates.json` và báo cáo ba mốc.
- `S1-20@11` minh họa ngày giao thiếu; loạt S1-40…43 minh họa lỗi tích lũy; after `carrier_strike_peak_per_day=2`, `held_carrier_strikes=2`.
- Grade chung `R-S1-grade-20261119-161212-5110cc`: lỗi hãng oan 30→0, PII 0, chờ max 0, ca ùn 0 trong mock; không suy ra đã kiểm được SLA thật.
- Cập nhật ngày 20/11/2026: TEAM và submission.json có đủ 4 thành viên khớp MSSV; commit ký gốc `4b9d370` lúc15:06:11 có trước baseline15:10:11. Mô tả thiếu commit ký ở bản cũ không còn đúng; bằng chứng commit/push snapshot trước nhận thẻ vẫn cần Coach xác nhận.

### Bổ sung kết quả rà soát ngày 20/11/2026

Theo yêu cầu của tôi, Codex hỗ trợ đọc và đối chiếu hồ sơ vận hành/pháp lý với code, dữ liệu mô phỏng và công cụ kiểm tra. Đây là đóng góp rà soát có AI hỗ trợ; không nhận là tôi tự viết code gốc, tự chạy công cụ bằng tay, đã demo, liên hệ đối tác hoặc được Coach phê duyệt.

| Hạng mục rà soát | Bằng chứng và kết luận | Việc xử lý / giới hạn |
|---|---|---|
| HAZOP | B4 có5 dòng kỹ thuật và4 dòng ngoài kỹ thuật; C4 có5 dòng, gồm lịch sử7ngày chưa thấy trên trace. Có S1-01, S1-20/21, S1-40…43 | Đủ cấu trúc; giữ nguyên phân tích vòng1. DB sai dù đủ trường vẫn là rủi ro mở |
| Checklist và PIC | B5/C11 đủ9 nhóm có PIC. staff: NV-TUNG/Lê Thanh Tùng giữ công tắc; NV-HANH/Trần Thị Hạnh duyệt hoàn vượt hạn mức; NV-OANH/Phạm Kiều Oanh đối soát | Mã PIC có người tương ứng trong mock; chưa chứng minh đã nhận việc thật. C11 làm rõ giới hạn thẩm quyền |
| Operations và SLA | Config:1 người,6ca/giờ,SLA60phút,sampling10%,decision_note=true. Runbook báo sớm30phút,dừng trong5phút | Ngưỡng kế hoạch khớp; kênh cảnh báo mô phỏng và chờ=0 chưa chứng minh SLA hay thời gian dừng thật |
| Giờ cao điểm | 14ca đồng thời,10phút/ca:1người thì ca cuối bắt đầu phút130. B7.6 ghi65/43,3phút với công suất gộp2/3người | ops.py mô phỏng công suất gộp; nếu người thật xử lý ca nguyên song song thì ca cuối bắt đầu phút60/40. Không coi số mô phỏng là dự báo chính xác thực tế; chưa đổi config khi chưa đo tải/ROI |
| Legal và cổng ghi | Config chặn recipient_contact/customer_note/name/phone/street, yêu cầu nguyên nhân lỗi. write_gate kiểm carrier_at_fault/đúng kiện và dựng payload từ facts theo allowlist policy | Không gửi văn bản tự do; PII=0 chỉ là metric mock, chưa chứng minh mọi kênh dữ liệu đều an toàn |
| Risk register/task held | C10 có tracking sai,trần2/ngày so với3/7ngày,công held và thủ tục. Guard giữ lỗi thứ3 và ghi log cho NV-OANH, chưa tạo task bền vững | Cập nhật rủi ro thủ tục lỗi thời; bổ sung C11 task/PIC/ACK30phút,điều phối quá hạn,giữ chế tài và đo công riêng. Đây là đề xuất trước pilot |
| Bài nộp/quyết định | Grade lưu R-S1-grade-20261119-173049-5110cc PASS-VISIBLE; hash code5110ccfb8217. V1/v2 Cải tiến thêm; đủ4 thành viên | Giữ tiêu chí,snapshot,code/config. Main đã có bổ sung Lab9/crosswalk của nhóm; còn cần thống nhất nguồn. Test ẩn,demo,Coach và LMS chưa có bằng chứng hoàn tất |

**Bàn giao:** cập nhật mục cá nhân và Phiếu C C10/C11; đồng bộ Phiếu C vào submission và sinh lại manifest bằng collect. Giữ các thay đổi chi phí và nguồn Lab9 mới của nhóm, giữ nguyên v1 và file khóa. Các đoạn bàn giao cũ cần đọc theo thời điểm ghi.

**Kiểm chứng có AI hỗ trợ:** public tests13/13 đạt; tiêu chí/snapshot ok; config hợp lệ, hash code khớp grade đã lưu; check_submission in ĐỦ THÀNH PHẦN sau khi gom lại. Dùng nguyên report và nhật ký đã lưu, không tạo grade mới hay sửa thời điểm lịch sử. Commit/push là bước bàn giao Git, không thay xác nhận Coach hoặc nộp LMS.

### Exit ticket

- **Điều rút ra từ hồ sơ:** thêm người duyệt hoặc ghi log không tự tạo ra kiểm soát có hiệu lực. Phải có người nhận thật, quyền quyết định, thời hạn và chi phí; bảo vệ hãng cũng phải giữ đúng quyền lợi hoàn tiền của khách.
- **Điều còn chưa chắc:** việc nhận task giữ, truy lịch sử lỗi 7 ngày và dừng trong 5 phút có hoạt động khi tải dồn hoặc nguồn chứng từ lỗi hay không. Cần diễn tập và đo trước pilot; kết quả mock chưa thay được bằng chứng vận hành này.
