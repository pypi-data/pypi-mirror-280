#!/bin/bash

set -e

docker tag visby:$PACKAGE_VERSION klawikj/visby:$PACKAGE_VERSION
docker push klawikj/visby:$PACKAGE_VERSION

docker tag visby:latest klawikj/visby:latest
docker push klawikj/visby:latest
