#!/bin/bash

# This script (hardcode "warmpool.sh") is invoked by Singularity service which doesn't honor the entrypoint of image.
# Singularity warm pool needs to set environment variables (from client requests) before starting the service.
# It will prepare necessary environment variables and write to the file "envfile.sh" in the mounted directory.
# So wait until the file is ready and run the script to export environment variables.
envfile="/mnt/cloud/code/envfile.sh"
until [ -f "$envfile" ]
do
    echo "waiting for $envfile ready"
    sleep 2
done
echo "$envfile found, executing it"
source $envfile

# Start service with image entrypoint.
/service/scripts/start.sh
