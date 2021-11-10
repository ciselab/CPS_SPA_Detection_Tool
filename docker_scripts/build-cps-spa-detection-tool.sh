# Stop and remove the previous docker container
CHECK_CONTAINERS=$(docker container ls | grep 'cps-spa-detection-tool-container')
if [ -n "$CHECK_CONTAINERS" ]; then
  echo "Stopping and removing existing container..."
  docker stop cps-spa-detection-tool-container > /dev/null
  docker rm cps-spa-detection-tool-container > /dev/null
fi

# Remove previous docker image
CHECK_IMAGES=$(docker images | grep 'cps-spa-detection-tool')
if [ -n "$CHECK_IMAGES" ]; then
  docker rmi 'cps-spa-detection-tool'
fi

# Build the new image from Dockerfile.cps-spa-detection-tool
docker image build -t cps-spa-detection-tool \
$(pwd) -f Dockerfile.cps-spa-detection-tool
