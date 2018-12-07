#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os
from retroarchapi import RetroArchPythonApi

def getRetroarchPid():
    return os.popen('pidof retroarch').read()

# [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['retroarch']]
# api.toggle_pause()
retroarchPid = getRetroarchPid()

api = RetroArchPythonApi(retroarch_pid=retroarchPid,settings_path='settings')