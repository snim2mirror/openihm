#!/bin/sh

# TODO: Write a corresponding .bat file

echo "Generating RST files in directory rst/"

root=`pwd`/src/openihm

python scripts/generate_modules.py -f -s rst -d rst/  $root/data $root/data/scripts
python scripts/generate_modules.py -f -s rst -d rst/  $root/gui $root/gui/interface/images_rc $root/gui/designs/images_rc
python scripts/generate_modules.py -f -s rst -d rst/  $root/inputs
python scripts/generate_modules.py -f -s rst -d rst/  $root/outputs 

# Test cases

python scripts/generate_modules.py -f -s rst -d rst/  tests 

# Modules we have imported from elsewhere

python scripts/generate_modules.py -f -s rst -d rst/  $root/includes $root/includes/mysql/ $root/includes/mysql/connector

echo "Finished generating documention."
echo "Please re-create the documention in HTML."
echo "If you are using a UNIX system please run 'make clean && make html' from the command line."
echo "If you are using a Windows system please run make.bat."
