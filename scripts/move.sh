#!/bin/sh
# script move.sh
# move "item" to destination "dest"

item="$1"
destination="$2"
file_location=`./scripts/find.sh "$item"`
mv "$file_location" "$destination"
