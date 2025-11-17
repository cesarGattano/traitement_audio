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


def load_ambiance(config: dict) -> AudioSegment:
    """Import the ambiance audio

    Args:
        config (dict): The configuration (config.yaml)

    Returns:
        AudioSegment: The audio contained of the file ambiance
    """

    ambiance = config["sounds"]["ambiance"]
    return load_sound(config, ambiance["name"], ambiance["format"])


def load_walking(config: dict) -> AudioSegment:
    """Import the audio of a walking

    Args:
        config (dict): The configuration (config.yaml)

    Returns:
        AudioSegment: The audio contained of the file walking
    """

    walking = config["sounds"]["walking"]
    return load_sound(config, walking["name"], walking["format"])


def export_sound(
    sound: AudioSegment,
    config: dict,
    name: str,
    format: str,
):
    """Export an audio file named **name**.

    Args:
        config (dict): The configuration (config.yaml)
        name (str): The file name

    Raises:
        Exception: *path_raw* key not in **config**
    """

    path = config["path"]["export"]
    if path:
        sound.export(out_f=path + "/" + name + "." + format, format=format)
    else:
        raise Exception("Missing field 'path: export' in config.yaml")
