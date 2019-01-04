#!/bin/sh
# script open_terminal
# Opens terminal at desired location

terminal_location="${1}"
if [[ -d $terminal_location ]]
then
  osascript -e "tell application \"Terminal\" to do script \"cd '${terminal_location}' && clear\"">>/dev/null
  exit 0
else
  exit 252
fi
