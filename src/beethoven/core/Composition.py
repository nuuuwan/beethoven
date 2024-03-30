import os
from dataclasses import dataclass

from midiutil import MIDIFile
from utils import Log

from beethoven.core.Part import Part
from beethoven.core.Time import Time

log = Log('Composition')


@dataclass
class Composition:
    title: str
    midi: MIDIFile
    parts: list[Part]

    @staticmethod
    def new(title: str):
        midi = MIDIFile(
            numTracks=32,
            # If adjust_origin is True the library will find the earliest event
            # in all the tracks and shift all events so that that time is t=0.
            adjust_origin=False,
        )
        return Composition(title, midi, [])

    def set_tempo(self, time: Time, tempo: int):
        self.midi.addTempo(0, time.value, tempo)

    def new_part(self, program: int, time: Time = None):
        if time is None:
            time = Time(0)
        track = len(self.parts)
        channel = track
        part = Part(self, track, channel, program)
        self.midi.addProgramChange(track, channel, time.value, program)
        self.parts.append(part)
        return part

    def write(self):
        midi_path = os.path.join('midi', f"{self.title}.mid")
        with open(midi_path, "wb") as output_file:
            self.midi.writeFile(output_file)
            log.info(f'Wrote {midi_path}')
        return midi_path
