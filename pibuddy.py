#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os

def getRetroarchPid():
    return os.popen('pidof retroarch').read().splitlines()[0]


retroarchPid = getRetroarchPid()

print retroarchPid

running = False

try:
    _process_stdin = open(os.path.join('/proc', str(retroarchPid), 'fd', '0'), 'a')
    _process_stdin.write('checkalive\n')
    running = True
    print "Retroarch alive"
except:
    print "Didn't work"

if running:
    _process_stdin.write('PAUSE_TOGGLE\n')
    print "Toggle Pause"

    # api = RetroArchPythonApi(retroarch_pid=retroarchPid,settings_path='settings')
    # api.toggle_pause()
