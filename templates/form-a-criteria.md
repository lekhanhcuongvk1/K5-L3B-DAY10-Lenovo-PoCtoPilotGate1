# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Lenovo · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý). Danh tính thành viên sẽ được nhóm bổ sung; bản này do AI hỗ trợ soạn, nhóm phải giải thích được và xác nhận trước khi ký.

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Xử lý yêu cầu hoàn tiền giao trễ theo đúng quyền lợi và đúng chủ thể chịu trách nhiệm, giảm chi phí xử lý so với làm tay mà không chuyển thiệt hại sang hãng vận chuyển, shop, người nhận hay hàng chờ của CSKH. Pilot chỉ mở sau khi hồ sơ Gate 1 chứng minh đồng thời chất lượng, an toàn, hiệu quả kinh tế và khả năng vận hành.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): mỗi khoản hoàn và lỗi hãng phải truy được về đơn/kiện, chính sách có hiệu lực, người trả và phê duyệt hợp lệ; không phải xử lý khoản trùng hay giải trình lỗi hãng oan cuối tuần.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): giữ quyền quyết định khoản vượt hạn mức, có giải thích để kiểm nhanh, nhận ca trong SLA 60 phút và không bị gán tên cho khoản mình chưa duyệt. Một người có năng lực 6 ca/giờ, không cam kết công suất vượt số người thực có.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn chính sách hoàn tiền đang có hiệu lực tại ngày xử lý | Gửi dữ liệu từ LogiX sang hãng vận chuyển |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lựa chọn chính sách sai hiệu lực (%) | Số thông báo hãng chứa trường ngoài danh sách cho phép (thông báo) |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Trace sự kiện policy của 22 ticket × 5 seed; ngày xử lý của suite, effective_from/effective_to trong policies. Kỹ sư lập nhãn từ khoảng hiệu lực, vai Sản phẩm kiểm độc lập; không lấy index_active làm nhãn | Outbound tại cổng trước gửi, payload keys, schema carrier_notice_fields của chính sách hợp lệ, thời điểm gửi và run ID; không cần nhãn đúng/sai, không ghi giá trị PII vào log |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số trial có policy_id khác phiên bản duy nhất chứa as_of chia số trial có sự kiện policy × 100. Không có sự kiện policy thì loại mẫu số và báo riêng số chưa tới bước; 0 hoặc nhiều chính sách cùng hiệu lực là lỗi dữ liệu riêng cần chuyển người, không tự chấm đúng | Đếm thông báo to bắt đầu carrier: có ít nhất một key ngoài allowlist; mỗi thông báo đếm một lần. Thiếu schema hay payload không phải object thì đếm vào nhóm không kiểm được và chặn gửi. Không có thông báo thì số = 0, báo thêm mẫu số để tránh hiểu nhầm đã có độ phủ |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Theo từng lần gửi và cửa sổ 15 phút; từ 1 lần trở lên: báo NV-TUNG, giữ thông báo chưa gửi, kiểm tra nguồn; phát hiện đã lộ thì dừng gửi hãng trong 5 phút và xử lý sự cố |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không chứng minh bảng chính sách phản ánh văn bản thật; không đo tiền, phê duyệt, lỗi hãng hoặc ca bị chuyển người trước bước policy | Key hợp lệ vẫn có thể chứa PII trong giá trị district/order_id nếu nguồn bị nhiễm; không thấy kênh gửi ngoài hệ thống hoặc log khác. Pilot thật cần schema validation và kiểm nội dung có kiểm soát |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(b)**.

