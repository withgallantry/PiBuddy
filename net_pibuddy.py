#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os
import subprocess

try:
    subprocess.call('echo -n "RESET" | nc -u -w1 127.0.0.1 55355')
    print "Executed Reset"
except:
    print "Cannot execute"
