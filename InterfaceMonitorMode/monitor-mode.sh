#!/usr/bin/env bash

# define bash options
set -e     # Abort script when a command exits with non-zero status
set -f     # Filename expansion (globbing) disabled
set -u     # Undefined variable forces an exit
# set -v   # Print each command to stdout before executing it
# set -x   # Similar to -v, but expands commands
# set -n   # Read commands in script, but do not execute them

# declare global magic variables
declare TIMESTAMP='+%Y-%m-%d_%H-%M-%S'
declare -r SCRIPT_VERSION='1.0.0'
declare -r SCRIPT_NAME=$( basename "$0" )
declare -r -a PACKAGES=('ip' 'iwconfig')
declare -r -i SUCCESS=0
declare -r -i NO_ARGS=84
declare -r -i BAD_ARGS=85
declare -r -i MISSING_ARGS=86
declare -r -i MISSING_PACKAGE=87

# global script functions
function trigger_error() {
  printf "[%s] \e[1m[ERROR]\e[22m: %s\n" "$( date +"$TIMESTAMP" )" "$1" 1>&2
  exit "$2"
}

function print_status() {
  printf "[%s] [%s]: %s\n" "$( date +"$TIMESTAMP" )" "$1" "$2"
}

function print_help() {
  printf "Usage: ./%s [options...] [-h] [-V] [-v]\n" "$SCRIPT_NAME"
  printf "\t-h : print this help\n"
  printf "\t-V : print script version\n"
  printf "\t-i : interface which should set to monitor mode\n"
}

# verify user parameters
if [ "$#" -eq 0 ]; then
  trigger_error 'No parameters provided to script' "$NO_ARGS"
fi

while getopts "hVi:" OPTION; do
  case "$OPTION" in
    h)
      print_help && exit "$SUCCESS";;
    V)
      print_status "INFO" "Version $SCRIPT_VERSION" && exit "$SUCCESS";;
    i)
      INTERFACE="$OPTARG";;
    *)
      trigger_error 'Wrong parameters provided to script' "$BAD_ARGS";;
  esac
done

if [ -z "$INTERFACE" ]; then
  trigger_error 'Empty value for interface' "$MISSING_ARGS"
fi

# check needed packages
for CISP in "${PACKAGES[@]}"; do
  command -v "$CISP" > /dev/null 2>&1 || {
    trigger_error "Package $CISP not found" "$MISSING_PACKAGE"
  }
done

# script functions
function main() {
  print_status "INFO" "$INTERFACE selected by user"
  print_status "INFO" "Set interface $INTERFACE down"
  ip link set "$INTERFACE" down
  print_status "INFO" "Set interface $INTERFACE mode monitor"
  iwconfig "$INTERFACE" mode monitor
  print_status "INFO" "Set interface $INTERFACE up"
  ip link set "$INTERFACE" up
  STATUS=$( iwconfig "$INTERFACE" | grep -i mode | awk '{print $4}' )
  print_status "INFO" "Interface $INTERFACE status is $STATUS"
}

# call main function
main

# exit 0
exit "$SUCCESS"
