#!/bin/sh
# script find.sh
# finds given "filename" in current user directory (~)

filename="$1"
find ~ -iname "$filename" -print
