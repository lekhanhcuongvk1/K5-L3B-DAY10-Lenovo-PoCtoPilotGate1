"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _policy(ctx):
    """G1: choose by effective dates, never by an index flag or customer text."""
    day = H.d(ctx.as_of)
    matches = [p for p in ctx.tools.lookup_policies()
               if H.d(p["effective_from"]) <= day
               and (not p.get("effective_to") or day <= H.d(p["effective_to"]))]
    return matches[0] if len(matches) == 1 else None


def _parcel(ctx, order):
    parcels = order.get("parcels") or []
    pid = ctx.ticket.get("parcel_id")
    if pid:
        return next((p for p in parcels if p["parcel_id"] == pid), None)
    return max(parcels, key=lambda p: H.db_delay_days(p, ctx.as_of)) if parcels else None


def pre_guard(ctx):
    try:
        policy = _policy(ctx)
        if policy is None:
            return Verdict.escalate("G1: không có đúng một chính sách có hiệu lực")
        order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
        if order:
            for p in order.get("parcels", []):
                delivered = p.get("delivered_date")
                if p.get("status") == "DELIVERED" and not delivered:
                    ctx.log("tracking_incomplete", field="delivered_date", parcel_id=p.get("parcel_id"))
                    return Verdict.escalate("G1: đã giao nhưng thiếu ngày giao")
                if delivered and (H.d(delivered) > H.d(ctx.as_of)
                                  or p.get("status") != "DELIVERED"):
                    return Verdict.escalate("G1: ngày và trạng thái giao mâu thuẫn")
                H.db_delay_days(p, ctx.as_of)
            if not _parcel(ctx, order):
                return Verdict.escalate("G1: thiếu kiện hàng hoặc parcel_id không thuộc đơn")
        ctx.log("policy_pinned", policy_id=policy["policy_id"])
        return Verdict.allow(policy_id=policy["policy_id"])
    except (ValueError, TypeError, KeyError):
        return Verdict.escalate("G1: dữ liệu ngày/chính sách không hợp lệ")


def _valid_approval(ctx, order, approval_id, amount):
    matches = ctx.tools.lookup_approvals(approval_id=approval_id)
    if len(matches) != 1:
        return False
    a = matches[0]
    approver = ctx.gates.get("operations", {}).get("approver_id")
    return (a.get("status") == "valid"
            and a.get("ticket_id") == ctx.ticket["ticket_id"]
            and a.get("order_id") == order["order_id"]
            and a.get("customer_id") == order["customer_id"]
            and bool(a.get("approver_id"))
            and (not approver or a.get("approver_id") == approver)
            and a.get("expires_at", "") >= ctx.as_of
            and a.get("max_vnd", 0) >= amount)


