#!/bin/bash
# Loads the X11 environment from the ~/.xinitrc if the user login into the TTY1 and if a X environment is not already started.

if [[ "$(tty)" == '/dev/tty1' ]]; then
    [[ -z "$(pgrep xinit)" ]] && [[ -e "${HOME}/.xinitrc" ]] && exec bash ${HOME}/.xinitrc || echo "[ERROR] '${HOME}/.xinitrc' does not exist."
fi
