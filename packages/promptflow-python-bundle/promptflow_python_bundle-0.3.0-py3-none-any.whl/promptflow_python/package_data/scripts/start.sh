#!/bin/bash

BASEDIR=$(dirname "$0")
source $BASEDIR/auto_detect_env.sh

# stop services created by runsv and propagate SIGTERM to child jobs
sv_stop() {
    echo "$(date -uIns) - Stopping all runsv services"
    for s in $(ls -d /var/runit/*); do
        sv stop $s
    done
}

# register SIGTERM handler
trap sv_stop SIGTERM

# start services in background and wait all child jobs
if [[ $AZUREML_COMPUTE_TYPE == "Singularity" ]]; then
    # Singularity doesn't start process with root user,
    # so need sudo to start runsvdir and add -E to keep environment variables
    echo "$(date -uIns) - Starting runsvdir with sudo"
    sudo -E runsvdir /var/runit &
else
    echo "$(date -uIns) - Starting runsvdir"
    runsvdir /var/runit &
fi
wait
