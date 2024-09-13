"""Clipea application.

📎🟢 Like Clippy, but for the CLI. A blazing fast AI helper for your command line.
"""

import os
import sys
from dataclasses import dataclass
from pathlib import Path

from loguru import logger as log

from clipea import cli, utils

# set default log level to INFO
log.remove()
log.add(sys.stderr, level="INFO")


@dataclass
class ClipeaConfig:
    """Configuration class for clipea"""

    llm_model_name: str = "gpt-4o"
    command_prefix: str = "🟢 "


CLIPEA_DIR: Path = Path(__file__).parent
USAGE_FILE_PATH: Path = CLIPEA_DIR / "usage.txt"
SYSTEM_PROMPT_FILE: Path = utils.get_config_file_with_fallback(
    fallback=CLIPEA_DIR,
    appname="clipea",
    filename="system-prompt.txt",
)
ENV: dict[str, str] = {
    "shell": cli.get_current_shell(),
    "platform": sys.platform,
    "editor": os.getenv("EDITOR", "nano"),
}
log.trace(f"ENV: {ENV}")
SYSTEM_PROMPT: str = utils.read_file(SYSTEM_PROMPT_FILE) + str(ENV)
CONFIG: ClipeaConfig = ClipeaConfig()
