class Interval:
    def __init__(self, x):
        if isinstance(x, str):
            self.value = Interval.parse(x)
        elif isinstance(x, int):
            self.value = x
        else:
            raise ValueError(f"Invalid interval: {x}")

    @staticmethod
    def parse(s):
        idx = {
            'Unison': 0,
            'Minor 2nd': 1,
            'Major 2nd': 2,
            'Minor 3rd': 3,
            'Major 3rd': 4,
            'Perfect 4th': 5,
            'Tritone': 6,
            'Perfect 5th': 7,
            'Minor 6th': 8,
            'Major 6th': 9,
            'Minor 7th': 10,
            'Major 7th': 11,
            'Octave': 12,
        }
        return idx[s]
