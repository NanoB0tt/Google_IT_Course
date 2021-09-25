#!/bin/bash

echo "How many files do you want to create? "
read numfile
echo "Were do you want to create these files? "
read path
cd $path
i=0
while [ $i -lt $numfile ]; do
	echo "Enter the name of the file"
	read filename
	touch $filename
	((i+=1))
done
