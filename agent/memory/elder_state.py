class ElderState:
    def __init__(self, elder_id: str):
        self.elder_id = elder_id
        self.last_event_ts = None
        self.recent_silence_windows = []
        self.risk_score = 0.0

    def update_from_event(self, event):
        self.last_event_ts = event.ts_ms

        if event.type.value == "SILENCE_WINDOW":
            self.recent_silence_windows.append(
                event.payload.get("silence_duration_sec", 0)
            )
