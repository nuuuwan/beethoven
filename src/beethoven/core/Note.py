from dataclasses import dataclass

from beethoven.core.Time import Time


@dataclass
class Note:
    time: Time
    pitch: int
    duration: int
    volume: int
