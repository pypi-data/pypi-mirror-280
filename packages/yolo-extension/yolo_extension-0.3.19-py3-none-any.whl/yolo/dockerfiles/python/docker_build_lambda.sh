#!/bin/bash -e
readonly inject_build_info="${1}"

if [[ ! -f /build_cache/${DEPENDENCIES_SHA}.zip ]] || [[ "$REBUILD_DEPENDENCIES" == "1" ]]; then
    echo "rebuilding dependencies"
    rm -rf /build_cache/*
    mkdir /tmp/build
    /usr/local/bin/python3 -m pip install --no-input -r /dependencies/requirements.txt -t /tmp/build
    cd /tmp/build
    zip -X -r /build_cache/${DEPENDENCIES_SHA}.zip .
else
    echo "using cached dependencies; no rebuild"
fi
cd /src
rm -f /dist/lambda_function.zip
cp /build_cache/${DEPENDENCIES_SHA}.zip /dist/lambda_function.zip
if [[ "$EXCLUDE_PATTERNS" != "" ]]; then
    EXCLUDE="-x $EXCLUDE_PATTERNS/**"
fi
zip -X -r /dist/lambda_function.zip ${INCLUDE}

if [[ -n "${inject_build_info}" ]]; then
    cd /tmp
    echo "{\"VERSION_HASH\": \"${VERSION_HASH}\", \"BUILD_TIME\": \"${BUILD_TIME}\"}" > config.json
    zip -X -r /dist/lambda_function.zip config.json
fi
#if [[ ! -f /build_cache/${DEPENDENCIES_SHA}.zip ]] || [[ "$REBUILD_DEPENDENCIES" == "1" ]]; then
#    echo "rebuilding dependencies"
#    rm -rf /build_cache/*
#    mkdir /tmp/build
#    /usr/local/bin/python3 -m pip wheel --no-binary :all: -w /build_cache -r /dependencies/requirements.txt
#    sha1sum /dependencies/requirements.txt | cut -d " " -f 1 > /build_cache/cache_version.sha1
#else
#    echo "using cached dependencies; no rebuild"
#fi
#/usr/local/bin/python3 -m pip install -t /install --no-compile --no-index --find-links /build_cache -r /dependencies/requirements.txt
#cd /install && rm -f /dist/lambda_function.zip && zip -r /dist/lambda_function.zip ./*
#cd /src && zip -r /dist/lambda_function.zip ${INCLUDE}
#cd /tmp && echo "{\"VERSION_HASH\": \"${VERSION_HASH}\", \"BUILD_TIME\": \"${BUILD_TIME}\"}" > config.json && zip -r /dist/lambda_function.zip config.json
