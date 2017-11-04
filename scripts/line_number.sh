#!/bin/sh
# script line_number.sh
# appends line numbers to a .txt file

input_file="$1"
output_file="$2"
nl "$input_file" > "$output_file"
