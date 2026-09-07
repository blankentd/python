##!/usr/bin/python

## This script copies all the .txt files found within the directory named 'folder1' located within 
## a 'main' directory to a destination directory

import os, datetime, shutil, sys, time, urllib.request, glob
import profile as profile 

path = 'Y:\\Engineers\\timb' # This code defines the origin path of the .txt files
dest_path = "c:\\temp\\" # This code defines the destination path of for the .txt files
dirs = filter(os.path.isdir, os.listdir ( path ))

## Glob is used for filename pattern matching
for i in glob.glob(path + '\\folder1\\*.txt'): # Looks for any .txt files found in the folder1 directory
    shutil.copy(i, dest_path) # Copies the .txt files found in the path to the destination path
