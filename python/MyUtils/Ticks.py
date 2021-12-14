from datetime import datetime


def ticks(dt: datetime) -> float:
    return (dt - datetime(1, 1, 1)).total_seconds() * 10000000
