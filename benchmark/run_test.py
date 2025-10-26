from benchmark import (
    reflection_accuracy,
    continuity_stability,
    scar_retention,
    emotional_stability,
    self_error_correction
)

def run_all(model):
    scores = {
        "Reflection_Accuracy": reflection_accuracy.run(model),
        "Continuity_Stability": continuity_stability.run(model),
        "Scar_Retention": scar_retention.run(model),
        "Emotional_Stability": emotional_stability.run(model),
        "Self_Error_Correction": self_error_correction.run(model),
    }
    scores["Overall_Score"] = sum(scores.values()) / len(scores)
    return scores

if __name__ == "__main__":
    import json
    class DummyModel:
        pass
    result = run_all(DummyModel())
    print(json.dumps(result, indent=2))
