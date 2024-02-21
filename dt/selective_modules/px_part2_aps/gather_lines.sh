#!/bin/bash
set -e

declare -a StringArray=("rate.txt" "size.txt" "speed.txt" "timeout.txt" "unneeded.txt")

file_mwn="mwn.txt"
file_hcft="hcft.txt"

mwn="mwn"
hcft="hcf"

if [ -f "$file_mwn" ] ; then
  echo "$file_mwn exists already"
  rm "$file_mwn"
  touch "$file_mwn"
fi
if [ -f "$file_hcft" ] ; then
  echo "$file_hcft exists already"
  rm "$file_hcft"
  touch "$file_hcft"
fi

for file_input in "${StringArray[@]}"; do
  while IFS= read -r line
  do
    if [[ $line =~ $mwn ]]; then
      echo "$line" >> "$file_mwn"
    fi
  done < "$file_input"
done

for file_input in "${StringArray[@]}"; do
  while IFS= read -r line
  do
    if [[ $line =~ $hcft ]]; then
      echo "$line" >> "$file_hcft"
    fi
  done < "$file_input"
done
