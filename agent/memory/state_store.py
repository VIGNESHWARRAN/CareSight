from agent.memory.elder_state import ElderState

ELDER_STATES = {}

def get_elder_state(elder_id: str) -> ElderState:
    if elder_id not in ELDER_STATES:
        ELDER_STATES[elder_id] = ElderState(elder_id)
    return ELDER_STATES[elder_id]
