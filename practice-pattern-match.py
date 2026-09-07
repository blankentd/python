##!/usr/bin/python

import os, shutil, sys, urllib.request, webbrowser, re 
import profile as profile

from datetime import datetime
from urllib.request import urlopen

url_path = ("adict.bcn.rd.hpicorp.net:88/cim/fmw/ipg-atlas_bcd/vulcan/wrl60-haswell_x86_64-dbg")

## ^ matches the start of the string
## \w matches the alphanumeric character in the string
## $ matches the end of the string
## \s creates a space in the line

pattern = re.match(r"^\w+", 'adict.bcn.rd.hpicorp.net-88') 
print (pattern)

#pattern = re.search(r"^\w+", url_path) 
#print (pattern)

## This searches the string starting at the beginning and returns all the alphanumeric characters
## until a non-alpha numeric character is reached 
#pattern = re.findall(r"^\w+", url_path) 
#print (pattern)

## This searches the string starting at the beginning splits the string into individual words
## Non alpha numeric characters in words are included as part of the word or, if by themselves, a word
#print (re.split(r'\s', 'adict bcn rd hpicorp net-88 -'))