def compute_anomaly_score(features: dict) -> float:
    """
    Simple rule-based anomaly scoring
    """
    energy = features["energy"]

    if energy < 0.05:
        return 0.9  # silence anomaly
    elif energy > 0.9:
        return 0.6  # loud noise
    else:
        return 0.1  # normal
