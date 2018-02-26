#!/bin/sh
# script move.sh
# move "item" to destination "dest"

item="$1"
destination="$2"
if [[ -f "$destination" || -d "$destination" ]]
then
  exit 253
fi
mv "$item" "$destination"
