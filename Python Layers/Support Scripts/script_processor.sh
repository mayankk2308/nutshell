#!/bin/bash
# script_processor.sh
# Authors: Vedant Puri

# Text preferences
underline="$(tput smul)"
bold="$(tput bold)"
normal="$(tput sgr0)"

# Defaults
testing=false
working_dir="$(pwd)/"

script_to_string() {
  local IFS=$'\t'
  local file_path="${1}"
  local bash_string=""
  while read -r p
  do
    bash_string+="${p}\n"
  done <"${file_path}"
  echo -e "\n${bold}Your script as a single string is:${normal}"
  echo  "'"$bash_string"'"
  # echo
  if [[ "${testing}" == true ]]
  then
    echo -e "\n${bold}Script when created will look like:${normal}"
    echo -e $bash_string
  fi
}

# Parse script arguments
parse_args() {
  for arg in "${@}"
  do
    case "${arg}" in
      -r=*|--relative=*)
      local file_path="${working_dir}${arg#*=}"
      script_to_string "${file_path}"
      ;;
      -a=*|--absolute=*)
      script_to_string "${arg#*=}"
      ;;
      -t|--test)
      testing=true
      ;;
      *)
      echo "Invalid argument."
      ;;
    esac
  done
}

parse_args "${@}"
