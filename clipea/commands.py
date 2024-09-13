"""Commands
Commands with a bit more logic than a few lines are stored there
"""

import json
import sys
from dataclasses import dataclass
from typing import TYPE_CHECKING

from llm import UnknownModelError

from clipea import CLIPEA_DIR, ENV, SYSTEM_PROMPT, cli

if TYPE_CHECKING:
    from pathlib import Path

    from llm import Model, Response

COMMAND_PREFIX: str = "🟢 "


@dataclass
class ClipeaConfig:
    """Configuration class for clipea"""

    llm_model_name: str = "gpt-4o"


config: ClipeaConfig = ClipeaConfig()


def setup() -> None:
    """Checks if `llm` has an openai key and prompt to change it or create one"""
    import llm.cli  # pylint: disable=import-outside-toplevel

    should_setup: bool = True
    path: Path = llm.cli.user_dir() / "keys.json"
    if path.exists():
        keys = json.loads(path.read_text())
        should_setup = "openai" not in keys

    if should_setup:
        print(
            "Get an OpenAI API key from: "
            "https://platform.openai.com/account/api-keys",
        )
    else:
        print("An OpenAI key is already set-up, proceed if you want to change it.")
    # trigger key setting (llm uses Click)
    llm.cli.keys_set()  # pylint: disable=no-value-for-parameter


def clipea_execute_prompt(user_prompt: str, llm_model_name: str) -> None:
    """Executes the user prompt with the given llm model.

    Structure all user input as so:

        <user_input>
        ~~~DATA~~~
        <data>

    Sends it to `llm`, stream the responses and prompt if the user wants
    to execute them. If zsh extension is enabled, it will be put into
    zsh's buffer

    Args:
        user_prompt (str): user command input
    """

    from clipea import clipea_llm  # pylint: disable=import-outside-toplevel

    try:
        model: Model = clipea_llm.init_llm(llm_model_name)
    except UnknownModelError as e:
        sys.exit(str(e))

    user_data: str = cli.get_input()
    response: Response = model.prompt(
        system=SYSTEM_PROMPT,
        prompt=user_prompt + (("\n~~~DATA~~~\n" + user_data) if user_data else ""),
    )
    clipea_llm.stream_commands(response, command_prefix=COMMAND_PREFIX)


def alias() -> None:
    """Gives zsh's alias (automatic command buffering) commands to the user"""
    shell: str = ENV["shell"]
    if shell in ("zsh", "-zsh"):
        command: str = f"alias '??'='source {CLIPEA_DIR}/clipea.zsh'"
        user_prompt: str = (
            f"Append this line to my {shell} startup file, \
            watching out for quotes and escaping, then explain how"
            f"to manually source it: {command}"
        )
        clipea_execute_prompt(user_prompt, llm_model_name=config.llm_model_name)
    if shell in ("bash", "-bash"):
        command = (
            "CLIPEA_HOME= # where you cloned this repo"
            "alias ??='source ${CLIPEA_HOME}/clipea/bash_wrapper.sh; clipea_wrapper'"
        )
        user_prompt = (
            f"Append this line to my {shell} startup file, \
            watching out for quotes and escaping, then explain how"
            f"to manually source it: {command}"
        )
        clipea_execute_prompt(user_prompt, llm_model_name=config.llm_model_name)
    else:
        print(
            f"`alias` feature is only for zsh and bash users. Current shell = {shell}",
        )
