from dataclasses import dataclass, field
from typing import Dict, Any, Literal, Optional
from enum import Enum
import uuid
import time


# -----------------------------
# ENUMS (STRICT & SAFE)
# -----------------------------

class EventType(str, Enum):
    ACOUSTIC_FEATURES = "ACOUSTIC_FEATURES"
    AUDIO_REF = "AUDIO_REF"
    EMOTION_RESULT = "EMOTION_RESULT"
    SCENE_RESULT = "SCENE_RESULT"
    SILENCE_WINDOW = "SILENCE_WINDOW"
    ALERT = "ALERT"
    CAREGIVER_CONFIRMATION = "CAREGIVER_CONFIRMATION"
    DOCTOR_VISIT_TRANSCRIPT = "DOCTOR_VISIT_TRANSCRIPT"
    MED_EVENT = "MED_EVENT"


class EventSource(str, Enum):
    ANDROID = "android"
    CLOUD_INFER = "cloud_infer"
    CAREGIVER_APP = "caregiver_app"
    SYSTEM = "system"


# -----------------------------
# CONSENT BLOCK
# -----------------------------

@dataclass
class Consent:
    monitoring_on: bool
    audio_upload: bool
    doctor_mode: bool


# -----------------------------
# BASE EVENT
# -----------------------------

@dataclass
class BaseEvent:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    elder_id: str = ""
    ts_ms: int = field(default_factory=lambda: int(time.time() * 1000))

    type: EventType = EventType.ACOUSTIC_FEATURES
    source: EventSource = EventSource.SYSTEM

    schema_v: int = 1
    consent: Consent = None

    payload: Dict[str, Any] = field(default_factory=dict)

    # -------------------------
    # VALIDATION (MVP SAFE)
    # -------------------------

    def validate(self) -> None:
        if not self.elder_id:
            raise ValueError("elder_id is required")

        if not isinstance(self.ts_ms, int):
            raise ValueError("ts_ms must be int (epoch milliseconds)")

        if self.consent is None:
            raise ValueError("consent block is required")

    # -------------------------
    # SERIALIZATION
    # -------------------------

    def to_dict(self) -> Dict[str, Any]:
        self.validate()

        return {
            "event_id": self.event_id,
            "trace_id": self.trace_id,
            "elder_id": self.elder_id,
            "ts_ms": self.ts_ms,
            "type": self.type.value,
            "source": self.source.value,
            "schema_v": self.schema_v,
            "consent": {
                "monitoring_on": self.consent.monitoring_on,
                "audio_upload": self.consent.audio_upload,
                "doctor_mode": self.consent.doctor_mode,
            },
            "payload": self.payload,
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "BaseEvent":
        return BaseEvent(
            event_id=data.get("event_id", str(uuid.uuid4())),
            trace_id=data.get("trace_id", str(uuid.uuid4())),
            elder_id=data["elder_id"],
            ts_ms=data["ts_ms"],
            type=EventType(data["type"]),
            source=EventSource(data["source"]),
            schema_v=data.get("schema_v", 1),
            consent=Consent(**data["consent"]),
            payload=data.get("payload", {}),
        )
