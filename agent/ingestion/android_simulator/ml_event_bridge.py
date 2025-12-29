from ml.acoustic_model.feature_extraction import extract_audio_features
from ml.acoustic_model.simple_classifier import compute_anomaly_score
from agent.events.base_event import BaseEvent, EventType, EventSource, Consent

ELDER_ID = "elder_001"


def generate_acoustic_event():
    features = extract_audio_features()
    anomaly = compute_anomaly_score(features)

    return BaseEvent(
        elder_id=ELDER_ID,
        type=EventType.ACOUSTIC_FEATURES,
        source=EventSource.CLOUD_INFER,
        consent=Consent(
            monitoring_on=True,
            audio_upload=False,
            doctor_mode=False
        ),
        payload={
            "energy_level": features["energy"],
            "spectral_flux": features["spectral_flux"],
            "anomaly_score": anomaly
        }
    )


if __name__ == "__main__":
    event = generate_acoustic_event()
    print(event.to_dict())
