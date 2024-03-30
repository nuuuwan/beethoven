# https://en.wikipedia.org/wiki/General_MIDI


class Instrument:
    class PIANO:
        ACOUSTIC_GRAND_PIANO = 0
        HARPSICHORD = 6

    class CHROMATIC_PERCUSSION:
        CELESTA = 8
        GLOCKENSPIEL = 9

    class ORGAN:
        CHURCH_ORGAN = 19

    class GUITAR:
        ACOUSTIC_GUITAR_NYLON = 24
        ACOUSTIC_GUITAR_STEEL = 25

    class BASS:
        ACOUSTIC_BASS = 32

    class STRINGS:
        VIOLIN = 40
        VIOLA = 41
        CELLO = 42
        CONTRABASS = 43
        TREMOLO_STRINGS = 44
        PIZZICATO_STRINGS = 45
        ORCHESTRAL_HARP = 46

    class ENSEMBLE:
        STRING_ENSEMBLE_1 = 48
        STRING_ENSEMBLE_2 = 49
        CHOIR_AAHS = 52
        SYNTH_STRINGS_1 = 50
        ORCHESTRA_HIT = 55

    class BRASS:
        TRUMPET = 56
        TROMBONE = 57
        TUBA = 58

    class REED:
        ALTO_SAX = 65
        OBOE = 68
        ENGLISH_HORN = 69
        BASSOON = 70
        CLARINET = 71

    class PIPE:
        PICCOLO = 72
        FLUTE = 73
        RECORDER = 74
        PAN_FLUTE = 75
        BLOWN_BOTTLE = 76
        SHAKUHACHI = 77
        WHISTLE = 78
        OCARINA = 79

    class SYNTH_PAD:
        NEW_AGE = 88
        WARM = 89

    class ETHNIC:
        SHAMISEN = 106
