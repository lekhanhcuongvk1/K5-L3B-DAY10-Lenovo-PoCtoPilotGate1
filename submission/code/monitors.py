"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def model_override_rate(trials):
    """Fraction of tickets with a claimed delay substituted for tracking, no labels."""
    return sum(any(e.get("type") == "model_override" for e in t.get("events", []))
               for t in trials) / max(1, len(trials))


def incomplete_tracking_rate(trials):
    """Share held at G1 for delivered parcels lacking a delivery date."""
    return sum(any(e.get("kind") == "tracking_incomplete" for e in t.get("events", []))
               for t in trials) / max(1, len(trials))


def carrier_strike_peak_per_day(trials):
    """Peak actual strikes for one carrier in one day/seed (never pool five seeds)."""
    counts = {}
    for t in trials:
        for row in t.get("faults", []):
            key = (t.get("day"), t.get("seed"), row.get("carrier_id"))
            counts[key] = counts.get(key, 0) + 1
    return max(counts.values(), default=0)


def held_carrier_strikes(trials):
    """Pending third-party reviews per simulated day, averaged over seeds."""
    return sum(e.get("kind") == "carrier_strike_held" for t in trials
               for e in t.get("events", [])) / max(1, len({t.get("seed") for t in trials}))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "model_override_rate": model_override_rate,
    "incomplete_tracking_rate": incomplete_tracking_rate,
    "carrier_strike_peak_per_day": carrier_strike_peak_per_day,
    "held_carrier_strikes": held_carrier_strikes,
}
STARTER_MONITORS = ("escalation_rate",)
