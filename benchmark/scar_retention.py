import random

def run(model):
    """
    Simulates scar retention — how well the AI avoids repeating mistakes.
    """
    score = round(random.uniform(0.30, 0.90), 2)
    print(f"[scar_retention] Score: {score}")
    return score
