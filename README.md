# CPS SPA Detection Tool

## Setup
For portability and replicability of this tool, we use docker.
For easier docker setup, we provide two scripts for building docker image and running the docker container.

__! Note:__ For Windows, first install (and have it running) **_Docker for Windows_**. Then use **_Git Bash_** to run the following scripts.

### Docker image setup
Execute the following script for building the docker image:

`. docker_scripts/build-cps-spa-detection-tool.sh`

### Docker image container
The script `docker_scripts/run-cps-spa-detection-tool-container.sh` is created for this task. 
We need to pass the directory of the local repositories as the input argument:

`. docker_scripts/run-cps-spa-detection-tool-container.sh [local_repositories]`

For example `. docker_scripts/run-cps-spa-detection-tool-container.sh ~/projects/`

__! Note:__ This input argument should be an absolute path.

## Run
Then next step is to execute Docker: `docker exec -it cps-spa-detection-tool-container /bin/bash`,
the script can also be run immediately by doing instead `docker exec -it cps-spa-detection-tool-container /bin/bash "python dt/main.py"`.

### Run after executing
In order to run the script, run `main.py` (when using an IDE; make sure the working directory in the IDE is set to `CPS_SPA_Detection_Tool/dt`).
From the terminal (using Docker), this can be done by `python dt/main.py`.

## Notes
Running the script with a selection of project can be done by removing/commenting the projects from the dictionary in `dict_repo_list.py` called `projects`.

## Manual Validation
To generate the .md files for manual validation of this tool, run `results_analyses_to_md_csv.py`.
Currently, only a selection of files are being analysed.
