# Make results dir if it is needed
if [ ! -d "results" ];then
    mkdir results
fi

# Run a new docker container.
docker run --rm -dit \
--mount type=bind,source="$(pwd)/results",target=/home/user/cps-spa-detection-tool/results \
--mount type=bind,source="$HOME/projects",target=/home/user/projects \
-u "$(id -u)":"$(id -g)" \
cps-spa-detection-tool-studyone "$@"
