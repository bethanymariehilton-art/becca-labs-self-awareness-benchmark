def average(scores: dict) -> float:
    """Returns the mean of numeric values in a dict."""
    if not scores:
        return 0.0
    return round(sum(scores.values()) / len(scores), 2)
