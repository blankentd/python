##!/usr/bin/python

# This script downloads firmware files at a specified time using a timer

import os, datetime, shutil, sys, time, urllib.request 
import profile as profile

from datetime import datetime
from threading import Timer

x=datetime.today()
y=x.replace(day=x.day+10, hour=11, minute=1, second=0, microsecond=0) # Set when to start executing the script

delta_t=y-x
secs=delta_t.seconds+1

def download_files():
    url_path = "http://adict.bcn.rd.hpicorp.net:88/cim/fmw/ipg-atlas_bcd/vulcan/wrl60-haswell_x86_64-dbg"
    fw_folder = "180442"
    fmw_file = "vulcan-trunk-R180442-170919.unsigned.fmw"
    sh_file = "vulcan-trunk-R180442-170919.sh"

#    get_fmw_file = urllib.request.URLopener()
#    get_fmw_file.retrieve(url_path+ '/' + '/'+ fw_folder+ '/' + fmw_file, fmw_file)

    getShFile = urllib.request.URLopener()
    getShFile.retrieve(url_path+ '/' + '/'+ fw_folder+ '/' + sh_file, sh_file)

t = Timer(secs, download_files)
t.start() # Start the script
