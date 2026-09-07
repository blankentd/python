##!/usr/bin/python

## This script walks through directories found in a 'main' directory and copies .txt files
## found in each subdirectory if they exist to a 'destination' directory

import os, datetime, shutil, sys, time, urllib.request, glob
import profile as profile 

path = 'Y:\\Engineers\\timb' # This code defines the origin path of the .txt files
dest_path = "c:\\temp\\" # This code defines the destination path of for the .txt files
dirs = filter(os.path.isdir, os.listdir ( path ))

for path, dirs, files in os.walk(path):
    for y in files:
        if y.endswith('.txt'):
         shutil.copy(path + '\\' + y, dest_path) # Copies the .txt files found in the path to the destination path