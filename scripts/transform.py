from pydub import AudioSegment


def overlap_sound(base: AudioSegment, sounds: list):
    """Overlay multiple audio segments onto a base audio segment."""
    mix = base
    for s in sounds:
        mix = mix.overlay(s)
    return mix


def volume(audio, db_adjustment):
    """Adjust the volume of the audio by a certain number of decibels."""
    if db_adjustment == 0:
        return audio
    
    adjusted = audio.apply_gain(db_adjustment)
    return adjusted

def fade_in(audio, duration=1000):
    """Apply fade in effect to audio."""
    return audio.fade_in(duration)