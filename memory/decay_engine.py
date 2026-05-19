import time

def apply_decay(memory):

    current_time = time.time()

    elapsed = current_time - memory.timestamp

    decay_factor = 0.00001

    memory.strength *= (1 - decay_factor * elapsed)

    if memory.strength < 0:
        memory.strength = 0

    return memory
