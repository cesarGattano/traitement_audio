from pydub import AudioSegment


def load_sound(
    config: dict,
    name: str,
    format: str,
) -> AudioSegment:
    """Import an audio file named **name**.

    Args:
        config (dict): The configuration (config.yaml)
        name (str): The file name

    Raises:
        Exception: *path_raw* key not in **config**

    Returns:
        AudioSegment: The audio contained in the file
    """

    path = config["path"]["raw"]
    if path:
        return AudioSegment.from_file(path + "/" + name + "." + format, format=format)
    else:
        raise Exception("Missing field 'path_raw' in config.yaml")


def load_voice(config: dict) -> AudioSegment:
    """Import the audio of a voice

    Args:
        config (dict): The configuration (config.yaml)

    Returns:
        AudioSegment: The audio contained of the file voice
    """

    voice = config["sounds"]["voice"]
    return load_sound(config, voice["name"], voice["format"])
