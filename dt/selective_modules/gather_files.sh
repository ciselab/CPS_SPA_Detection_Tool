#!/bin/bash
set -e

hash_code=$1
github_projects=$2
this_project_dir=$3

if [[ "$hash_code" != '' ]] && [[ "$github_projects" != '' ]] && [[ "$this_project_dir" != '' ]]; then
  base_project="${github_projects}"
  gh_repository="PX4"
  gh_project="PX4-Autopilot"
  project_dir="${base_project}/PX4-Autopilot"

  save_file_location="${this_project_dir}/dt/selective_modules/px_commit_results/"
  if [[ ! -d "$save_file_location" ]]; then
    echo "[gather_files] Save file directory does not yet exist..creating..location: ${save_file_location}"
    mkdir -p "$save_file_location" &
    wait
  fi

  save_file="${save_file_location}results_${hash_code}_px4.json"
  (cd "$project_dir" || exit; gh api "/repos/${gh_repository}/${gh_project}/commits/${hash_code}" > "$save_file")
else
  echo "Empty (hash_code, github_projects, or this_project_dir) input stopping."
fi
