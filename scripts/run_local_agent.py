"""
Local runner for CareSight Agent
--------------------------------
This script simulates incoming events and feeds them to the agent.
Run this during demo.
"""

from agent.app import on_event
from agent.events.base_event import (
    BaseEvent,
    EventType,
    EventSource,
    Consent
)


def generate_test_silence_event():
    """
    Simulates a long silence event from elderly phone
    """
    return BaseEvent(
        elder_id="elder_001",
        type=EventType.SILENCE_WINDOW,
        source=EventSource.ANDROID,
        consent=Consent(
            monitoring_on=True,
            audio_upload=False,
            doctor_mode=False
        ),
        payload={
            "silence_duration_sec": 3600,  # 1 hour silence
            "anomaly_score": 0.85
        }
    )


def generate_normal_activity_event():
    """
    Simulates normal background activity
    """
    return BaseEvent(
        elder_id="elder_001",
        type=EventType.ACOUSTIC_FEATURES,
        source=EventSource.ANDROID,
        consent=Consent(
            monitoring_on=True,
            audio_upload=False,
            doctor_mode=False
        ),
        payload={
            "energy_level": 0.3,
            "anomaly_score": 0.1
        }
    )


if __name__ == "__main__":
    print("\n==============================")
    print(" CareSight Local Agent Runner ")
    print("==============================\n")

    print(">>> Sending NORMAL activity event (should NOT alert)")
    normal_event = generate_normal_activity_event()
    on_event(normal_event)

    print("\n>>> Sending SILENCE event (should ALERT)")
    silence_event = generate_test_silence_event()
    on_event(silence_event)

    print("\n>>> Demo complete\n")
