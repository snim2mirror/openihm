#!/bin/bash

cd gui/designs
for f in *.ui ; do pyuic4 $f -o "${f/.ui/.py}" ; done
