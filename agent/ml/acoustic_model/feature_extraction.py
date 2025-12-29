import random

def extract_audio_features():
    """
    Simulates on-device audio feature extraction
    """
    return {
        "energy": round(random.uniform(0.0, 1.0), 2),
        "zero_crossing_rate": round(random.uniform(0.0, 0.5), 2),
        "spectral_flux": round(random.uniform(0.0, 1.0), 2)
    }
