import yaml
from yaml import Loader
from scripts.load_export import load_voice, load_walking, load_ambiance
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

play(ambiance)
