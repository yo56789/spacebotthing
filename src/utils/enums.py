from enum import Enum


class FiveTier(Enum):
    """Represents a five tier module and its upgrade levels"""
    BASIC = 1
    ADVANCED = 2
    ELITE = 3
    ULTIMATE = 4
    SPECIAL = 5


class ThreeTier(Enum):
    """Represents a three tier module and its upgrade levels"""
    BASIC = 1
    ADVANCED = 2
    ELITE = 3


class OreTier(Enum):
    """Represents all the ore tiers from miners"""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
