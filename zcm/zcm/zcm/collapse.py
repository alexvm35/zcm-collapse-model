"""
Core collapse helpers for ZCM.

These functions implement simple, deterministic collapse operations using
radar bands. They are intentionally generic and do not contain any
database, storage or engine logic.
"""

from typing import Iterable, Sequence, List
from .radar_bands import RadarBand, make_radar_band, filter_by_radar_band


def collapse_by_radar_band(
    candidates: Sequence[float],
    center: float,
    radius: float,
) -> List[float]:
    """
    Deterministically collapse a list of numeric candidates into a smaller
    set using a single radar band.

    This is a minimal public example of the ZCM idea:
    - define a band around a reference value
    - keep only values that fall inside that band

    More advanced multi-band and harmonic logic lives in higher-level
    systems that are not part of this math-only library.
    """
    band: RadarBand = make_radar_band(center=center, radius=radius)
    return filter_by_radar_band(candidates, band)
