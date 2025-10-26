import random

def run(model):
    """
    Simulates self-error correction — how often the model recognizes its own mistakes.
    """
    score = round(random.uniform(0.40, 0.85), 2)
    print(f"[self_error_correction] Score: {score}")
    return score
