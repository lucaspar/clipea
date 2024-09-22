#!/usr/bin/env bash
# This file can be moved to a different location in order to be sourced.

# check if executed or sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo -e "Error: Source the script instead of executing it:\n"
    echo "source $0"
    exit 1
fi

# this script is sourced, so manually change CLIPEA_SOURCE_DEBUG,
# or set it in as an environment variable before sourcing
CLIPEA_SOURCE_DEBUG=${CLIPEA_SOURCE_DEBUG:-0}

# make sure uv is available
if ! command -v uv &>/dev/null; then
    echo "Error: uv is not available. Install a package-manager agnostic version with:"
    echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
    return 1
fi

function clipea_wrapper() {

    CLIPEA_HOME=${CLIPEA_HOME:-${XDG_DATA_HOME}/clipea}
    if [[ ! -d "${CLIPEA_HOME}" ]]; then
        echo "Error: CLIPEA_HOME not found: ${CLIPEA_HOME}"
        return 1
    fi

    if [[ ${CLIPEA_SOURCE_DEBUG} -eq 1 ]]; then
        echo "CLIPEA_HOME=${CLIPEA_HOME}"
    fi

    # check if history is enabled
    hist_enabled="$(shopt -q -o history)"

    if [[ ${hist_enabled} -eq 0 ]]; then
        # Append current history to file, since we're
        #   going to clear the commands below. Just editing
        #   the history file directly does not
        #   respect the HISTTIMEFORMAT variable.
        history -a
    fi

    # run clipea
    args=("$@")
    if [[ ${CLIPEA_SOURCE_DEBUG} -eq 1 ]]; then
        echo "Running Clipea with args: ${args[*]}"
    fi
    if [[ ${CLIPEA_SOURCE_DEBUG} -eq 1 ]]; then
        uv --directory "${CLIPEA_HOME}" sync --quiet
        uv --directory "${CLIPEA_HOME}" run "${CLIPEA_HOME}/clipea/clipea.sh" --debug "${args[@]}"
    else
        uv --directory "${CLIPEA_HOME}" sync --quiet
        uv --directory "${CLIPEA_HOME}" run "${CLIPEA_HOME}/clipea/clipea.sh" "${args[@]}"
    fi

    if [[ ${hist_enabled} -eq 0 ]]; then
        # reload history with the executed command (if any)
        if [[ ${CLIPEA_SOURCE_DEBUG} -eq 1 ]]; then
            echo "Reloading history..."
        fi
        history -r
    fi

}
