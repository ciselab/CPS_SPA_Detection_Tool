#!/bin/bash
set -e

hash_code=$1
dir_project=$2

if [[ "$hash_code" != '' ]] && [[ "$dir_project" != '' ]]; then
  echo "[SB] dir: "$dir_project
  echo "[SB] hash: "$hash_code

  echo "Checkout: undo removals."
  (cd "$dir_project" || exit; git checkout .) &
  wait
  echo "Checkout branch."
  (cd "$dir_project" || exit; git checkout "$hash_code") &
  wait
else
  echo "Empty hash or directory input, stopping."
fi
