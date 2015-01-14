#!/bin/bash

function killTasks() {
    if [ -f run.lock ]
        then
            echo "Killing previous background tasks"
            while read line
            do
                kill $line
            done < run.lock
    fi
}

function runAll() {
    echo "Running lithe on port 8000"
    python lithe/main.py & 
    jobs -p > run.lock
}

if [ "$1" = "start" ]
    then
        killTasks
        runAll
        echo "All tasks run in the background, press enter if you did not return to your cli"
elif [ "$1" = "stop" ]
    then
        killTasks
        rm run.lock
elif [ "$1" = "restart" ]
    then
        killTasks
        rm run.lock
        runAll
        echo "All tasks run in the background, press enter if you did not return to your cli"
else
    echo "Please run with start|stop"
fi