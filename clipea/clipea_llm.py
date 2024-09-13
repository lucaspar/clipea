"""LLM
Interactions with `llm` python library
"""

import os
import sys
from pathlib import Path

import llm
import llm.cli
from loguru import logger as log

import clipea.cli
from clipea import ENV, utils


def init_llm(llm_model: str = "") -> llm.Model:
    """Initialize base llm library with user's `llm_model`
    Args:
        llm_model:  LLM model name (ex: "gpt-4o").
    Returns:
        llm.Model
    """
    model = llm.get_model(llm_model)

    if model.needs_key:
        model.key = llm.get_key("", model.needs_key, model.key_env_var)
    return model


def stream_commands(response: llm.Response, command_prefix: str = "") -> None:
    """Streams llm response which returns shell commands
    The processing is done internally with a nested function `process_command`
    A command is considered valid if it starts with '$ ' and is a full line of answer

    Args:
        response:       LLM's answer to user's prompt
        command_prefix: What to write before streaming the commands. Defaults to "".
    """
    command: str = ""
    output_file_str: str | None = os.getenv("CLIPEA_CMD_OUTPUT_FILE")
    output_file: Path | None = Path(output_file_str) if output_file_str else None
    approved_cmd_list: str = ""
    new_line_pos: int

    def process_command() -> None:
        nonlocal command, approved_cmd_list, new_line_pos

        cmd_unapproved: str = (
            command[2:new_line_pos] if new_line_pos > 0 else command[2:]
        )
        command = command[new_line_pos + 1 :]

        # if in an interactive shell, prompt the user
        # for changes then run the command once approved.
        cmd_executed = None
        if sys.stdin.isatty():
            cmd_executed = clipea.cli.execute_after_approval(
                cmd_unapproved,
                shell=ENV["shell"],
            )
        if output_file is not None:
            cmd_to_add: str = cmd_unapproved
            if sys.stdin.isatty():
                if not cmd_executed:
                    return  # no command was approved and executed
                cmd_to_add = cmd_executed
            log.debug("Adding to command list: ", cmd_to_add)
            approved_cmd_list += cmd_to_add + os.linesep

    print(command_prefix, end="")
    for chunk in response:
        print(chunk, end="", flush=True)
        command += chunk

        if (new_line_pos := command.find(os.linesep)) == -1:
            continue
        if command.startswith("$ "):
            process_command()
        else:
            command = ""

    # llm CLI put a line feed manually to it's response, but not it's library
    # We have to do this to manage the case where the model returns a
    # non-linefeed terminated string.
    # It also explains why there is a capturing nested function `process_command`
    if command.startswith("$ "):
        print()
        process_command()

    if output_file:
        cmd_lines = approved_cmd_list.rstrip(os.linesep).split(os.linesep)
        cmd_lines = [cmd for cmd in cmd_lines if cmd]  # remove empty lines
        log.debug(f"Writing {len(cmd_lines)} lines to {output_file}")
        utils.write_to_file(
            output_file,
            ";".join(
                cmd_lines,
            )
            + os.linesep,
        )