def write_gate(ctx, action):
    """G2 authorizes money; G3 protects third parties. No labels or ID exceptions."""
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier", "send_reply"):
        return Verdict.deny("không có quyền gọi tool ghi này")
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if tool == "send_reply":
        # A zero proposal bypasses issue_refund entirely. Verify negative decisions too.
        proposal = next((e for e in reversed(ctx.events) if e.get("type") == "proposal"), None)
        if (order and order.get("customer_id") == ctx.ticket.get("customer_id")
                and proposal and proposal.get("amount_vnd", 0) <= 0
                and not ctx.tools.ledger_rows(order_id=order["order_id"])):
            try:
                policy, parcel = _policy(ctx), _parcel(ctx, order)
                expected = H.entitlement_vnd(policy, order, H.db_delay_days(parcel, ctx.as_of),
                                              parcel.get("delay_cause"))
                if expected > 0:
                    ctx.log("false_denial_blocked", entitlement_vnd=expected)
                    return Verdict.escalate("G2: không từ chối quyền lợi thật theo lời khai; người kiểm lại")
            except (TypeError, KeyError, ValueError):
                return Verdict.escalate("G2: chưa đủ dữ kiện để gửi kết luận từ chối")
        return Verdict.allow()
    if not order or order.get("customer_id") != ctx.ticket.get("customer_id"):
        return Verdict.escalate("G2: chưa xác minh chủ đơn")
    if action.get("ticket_id") != ctx.ticket["ticket_id"]:
        return Verdict.escalate("G2: lệnh ghi không thuộc ticket hiện tại")
    try:
        policy, parcel = _policy(ctx), _parcel(ctx, order)
        if not policy or not parcel:
            return Verdict.escalate("G1: thiếu nguồn sự thật hợp lệ")
        delay = H.db_delay_days(parcel, ctx.as_of)
        entitlement = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        limits = ctx.tools.ops_limits()
        if tool == "issue_refund":
            if action.get("order_id") != order["order_id"]:
                return Verdict.escalate("G2: lệnh hoàn không thuộc đơn hiện tại")
            # A retry is skipped without converting an already-paid ticket into an escalation.
            if ctx.tools.ledger_rows(order_id=order["order_id"]):
                ctx.log("duplicate_refund_blocked", order_id=order["order_id"])
                return Verdict.deny("G2: sổ cái đã có khoản hoàn cho đơn; không ghi trùng")
            if entitlement <= 0:
                return Verdict.deny("G2: nguồn sự thật không cho quyền lợi hoàn")
            if action.get("payer") != "LOGIX":
                return Verdict.escalate("G2: lời khai không có quyền trừ tiền shop")
            approval = action.get("approval_id")
            if (entitlement > policy["auto_limit_vnd"] or approval) and not _valid_approval(
                    ctx, order, approval, entitlement):
                ctx.log("invalid_approval_blocked")
                return Verdict.escalate("G2: cần phê duyệt hợp lệ, đúng ticket/đơn/khách/người/tiền/ngày")
            if not approval:
                customer_spent = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(
                    customer_id=order["customer_id"]) if not r.get("approval_id"))
                if customer_spent + entitlement > limits.get(
                        "max_auto_refund_per_customer_per_day_vnd", float("inf")):
                    return Verdict.escalate("G2: vượt trần hoàn tự động cho khách; cần người duyệt")
                if ctx.tools.auto_refund_today_vnd() + entitlement > limits.get(
                        "daily_auto_refund_budget_vnd", float("inf")):
                    return Verdict.escalate("G2: vượt ngân sách Finance thực tế")
            # The carrier-strike limit governs blame, not the customer's verified refund.
            if action.get("amount_vnd") != entitlement:
                ctx.log("refund_corrected", proposed=action.get("amount_vnd"), allowed=entitlement)
                return Verdict.modify("G2: tính lại quyền lợi từ tracking và policy", amount_vnd=entitlement)
        elif tool == "file_carrier_fault":
            if not H.carrier_at_fault(policy, parcel, delay):
                return Verdict.deny("G3: không có nguyên nhân thuộc lỗi hãng theo policy hiện hành")
            if len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limits.get(
                    "max_auto_strikes_per_carrier_per_day", float("inf")):
                ctx.log("carrier_strike_held", carrier_id=parcel["carrier_id"],
                        parcel_id=parcel["parcel_id"], pic="NV-OANH")
                return Verdict.deny("G3: giữ lỗi hãng từ ngưỡng ngày để NV-OANH kiểm; vẫn hoàn đúng cho khách")
            if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
                return Verdict.deny("G3: đã ghi lỗi cho kiện này")
            return Verdict.modify("G3: quy trách nhiệm theo đúng kiện và tracking",
                                  order_id=order["order_id"], parcel_id=parcel["parcel_id"],
                                  carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"),
                                  delay_days=delay)
        elif tool == "notify_carrier":
            # Rebuild from verified facts; never copy customer text or recipient contacts.
            if not ctx.tools.fault_rows(ticket_id=ctx.ticket["ticket_id"],
                                        parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"]):
                return Verdict.deny("G3: chưa có lỗi hãng hợp lệ để thông báo")
            fields = set(policy.get("carrier_notice_fields", []))
            facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                     "district": order.get("recipient", {}).get("district"), "delay_days": delay}
            safe = {k: v for k, v in facts.items() if k in fields}
            ctx.log("carrier_payload_minimized", removed=sorted(set(action.get("payload", {})) - set(safe)))
            return Verdict.modify("G3: chỉ gửi trường cho phép từ nguồn sự thật",
                                  carrier_id=parcel["carrier_id"], payload=safe)
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate("G2/G3: thiếu hoặc sai kiểu dữ liệu để xác minh lệnh ghi")
    return Verdict.allow()
