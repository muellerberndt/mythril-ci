# Mythril Continuous Integration Docker Image

This repository contains a Dockerfile which will be used in future by Circle CI / Gitlab or by any CI/CD applications to test the solidity codes.

# General Overview about this Docker Image

- This image is created out of base Ubuntu 16.04 Image
- Includes common software dependencies, Python 3.6 latest version, Pip and Mythril
- Includes script `processor.py` which help run the tests of solidity files

# Docker Image Repository

- Docker Image is publicly available at https://hub.docker.com/r/sharathkumaranbu/mythril-ci/

- Git repository of Docker Image: https://github.com/sharathkumaranbu/mythril-ci

- Above image is built using `Automated Build` option in Docker. Hence any new commit to this git repository will trigger rebuilding of the docker image.

- Dockerfile itself has sufficient comments to describe about why each step is being used

# Updating the Docker Image

- In case if you like to Update the Docker image which I have built, Please follow the below steps.

- If you would like to add something on top of the existing image, In the Dockerfile use the below statement and keep building on top of it.

```
FROM sharathkumaranbu/mythril-ci
```

- If you would like to make some changes in the existing image itself, Please feel free to fork the repository and make changes in your version of `Dockerfile`.

- After making your changes, there are two ways to publish your Docker image to Dockerhub.

1. Build Docker image locally and push it to registry using `docker push`
2. Set up a automated build from Git repository which hosts this Dockerfile
