"""Utils
utils for the clipea application
"""

from pathlib import Path
from typing import AnyStr


def anystr_force_str(value: AnyStr) -> str:
    """Takes any AnyStr and gives back str

    Args:
        value (AnyStr)

    Returns:
        str: AnyStr's bytes decoded to str or it's str
    """
    if isinstance(value, bytes):
        return value.decode("utf-8")
    if isinstance(value, bytearray):
        return bytes(value).decode("utf-8")
    if isinstance(value, memoryview):
        return value.tobytes().decode("utf-8")
    if isinstance(value, str):
        return value
    raise TypeError(f"Unsupported type for anystr_force_str: {type(value)}")


def read_file(file_path: Path) -> str:
    """Reads a file as utf-8.

    Args:
        file_path

    Returns:
        str: file's content
    """
    assert isinstance(file_path, Path), "file_path must be a Path object"
    with file_path.open(encoding="utf-8") as fp:
        return anystr_force_str(fp.read())


def get_config_file_with_fallback(
    fallback: Path,
    appname: str,
    filename: str,
    home: Path | None = None,
) -> Path:
    """Returns opinionated config file path

    Args:
        home:       user's home
        fallback:   fallback in case the file doesn't exist
        appname:    your app name
        filename:   file you're trying to get

    Returns:
        Path: {home}/.config/{appname}/{filename} if it exists; else
            {fallback}/{filename}
    """
    if home is None:
        home = Path.home()
    assert isinstance(home, Path), "home must be a Path object"
    assert isinstance(fallback, Path), "fallback must be a Path object"
    assert isinstance(appname, str), "appname must be a string"
    assert isinstance(filename, str), "filename must be a string"
    config_path_obj: Path
    if (config_path_obj := home / ".config" / appname / filename).exists():
        return config_path_obj
    return fallback / filename


def say(message: str, *, prefix: bool | str = "", **kwargs) -> None:
    """Wrapper for user messages."""
    if prefix:
        print(f"{prefix}{message}", **kwargs)
    else:
        print(message, **kwargs)


def write_to_file(file_path: Path, content: AnyStr, mode: str = "w") -> None:
    """Write to file

    Args:
        file_path:  path to the file
        content:    content to write as bytes or str
        mode:       mode to open the file in
    """
    assert isinstance(file_path, Path), "file_path must be a Path object"
    with file_path.open(mode=mode, encoding="utf-8") as fp:
        fp.write(content)
