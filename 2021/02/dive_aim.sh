#!/bin/bash
horisontal=0
vertical=0
aim=0

while read -r line;
do
    cmd=$(echo $line | awk '{print $1}')
    val=$(echo $line | awk '{print $2}')
    [ "$cmd" == "forward" ] && horisontal=$((horisontal+val)) && vertical=$((vertical+aim*val))
    [ "$cmd" == "down" ] && aim=$((aim+val))
    [ "$cmd" == "up" ] && aim=$((aim-val))
done < "input.txt"

echo $((horisontal*vertical))
