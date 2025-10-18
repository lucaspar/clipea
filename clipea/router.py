"""clipea
Base application logic
"""

import sys

from clipea import CONFIG, ENV, USAGE_FILE_PATH, commands, utils


def commands_router(user_prompt: str) -> None:
    """Executes the correct behavior depending on user input

    Args:
        user_prompt (str): user input
    """
    args: list[str] = user_prompt.split()
    if len(args) == 0:
        utils.say(utils.read_file(USAGE_FILE_PATH))
        sys.exit("No query specified")

    match args[0]:
        case "alias":
            commands.alias()
        case "env":
            utils.say(str(ENV))
        case "setup":
            commands.setup()
        case "-h" | "--help" | "help":
            utils.say(utils.read_file(USAGE_FILE_PATH))
        case _:
            commands.clipea_execute_prompt(
                user_prompt,
                llm_model_name=CONFIG.llm_model_name,
            )
