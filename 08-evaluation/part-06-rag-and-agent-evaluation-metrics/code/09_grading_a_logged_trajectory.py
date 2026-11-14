"""Zero to AI Engineer · Evaluation · Part 6 of 11
Slide: Grading a logged trajectory
Run: python 09_grading_a_logged_trajectory.py
"""
def grade_trajectory(steps, case):
    used = {s["tool"] for s in steps}
    bad = used & case["forbidden_tools"]
    need = case["required_tools"]
    return {
        "no_forbidden": not bad,
        "required_used": need <= used,
        "within_budget":
            len(steps) <= case["max_steps"],
        "final_state_ok":
            case["check_state"](),
    }
