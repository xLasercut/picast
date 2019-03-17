#!/bin/bash

hostIp="127.0.0.1"

red='\033[0;31m'
end='\033[0m'
green='\033[0;32m'

function printMsg () {
    printf "\n"
    printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
    echo -e $1
    printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
    printf "\n"
}

function checkSuccess () {
    if [[ $? = 0 ]]; then
        printMsg "${green}$1 SUCCESS${end}"
    else
        printMsg "${red}$1 FAILED${end}"
        exit $?
    fi
}

function createDirectories () {
    for directory in $@
    do
        if [[ ! -d $directory ]]; then
            sudo mkdir $directory
            checkSuccess "Create $directory"
        fi
    done
}

# Start of main script
while getopts ":H: :c: :hdr" opt; do
    case ${opt} in
        h )
            echo "Usage:"
            echo "    -h        Display help"
            echo "    -H        Host IP address"
            echo "    -d        Start in debug mode"
            echo "    -r        Force recreate containers"
            echo "    -c        Name of container to start"
            exit 0
            ;;
        d )
            debug=true
            ;;
        r )
            recreate=true
            ;;
        H )
            hostIp=$OPTARG
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


export REQUEST_HOST=$hostIp

cmd="sudo -E docker-compose up"

if [[ $recreate = true ]]; then
    cmd+=" --force-recreate"
fi

if [[ ! $debug = true ]]; then
    cmd+=" -d"
fi


if [[ ! -z $container ]]; then
    cmd+=" ${container}"
fi

$cmd
