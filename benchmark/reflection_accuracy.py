import random

def run(model):
    """
    Simulates a reflection-accuracy test.
    In a real benchmark this would check whether the AI can describe
    why it produced a certain answer.  For now it just returns
    a pseudo-random score between 0 and 1.
    """
    score = round(random.uniform(0.35, 0.85), 2)
    print(f"[reflection_accuracy] Score: {score}")
    return score
