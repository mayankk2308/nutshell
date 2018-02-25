#!/bin/sh
# script copy.sh
# copy "item" to destination "dest"

item="$1"
destination="$2"
rsync -r "$item" "$destination"
