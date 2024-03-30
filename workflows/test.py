import os
import random

from beethoven import (Composition, Duration, Instrument, Interval, Note,
                       Pitch, Tempo, Time, Volume)

test_comp = Composition.new('test')
test_comp.set_tempo(Time(0), Tempo.ANDANTE)


motif1 = [
    (Interval(-5), Duration.CROTCHET),
    (Interval(0), Duration.CROTCHET),
    (Interval(2), Duration.CROTCHET),
    (Interval(4), Duration.CROTCHET),
]
motif_duration = sum(duration for __, duration in motif1)
pitch00 = Pitch(random.randint(50, 56))

for part, pitch_delta in [
    (test_comp.new_part(Instrument.STRINGS.ORCHESTRAL_HARP), 12),
    # voices
    (test_comp.new_part(Instrument.ENSEMBLE.CHOIR_AAHS), 12),
    (test_comp.new_part(Instrument.ENSEMBLE.CHOIR_AAHS), 0),
    (test_comp.new_part(Instrument.ENSEMBLE.CHOIR_AAHS), 0),
    (test_comp.new_part(Instrument.ENSEMBLE.CHOIR_AAHS), -12),
    # organ
    (test_comp.new_part(Instrument.ORGAN.CHURCH_ORGAN), 0),
    (test_comp.new_part(Instrument.ORGAN.CHURCH_ORGAN), 0),
    (test_comp.new_part(Instrument.ORGAN.CHURCH_ORGAN), -12),
]:
    pitch0 = pitch00 + pitch_delta
    time = Time(0)
    while time.value < 4 * 16:
        k = random.choice([0.5, 1, 1, 2])

        if random.random() < 0.5:
            time = time + k * motif_duration

        motif1a = motif1.copy()
        # permute
        if random.random() < 0.5:
            motif1a.reverse()

            if random.random() < 0.5:
                random.shuffle(motif1a)

        for interval, duration0 in motif1a:
            duration = duration0 * k
            note = Note(time, pitch0 + interval, duration, Volume.FORTE)
            part + note
            time = time + duration


os.startfile(test_comp.write())
