#!/bin/sh
# script organize.sh
# organize file by given type in given folder

folder="$1"
file_type="$2"
if [[ -d "$folder" ]]
then
    final_dest="$folder"/"$file_type"
    mkdir -p "$final_dest"
    mv "$folder"/*."$file_type" "$final_dest"
    exit 0
else
  exit 252
fi
