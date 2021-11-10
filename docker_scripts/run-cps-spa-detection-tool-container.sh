# Stop and remove the previous docker container
CHECK_CONTAINERS=$(docker container ls | grep 'cps-spa-detection-tool-container')
if [ -n "$CHECK_CONTAINERS" ]; then
  echo "Stopping and removing existing container..."
  docker stop cps-spa-detection-tool-container > /dev/null
  docker rm cps-spa-detection-tool-container > /dev/null
fi

# Make results dir if it is needed
if [ ! -d "results" ];then
    mkdir results
fi

# Mount projects directory for local repo analysis
EXTRA_MOUNT=""
if [ -n "$1" ]; then
    if [ -d "$1" ]; then
        # The input argument should be an absolute path 
        EXTRA_MOUNT="--mount type=bind,source=$1,target=/home/user/repo-mining/projects"
    fi
fi

# Run a new docker container.
docker run -dit --name cps-spa-detection-tool-container \
--mount type=bind,source="$(pwd)/results",target=/home/user/repo-mining/results \
$EXTRA_MOUNT \
cps-spa-detection-tool
