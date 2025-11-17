import yaml
from yaml import Loader
from scripts.load_export import load_voice, load_walking, load_ambiance, export_sound
from scripts.transform import fade_in, volume, overlap_sound
from pydub import AudioSegment
from pydub.playback import play

stream = open("config.yaml", "r")
config = yaml.load(
    stream,
    Loader=Loader,
)

voice = load_voice(config)
walking = load_walking(config)
ambiance = load_ambiance(config)

voice = volume(voice, config["sounds"]["voice"].get("volume", 0))
walking = volume(walking, config["sounds"]["walking"].get("volume", 0))
ambiance = volume(ambiance, config["sounds"]["ambiance"].get("volume", 0))

walking = fade_in(walking, duration=9000)

overlap = overlap_sound(ambiance, [walking, voice])

export_sound(
    overlap,
    config,
    name="final_mix",
    format="mp3",
)

# play(overlap)
