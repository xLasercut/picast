#!/bin/bash

function buildFrontend() {
    pushd ./client
    npm install
    npm run build
    popd
}

while getopts ":c: :h" opt; do
    case ${opt} in
        h )
            echo "Usage:"
            echo "    -h        Display help"
            echo "    -c        Name of container to build for building single container"
            exit 0
            ;;
        c )
            container=$OPTARG
            ;;
        \? )
            echo -e "${red}Invalid option: $OPTARG${end}" 1>&2
            exit 1
            ;;
        : )
            echo -e "${red}Invalid option: $OPTARG requires an argument${end}" 1>&2
            exit 1
            ;;
    esac
done
shift $((OPTIND -1))

if [[ -z $container ]]; then
    buildFrontend
    sudo docker-compose build
else
    if [[ $container = "picast-client" ]]; then
        buildFrontend
    fi
    sudo docker-compose build $container
fi
