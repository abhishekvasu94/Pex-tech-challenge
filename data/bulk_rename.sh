#!/bin/bash

#A lot of the files' names were not in English. This converted all the file names to a readable format
#Usage: bash bulk_rename.sh path extension

if [ "$#" -lt 2 ]; then
	echo "There should be two arguments"
	exit 1
fi

path=$1
ext=$2
for FILE in $path/*.$ext ; do
	new=$(printf $path"/%03d."$ext "$count")
	mv -i -- "$FILE" "$new"
	let count=$count+1
	echo $FILE
done
