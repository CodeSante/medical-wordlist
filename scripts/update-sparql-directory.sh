#!/bin/bash

usage() {
  echo "Usage: $0 [-d directory]" 1>&2;
  exit 1;
}

while getopts ":d:" opt; do
  case ${opt} in
    d ) directory=$OPTARG;;
    * ) usage;;
  esac
done
shift $((OPTIND-1))

if [ -z "$directory" ]; then
  usage
fi

if [ ! -d "$directory" ]; then
  echo "Error: Directory $directory not found" >&2
  exit 1
fi

for file in "$directory"/*; do
  if [ -f "$file" ]; then
    python3 launch-sparql-query.py "$file"
  fi
done
