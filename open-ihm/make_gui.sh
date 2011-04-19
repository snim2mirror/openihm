#!/bin/bash

cd gui/designs
for f in *.ui ; do 
	if [[ "${f/.ui/.py}"  -ot $f ]] ; then 
		echo pyuic4 $f -o "${f/.ui/.py}";
		pyuic4 $f -o "${f/.ui/.py}";
	fi
done
