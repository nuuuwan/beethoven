from beethoven.core.Interval import Interval


class Pitch:
    def __init__(self, x):
        if isinstance(x, str):
            self.value = Pitch.parse(x)
        elif isinstance(x, int):
            self.value = x
        else:
            raise ValueError(f"Invalid pitch: {x}")

    @staticmethod
    def parse(s):
        letter = s[:-1]
        octave = int(s[-1])

        letter_to_value = {
            'C': 0,
            'C#': 1,
            'Db': 1,
            'D': 2,
            'D#': 3,
            'Eb': 3,
            'E': 4,
            'Fb': 4,
            'E#': 5,
            'F': 5,
            'F#': 6,
            'Gb': 6,
            'G': 7,
            'G#': 8,
            'Ab': 8,
            'A': 9,
            'A#': 10,
            'Bb': 10,
            'B': 11,
            'Cb': 11,
            'B#': 12,
        }
        letter_value = letter_to_value[letter]
        return letter_value + (1 + octave) * 12

    def __add__(self, other):
        if isinstance(other, int):
            return Pitch(self.value + other)

        if isinstance(other, Interval):
            return Pitch(self.value + other.value)

        if isinstance(other, str):
            return Pitch(self.value + Interval.parse(other))

        raise ValueError(
            "Can only add int, Interval or str objects" + " to Pitch objects"
        )

    def __sub__(self, other):
        if isinstance(other, int):
            return Pitch(self.value - other)

        if isinstance(other, Interval):
            return Pitch(self.value - other.value)

        if isinstance(other, str):
            return Pitch(self.value - Interval.parse(other))

        raise ValueError(
            "Can only subtract int, Interval or str objects"
            + " from Pitch objects"
        )
