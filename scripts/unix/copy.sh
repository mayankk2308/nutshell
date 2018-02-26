#!/bin/sh
# script copy.sh
# copy "item" to destination "dest"

item="$1"
destination="$2"
if [[ -f "$item" && -d "$item" ]]
then
  rsync -r "$item" "$destination"
  exit 0
else
  exit 252
fi
