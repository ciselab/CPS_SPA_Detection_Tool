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
For running the mining for remote repositories, this script can be executed without any input parameter.
However, to perform the mining process for local repositories, we should pass the directory of local repositories as the input argument:

`. docker_scripts/run-cps-spa-detection-tool-container.sh [local_repositories]`

__! Note:__ This input argument should be an absolute path.