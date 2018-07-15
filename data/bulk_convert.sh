#!/bin/bash

#There were a lot of files in .webm format. This script was to convert it from webm to mp4
#Usage: bash bulk_convert.sh path

if [ "$#" -lt 1 ]; then
	echo "There should be two arguments"
	exit 1
fi

path=$1
for FILE in $path/*.webm ; do
	OUTNAME=`basename "$FILE" .webm`.mp4
	ffmpeg -i $FILE -strict -2 $path$OUTNAME
	rm $FILE
done
