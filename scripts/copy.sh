#!/bin/sh
# script copy.sh
# copy "item" to destination "dest"

item="$1"
destination="$2"
file_location=`./scripts/find.sh "$item"`
rsync -r "$file_location" "$destination"
