#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os
import subprocess

try:
    p1 = subprocess.Popen(["echo", "-n", "RESET"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["nc", "-u", "-w1", "127.0.0.1", "55355"], stdin=p1.stdout)
    print "Executed Reset"
except:
    print "Cannot execute"
