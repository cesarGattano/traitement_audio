from pydub import AudioSegment

def walking_sound():
    pass

def overlap_sound(base: AudioSegment, sounds: list):
    mix = base
    for s in sounds:
        mix = mix.overlay(s)
    return mix


def volume():
    pass