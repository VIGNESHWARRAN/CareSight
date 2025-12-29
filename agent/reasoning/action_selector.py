

ALERT_THRESHOLD = 0.7

def should_alert(risk_score: float) -> bool:
    return risk_score >= ALERT_THRESHOLD
