def compute_risk(elder_state) -> float:
    if not elder_state.recent_silence_windows:
        return 0.0

    last_silence = elder_state.recent_silence_windows[-1]

    if last_silence > 3600:      # 1 hour
        return 0.8
    elif last_silence > 1800:    # 30 min
        return 0.5

    return 0.1
