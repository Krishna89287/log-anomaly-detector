import pytest

from log_anomaly.detect import detect_anomalies, mad, median


def test_median_and_mad():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert mad([1, 2, 3, 4, 5], 3) == 1


def test_spike_is_flagged():
    counts = [3, 2, 4, 3, 2, 3, 40, 3, 2, 4]
    results = detect_anomalies(counts)
    flagged = [r for r in results if r["is_anomaly"]]
    assert len(flagged) == 1
    assert flagged[0]["count"] == 40


def test_flat_series_has_no_anomalies():
    results = detect_anomalies([5, 5, 5, 5, 5])
    assert not any(r["is_anomaly"] for r in results)


def test_single_deviation_from_constant_flags():
    results = detect_anomalies([5, 5, 5, 5, 99])
    assert results[-1]["is_anomaly"] is True


def test_validation():
    with pytest.raises(ValueError):
        detect_anomalies([])
    with pytest.raises(ValueError):
        detect_anomalies([1, 2], threshold=0)
