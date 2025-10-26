import random

def run(model):
    """
    Simulates emotional stability — measures volatility after stress events.
    """
    score = round(random.uniform(0.50, 0.95), 2)
    print(f"[emotional_stability] Score: {score}")
    return score
