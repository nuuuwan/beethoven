from beethoven.core.Interval import Interval


class Scale:
    MAJOR = [
        Interval(0),
        Interval(2),
        Interval(4),
        Interval(5),
        Interval(7),
        Interval(9),
        Interval(11),
        Interval(12),
    ]

    MINOR = [
        Interval(0),
        Interval(2),
        Interval(3),
        Interval(5),
        Interval(7),
        Interval(8),
        Interval(10),
        Interval(12),
    ]

    WHOLE_TONE = [
        Interval(0),
        Interval(2),
        Interval(4),
        Interval(6),
        Interval(8),
        Interval(10),
        Interval(12),
    ]

    PENTATONIC = [
        Interval(0),
        Interval(2),
        Interval(4),
        Interval(7),
        Interval(9),
        Interval(12),
    ]
