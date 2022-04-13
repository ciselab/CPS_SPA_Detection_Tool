# Build the new image from Dockerfile.cps-spa-detection-tool
docker image build -t cps-spa-detection-tool \
--build-arg LOCAL_UID="$(id -u)" --build-arg LOCAL_GID="$(id -g)" \
$(pwd) -f Dockerfile.cps-spa-detection-tool
