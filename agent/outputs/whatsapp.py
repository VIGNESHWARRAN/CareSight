def send_alert(elder_id: str, risk: float):
    message = (
        "⚠️ CareSight Alert\n"
        f"Elder ID: {elder_id}\n"
        f"Risk Score: {risk}\n"
        "Unusual silence detected.\n"
        "Please check immediately."
    )

    print(f"\n[WHATSAPP ALERT to {elder_id}]")
    print(message)
