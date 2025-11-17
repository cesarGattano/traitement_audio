import yaml
from yaml import Loader
from scripts.load_export import load_voice

stream = open("config.yaml", "r")
config = yaml.load(
    stream,
    Loader=Loader,
)

voice = load_voice(config)

