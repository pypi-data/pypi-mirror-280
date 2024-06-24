#!/bin/bash

set -e

docker build -t visby:$PACKAGE_VERSION -t visby:latest --build-arg PACKAGE_VERSION -f docker/prod.dockerfile .
