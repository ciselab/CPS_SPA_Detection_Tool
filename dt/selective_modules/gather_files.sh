#!/bin/bash
set -e

hash_code=$1

if [[ "$hash_code" != '' ]]; then
  base_project="${HOME}/GitHub/"
  gh_repository="PX4"
  gh_project="PX4-Autopilot"
  project_dir="${base_project}/PX4-Autopilot"

  save_file="${base_project}CPS_SPA_Detection_Tool/dt/selective_modules/px_commit_results/results_${hash_code}_px4.json"
  (cd "$project_dir" || exit; gh api "/repos/${gh_repository}/${gh_project}/commits/${hash_code}" > "$save_file")
else
  echo "Empty hash_code input, stopping."
fi
