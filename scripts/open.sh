#!/bin/sh
# script copy.sh
# open "item" with default OS application

item="$1"
file_location=`./scripts/find.sh "$item"`
open "$file_location"
