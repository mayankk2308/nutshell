#!/bin/sh
# script bin_ver.sh
# give version of  binary
# Could include several options eg. current window, entire screen etc.
# Could allow user to set location to store screenshot

sc_name="${1}"

if [[ -z $sc_name ]]
then
  sc_name="untitled.png"
fi
screencapture $HOME/Desktop/"${sc_name}"
