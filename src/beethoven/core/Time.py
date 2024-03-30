from dataclasses import dataclass

from beethoven.core.Duration import Duration


@dataclass
class Time:
    value: int

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.value + other.value)
        if isinstance(other, int):
            return Time(self.value + other)

        if isinstance(other, float):
            return Time(self.value + other)
        if isinstance(other, Duration):
            return Time(self.value + other.value)

        raise TypeError(f"Invalid other: {other} ({type(other)})")

    def __iadd__(self, other):
        return self + other
