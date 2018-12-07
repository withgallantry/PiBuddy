#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os
import subprocess
from bluetooth.ble import DiscoveryService
devices = service.discover(2)

for address, name in devices.items():
    print("name: {}, address: {}".format(name, address))
# [ERROR] 		LOAD_STATE
# [ERROR] 		SAVE_STATE
#[ERROR] 		LOAD_STATE
#[ERROR] 		SAVE_STATE
#[ERROR]        MENU_TOGGLE

def executeCommand(command):
    try:
        p1 = subprocess.Popen(["echo", "-n", command], stdout=subprocess.PIPE)
        p2 = subprocess.Popen(["nc", "-u", "-w1", "127.0.0.1", "55355"], stdin=p1.stdout)
        p1.stdout.close()
        p2.stdout.close()
        print "Executed Reset"
    except:
        print "Cannot execute"
