# Build the new image from Dockerfile.cps-spa-detection-tool-studyOne
docker image build -t cps-spa-detection-tool-studyOne \
--build-arg LOCAL_UID="$(id -u)" --build-arg LOCAL_GID="$(id -g)" \
"$(pwd)" -f Dockerfile.cps-spa-detection-tool-studyOne
