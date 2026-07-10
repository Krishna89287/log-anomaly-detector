from __future__ import annotations

_LARGE_SCORE = 1e6


def median(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2.0


def mad(values: list[float], center: float) -> float:
    """Median absolute deviation, a spread measure that ignores outliers."""
    return median([abs(v - center) for v in values])


def detect_anomalies(counts: list[float], threshold: float = 3.5) -> list[dict]:
    """Flag points whose modified z-score exceeds the threshold.

    The modified z-score (Iglewicz and Hoaglin) is built on the median and MAD,
    so a single huge spike does not hide the rest the way a mean and standard
    deviation would. 3.5 is the usual cutoff.
    """
    if not counts:
        raise ValueError("counts must not be empty")
    if threshold <= 0:
        raise ValueError("threshold must be positive")

    med = median(counts)
    spread = mad(counts, med)

    results = []
    for i, value in enumerate(counts):
        if spread > 0:
            score = 0.6745 * (value - med) / spread
        elif value == med:
            score = 0.0
        else:
            score = _LARGE_SCORE if value > med else -_LARGE_SCORE
        results.append({
            "index": i,
            "count": value,
            "score": round(score, 3) if abs(score) < _LARGE_SCORE else score,
            "is_anomaly": abs(score) >= threshold,
        })
    return results
