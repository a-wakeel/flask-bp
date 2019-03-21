#!/usr/bin/env bash
# entrypoint script

set -e

# get CMD
CMD="$1"

if [[ -z ${CMD} ]]; then
    echo "* Run mode environment variable not set. Setting to shell."
    CMD="shell"
fi

if ! [[ "$(ls -A /workspace)" ]]; then
    echo "** flaskbp dev environment needs to have flaskbp git checkout bound to /workspace with -v option"
    exit 1
fi

cd /workspace
pip3 install -r requirements.txt

if [[ ${CMD} == "shell" ]]; then
    exec "/bin/bash"
elif [[ ${CMD} == "api" ]]; then
    exec flask run -h 0.0.0.0 -p 5000
else
    exec "$@"
fi