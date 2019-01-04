#!/bin/sh
# script spawn_file.sh
# create and open a new file in default application
# By default creates it in Desktop.
# Needs a check for spacing in arguments.

file_name="${1}"
spawn_location="${2}"
if [[ -z "${spawn_location}" ]]
then
  spawn_location=$HOME"/Desktop"
fi
absolute_path="${spawn_location}/${file_name}"
touch "${absolute_path}"
osascript -e "tell application \"Finder\" to open POSIX file \"${absolute_path}\""
