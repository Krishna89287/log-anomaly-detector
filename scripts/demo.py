"""Scan a minute-by-minute error count series and report the spikes."""
from __future__ import annotations

from log_anomaly.detect import detect_anomalies

# Errors per minute. Mostly low, with two spikes.
COUNTS = [3, 2, 4, 3, 2, 3, 4, 2, 3, 40, 3, 2, 4, 3, 55, 2, 3, 4, 2, 3]


def main() -> None:
    results = detect_anomalies(COUNTS, threshold=3.5)
    spikes = [r for r in results if r["is_anomaly"]]
    print(f"scanned {len(results)} minutes, {len(spikes)} anomalies")
    for r in spikes:
        print(f"  minute {r['index']:2}: count={r['count']:3}  score={r['score']}")


if __name__ == "__main__":
    main()
