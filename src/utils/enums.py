from enum import Enum


class Farm(Enum):
    """Represents the ``Farm`` module and its levels"""
    BASIC = 1
    ADVANCED = 2
    ELITE = 3
    ULTIMATE = 4
    SUPERIOR = 5


class Lab(Enum):
    """Represents the ``Lab`` module and its levels"""
    BASIC = 1
    ADVANCED = 2
    ELITE = 3
    ULTIMATE = 4
    SUPERIOR = 5


class AsteroidMin(Enum):
    """Represents the ``Asteroid Miner`` module and its levels"""
    BASIC = 1
    ADVANCED = 2
    ELITE = 3


class Trading(Enum):
    """Represents the ``Trading Station`` module and its levels"""
    BASIC = 1
    ELITE = 2
    SUPERIOR = 3
