#!/bin/sh
# script line_number.sh
# appends line numbers to a .txt file and outputs result to "output_file"

input_file="$1"
output_file="$2"
if [[ -d "$input_file" ]]
then
  exit 251
elif [[ ! -f "$input_file" ]]
then
  exit 252
elif [[ -f "$output_file" ]]
then
  exit 253
else
  nl "$input_file" > "$output_file"
fi
