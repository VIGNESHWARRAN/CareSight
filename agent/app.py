from agent.memory.state_store import get_elder_state
from agent.reasoning.risk_scoring import compute_risk
from agent.reasoning.action_selector import should_alert
from agent.outputs.whatsapp import send_alert


def on_event(event):
    elder_state = get_elder_state(event.elder_id)

    elder_state.update_from_event(event)

    risk = compute_risk(elder_state)
    elder_state.risk_score = risk

    print(f"[DEBUG] Computed risk = {risk}")

    if should_alert(risk):
        print("[DEBUG] Risk above threshold → sending alert")
        send_alert(event.elder_id, risk)
    else:
        print("[DEBUG] Risk below threshold → no alert")
