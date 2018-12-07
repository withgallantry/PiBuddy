#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os
from retroarchapi import RetroArchPythonApi

def getRetroarchPid():
    return os.popen('pidof retroarch').read().splitlines()[0]

# [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['retroarch']]
# api.toggle_pause()
retroarchPid = getRetroarchPid()

# print retroarchPid

# _process_stdin = open(os.path.join('/proc', str(retroarchPid), 'fd', '0'), 'a')
# print _process_stdin

# try:
#     _process_stdin.write('checkalive\n')
#     print "Worked"
# except:
#     print "Didn't work"

api = RetroArchPythonApi(retroarch_pid=retroarchPid,settings_path='settings')
# api.toggle_pause()