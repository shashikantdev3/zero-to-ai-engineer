"""Zero to AI Engineer · Agents and Tools · Part 2 of 26
Slide: Validate, then check the owner
Run: python 06_validate_then_check_the_owner.py
"""
def refund_tool(raw: dict, user_id: str):
    # user_id comes from the verified token
    try:
        args = RefundArgs.model_validate(raw)
    except ValidationError as e:
        err = fail("INVALID_ARGS")
        err["detail"] = e.errors()[:3]
        return err
    if orders.get(args.order_id) != user_id:
        # do not reveal other users' orders
        return fail("NOT_FOUND")
    return {"ok": True}
