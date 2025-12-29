def send_alert(elder_id: str, risk: float):
    message = (
        "⚠️ CareSight Alert\n"
        f"Unusual silence detected\n"
        f"Risk Score: {risk}\n"
        "Please check immediately."
    )

    print(f"[WHATSAPP ALERT to {elder_id}]")
    print(message)
