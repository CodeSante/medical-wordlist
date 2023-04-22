#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

directory=$1
output_file="$directory/wordlist.txt"

if [ -f "$output_file" ]; then
  read -p "File \"$output_file\" already exists. Do you want to delete it? (y/N) " delete_file
  if [[ $delete_file =~ ^[Yy]$ ]]; then
    rm "$output_file"
  else
    exit 1
  fi
fi

cat "$directory"/*.txt | tr '[:upper:]' '[:lower:]' | sort -u > "$output_file"

echo "Word list created at \"$output_file\""