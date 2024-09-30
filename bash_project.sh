#!/bin/bash
countdown() {
    local seconds=$1
    while [ $seconds -gt 0 ]; do
        echo -ne "Time left: $seconds seconds\033[0K\r"
        sleep 1
        ((seconds--))
    done
    echo "Time's up!"
}


read -p "Enter countdown time in seconds: " input

if ! [[ "$input" =~ ^[0-9]+$ ]]; then
    echo "Please enter a valid number."
    exit 1
fi

countdown $input
