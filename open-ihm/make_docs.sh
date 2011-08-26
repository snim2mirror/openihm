#!/bin/sh

# TODO: Write a corresponding .bat file

echo "Generating RST files in directory rst/"

root=`pwd`

python scripts/generate_modules.py -f -s rst -d rst/  $root/data/mysql/connector $root/data/scripts
python scripts/generate_modules.py -f -s rst -d rst/  gui $root/gui/interface/images_rc $root/gui/designs/images_rc
python scripts/generate_modules.py -f -s rst -d rst/  inputs
python scripts/generate_modules.py -f -s rst -d rst/  outputs 

# Modules we have imported from elsewhere

python scripts/generate_modules.py -f -s rst -d rst/  includes

echo "Finished generating documention."
echo "Please re-create the documention in HTML."
echo "If you are using a UNIX system please run 'make clean && make html' from the command line."
echo "If you are using a Windows system please run make.bat."
