# Build the new image from Dockerfile.cps-spa-detection-tool
docker image build -t cps-spa-detection-tool \
$(pwd) -f Dockerfile.cps-spa-detection-tool