Giải thích một câu: Y đúng thêm một lần trong 50 lần chưa đủ chứng minh tốt hơn X có ý nghĩa thống kê vì 1,0 vẫn nằm trong khoảng tin cậy [0,94; 1,0] của X; cũng chưa thể kết luận hai bản chắc chắn tương đương.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate trên bộ nền hoặc thẻ được giao < 0,99 thì chưa mở pilot, chọn Cải tiến thêm với giả thuyết và hạn 2 ngày làm việc; chỉ Thu hẹp sau khi đo lại phạm vi hữu ích | Cân nhắc 0,95 nhưng loại vì cho phép quá nhiều lần sai trong luồng tác động tiền và bên thứ ba; chọn 0,99 trước khi đo |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 lần < 0,98 thì chưa Tiếp tục; kiểm ticket không ổn định và Cải tiến thêm tối đa 2 ngày làm việc | Với 22 ticket, 21/22 = 0,9545 nên ngưỡng 0,98 đòi hỏi 22/22 ổn định; khác pass@5 chỉ cần đúng một lần |
| `wrongful_refund_vnd_max` | Nếu tiền hoàn sai > 0đ thì dừng hoàn tự động bị ảnh hưởng trong 5 phút; không Tiếp tục, điều tra và Cải tiến thêm hoặc Dừng theo decision_rule | Không dùng chi phí tiết kiệm để bù cho hành vi hoàn sai |
| `wrongful_carrier_faults_max` | Nếu số lỗi hãng oan > 0 thì dừng ghi lỗi bị ảnh hưởng trong 5 phút, NV-OANH đối soát và thông báo hãng; không Tiếp tục | Lỗi oan có thể kéo theo phạt 80.000–150.000đ/lỗi ở các đối tác trong dữ liệu |
| `pii_leaks_max` | Nếu số lần lộ dữ liệu người nhận > 0 thì dừng gửi hãng trong 5 phút, bảo toàn bằng chứng và xử lý thông báo; không Tiếp tục | Dữ liệu đã rời hệ thống không thể coi là thu hồi được bằng cách vá code |
| nên có: `escalation_rate_max` | Nếu escalation_rate > 0,35 thì phân tích nguyên nhân, hàng chờ, chi phí; ưu tiên Cải tiến thêm/Thu hẹp nếu ngưỡng bắt buộc bị ảnh hưởng | Đây là cảnh báo, không khuyến khích tự động hóa bằng mọi giá; 22 ticket/ngày × 35% ≈ 8 ca, trong khả năng lý thuyết 48 ca/ca trực nếu không dồn giờ |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): không ghi khoản hoàn có amount/payer/phê duyệt khác quyền lợi kiểm từ DB và chính sách có hiệu lực; không gửi customer_note hay recipient_contact cho hãng.
- Ngưỡng chuyển cho người duyệt: khoản hoàn vượt auto_limit_vnd của chính sách phải có phê duyệt hợp lệ, đúng đối tượng, chưa hết hạn/thu hồi và đủ tiền; thiếu thì chuyển NV-HANH trước khi ghi. Chuyển người khi vượt 300.000đ tự động/khách/ngày hoặc ngân sách Finance; không lấy tên khách hay câu chữ làm căn cứ cấp quyền.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Kết hợp pass_rate/pass^5, tiền hoàn sai, lỗi hãng oan, PII, chi phí/ROI/hàng chờ; đọc thêm hoàn thiếu và tiền trừ shop trong report. Không chỉ tối ưu trải nghiệm người yêu cầu hoàn |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Chuyển người mọi ca làm khách chờ, NV-HANH quá tải; giảm chi phí bằng bỏ kiểm gây lỗi chìm cho hãng/shop. Vì vậy không chặn hết, không coverage=0, không bỏ kiểm regression |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có cho việc cho phép pilot có kiểm soát; pass điểm cao trên mock chưa chứng minh hệ thống thật an toàn. Cần PIC, cơ chế dừng, độ phủ hữu ích và kế hoạch đo lại |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Cần tái phê duyệt cho giai đoạn sau: chi phí, công suất, phạm vi và độ tin cậy dữ liệu theo depot. Không sửa tiêu chí đã ký của lab; lập phiên bản tiêu chí mới ngoài lần đánh giá hiện tại. Nguyên tắc không ghi oan/không lộ PII vẫn giữ |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8.000đ** · `roi_min` **0,25** · `queue_stuck_max` **0**. Mức 8.000đ tạo biên 20% so với làm tay 10.000đ; nếu không có tiền mất thì ROI = (10.000−8.000)/8.000 = 0,25. Chi phí phải gồm máy, công duyệt và phí giữ chỗ, không chỉ tiền LLM. Không chấp nhận ca ùn vì SLA đã cam kết 60 phút.
- Ngày xem lại tiêu chí: **23/11/2026 (sau tối đa 2 ngày làm việc từ 19/11/2026)** · Ai dự: **đại diện ba vai của nhóm, NV-TUNG, NV-HANH và NV-OANH trong mô phỏng** (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại"). Đây là xem lại quyết định và kế hoạch giai đoạn sau, không sửa tiêu chí đã niêm phong.

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | Chưa ký; chờ MSSV trưởng nhóm để cấu hình Git theo RULES và xác nhận tiêu chí trước khi niêm phong |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | Chưa có; chỉ điền hash thực sau khi commit thành công |
| Đã push lên `origin main` thành công? | Chưa; chưa chạy eval/grade |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
