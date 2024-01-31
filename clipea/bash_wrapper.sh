#!/usr/bin/env bash
# This file can be moved to a different location in order to be sourced.

# check if executed or sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo -e "Error: Source the script instead of executing it:\n"
    echo "source $0"
    exit 1
fi

IS_DEBUG=${IS_DEBUG:-0}

function clipea_wrapper() {

    CLIPEA_HOME=${CLIPEA_HOME:-${XDG_DATA_HOME}/clipea}
    if [[ ! -d "${CLIPEA_HOME}" ]]; then
        echo "Error: CLIPEA_HOME not found: ${CLIPEA_HOME}"
        return 1
    fi

    if [[ ${IS_DEBUG} -eq 1 ]]; then
        echo "CLIPEA_HOME=${CLIPEA_HOME}"
    fi

    # Append current history to file, since we're
    #   going to clear the commands below. Just editing
    #   the history file directly does not
    #   respect the HISTTIMEFORMAT variable.
    history -a

    # run clipea
    args=("$@")
    if [[ ${IS_DEBUG} -eq 1 ]]; then
        poetry run -C "${CLIPEA_HOME}" "${CLIPEA_HOME}/clipea/clipea.sh" --debug "${args[@]}"
    else
        poetry run -C "${CLIPEA_HOME}" "${CLIPEA_HOME}/clipea/clipea.sh" "${args[@]}"
    fi

    if [[ ${IS_DEBUG} -eq 1 ]]; then
        echo "Reloading history..."
    fi
    history -r

}
