#!/bin/bash -e

if [[ ! -f /build_cache/${DEPENDENCIES_SHA}.zip ]] || [[ "$REBUILD_DEPENDENCIES" == "1" ]]; then
    echo "rebuilding dependencies"
    rm -rf /build_cache/*
    mkdir /tmp/build
    /usr/local/bin/python3 -m pip wheel --no-binary :all: -w /build_cache -r /dependencies/requirements.txt
    sha1sum /dependencies/requirements.txt | cut -d " " -f 1 > /build_cache/cache_version.sha1
else
    echo "using cached dependencies; no rebuild"
fi
/usr/local/bin/python3 -m pip install -t /install --no-compile --no-index --find-links /build_cache -r /dependencies/requirements.txt
cd /install && rm -f /dist/lambda_function.zip && zip -r /dist/lambda_function.zip ./*
cd /src && zip -r /dist/lambda_function.zip ${INCLUDE}
cd /tmp && echo "{\"VERSION_HASH\": \"${VERSION_HASH}\", \"BUILD_TIME\": \"${BUILD_TIME}\"}" > config.json && zip -r /dist/lambda_function.zip config.json
