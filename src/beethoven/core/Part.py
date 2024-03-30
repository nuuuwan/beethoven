from dataclasses import dataclass

from beethoven.core.Note import Note


@dataclass
class Part:
    composition: object
    track: int
    channel: int
    program: int

    def __add__(self, other):
        if isinstance(other, Note):
            note = other
            self.composition.midi.addNote(
                self.track,
                self.channel,
                note.pitch.value,
                note.time.value,
                note.duration,
                note.volume,
            )
            return self

        raise ValueError("Can only add Note objects to Part objects")
