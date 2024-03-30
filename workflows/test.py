import os

from beethoven import (Composition, Duration, Instrument, Note, Pitch, Scale,
                       Tempo, Time, Volume)

test_comp = Composition.new('test')
test_comp.set_tempo(Time(0), Tempo.ALLEGRO)

harp = test_comp.new_part(Instrument.STRINGS.ORCHESTRAL_HARP)
strings = test_comp.new_part(Instrument.ENSEMBLE.STRING_ENSEMBLE_1)
choral = test_comp.new_part(Instrument.ENSEMBLE.CHOIR_AAHS)
organ = test_comp.new_part(Instrument.ORGAN.CHURCH_ORGAN)

pitch0 = Pitch('C3')
for i, interval in enumerate(Scale.PENTATONIC):
    pitch = pitch0 + interval

    harp + Note(
        Time(i), pitch + 'Octave', Duration.CROTCHET, Volume.MEZZO_FORTE
    )
    strings + Note(
        Time(i), pitch + 'Minor 6th', Duration.CROTCHET, Volume.MEZZO_FORTE
    )
    choral + Note(
        Time(i), pitch + 'Major 3rd', Duration.CROTCHET, Volume.MEZZO_FORTE
    )
    organ + Note(
        Time(i), pitch - 'Octave', Duration.CROTCHET, Volume.MEZZO_FORTE
    )

os.startfile(test_comp.write())
