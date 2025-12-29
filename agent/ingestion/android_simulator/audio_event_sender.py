import time
from agent.events.base_event import (
    BaseEvent,
    EventType,
    EventSource,
    Consent
)

ELDER_ID = "elder_001"


def silence_window_event(duration_sec: int, anomaly_score: float):
    return BaseEvent(
        elder_id=ELDER_ID,
        type=EventType.SILENCE_WINDOW,
        source=EventSource.ANDROID,
        consent=Consent(
            monitoring_on=True,
            audio_upload=False,
            doctor_mode=False
        ),
        payload={
            "silence_duration_sec": duration_sec,
            "anomaly_score": anomaly_score
        }
    )


def normal_activity_event():
    return BaseEvent(
        elder_id=ELDER_ID,
        type=EventType.ACOUSTIC_FEATURES,
        source=EventSource.ANDROID,
        consent=Consent(
            monitoring_on=True,
            audio_upload=False,
            doctor_mode=False
        ),
        payload={
            "energy_level": 0.25,
            "anomaly_score": 0.1
        }
    )


def sudden_noise_event():
    return BaseEvent(
        elder_id=ELDER_ID,
        type=EventType.ACOUSTIC_FEATURES,
        source=EventSource.ANDROID,
        consent=Consent(
            monitoring_on=True,
            audio_upload=False,
            doctor_mode=False
        ),
        payload={
            "energy_level": 0.95,
            "anomaly_score": 0.4
        }
    )


if __name__ == "__main__":
    print("=== Normal activity ===")
    print(normal_activity_event().to_dict())

    time.sleep(1)

    print("\n=== Sudden noise ===")
    print(sudden_noise_event().to_dict())

    time.sleep(1)

    print("\n=== Long silence (ALERT CASE) ===")
    print(silence_window_event(3600, 0.85).to_dict())
