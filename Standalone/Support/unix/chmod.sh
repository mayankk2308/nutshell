#!/bin/sh
# script chmod.sh
# Make file executable

item="$1"
if [[ -f "${item}" ]]
then
  chmod +x "${item}"
  exit 0
else
  exit 252
fi
