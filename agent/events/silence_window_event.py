from dataclasses import dataclass
from agent.events.base_event import BaseEvent, EventType


@dataclass
class SilenceWindowEvent(BaseEvent):

    def get_silence_duration(self) -> int:
        return self.payload.get("silence_duration_sec", 0)

    def get_anomaly_score(self) -> float:
        return self.payload.get("anomaly_score", 0.0)
