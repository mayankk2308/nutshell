#!/bin/sh
# script organize.sh
# organize file by given type in given folder

folder="$1"
file_type="$2"
folder_location=`./scripts/find.sh "$folder"`

if [[ -d "$folder_location" ]]
then
    final_dest="$folder_location"/"$file_type"
    echo $final_dest
    mkdir "$final_dest"
    mv "$folder_location"/*."$file_type" "$final_dest"
fi
