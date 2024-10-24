#!/bin/bash
OUTPUT=$1
echo " " > $OUTPUT
for planet in Sun Mercury  Venus Earth Mars Jupyter Saturn Uranus Neptune Pluto Moon
do 
    grep "/\* $planet" SolarSysData.h | awk '{print $1}'>> $OUTPUT
    grep -A6 "// $planet" SolarSysData.h | grep -v "// $planet" >> $OUTPUT
    echo " " >> $OUTPUT
done 