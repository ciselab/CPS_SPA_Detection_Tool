# AP-Spotter: CPS SPA Detection Tool

## Setup
For portability and replicability of this tool, we use docker.

__! Note:__ Make sure [Docker is installed](https://docs.docker.com/engine/install/ubuntu/) before continuing.

__! Note:__ For Windows, first install (and have it running) **_Docker for Windows_**. Then use **_Git Bash_** to run the following scripts.

## Project List
The list of project to be run with AP-Spotter is available in `dt/dict_repo_list.py`.
In this file, the location of each project is noted. This method makes it easy to have multiple projects in different locations.
Each project can be in different locations, a default value is set (which is adjustable in this file), in case all the projects are in the same location.

For each project, the tool runs against a pre-stated selection of directories. This way specific directories, that might not of interest of the project, can be excluded from the run.

### Docker image setup
Execute the following script for building the docker image:

`./docker_scripts/build-cps-spa-detection-tool.sh`

### Docker image container
To create the Docker image container, run the script `docker_scripts/run-cps-spa-detection-tool-container.sh`, with the project name and pattern. 

`./docker_scripts/run-cps-spa-detection-tool-container.sh project_name pattern programming_language`

project_name: name of the project as stated in `dt/dict_repo_list.py`.
project_name: `hcft` for the Hard Coded Fine Tuning antipattern, `mwn` for the Magical Waiting Number antipattern.
programming_language: [optional] Default value is set for C++ projects (for manual setting, use `cpp`), for Python projects use `python`.

The container will stop and clean-up after finishing the run.
In the meantime, to check status, run the command `docker container ls`.

#### C++ projects
For example, for running against the Arduino_IRremote project in search for the Hard Coded Fine Tuning antipattern, run:

`./docker_scripts/run-cps-spa-detection-tool-container.sh Arduino_IRremote hcft`

#### Python projects
For example, for running against the pypilot project in search for the Magical Waiting Number antipattern, run:

`./docker_scripts/run-cps-spa-detection-tool-container.sh pypilot mwn python`

## Manual Validation
To generate the .md files for manual validation of this tool, run `results_analyses_to_md_csv.py`.

To be updated:
In this file (`results_analyses_to_md_csv.py`), adjust `list_analyse_files` in the `main` function to contain the project up for manual validation.
The path to the project also needs to be updated in this file under `file_path`.

After the .md files have been generated, `analysis_cleanup.py` needs to be run.

## Development information
Python 3.9 is used in this project.

