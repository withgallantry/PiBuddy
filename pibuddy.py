#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup
import os
from retroarchapi import RetroArchPythonApi

api = RetroArchPythonApi(retroarch_path='/opt/retropie/emulators/retroarch/bin/retroarch',settings_path='settings')


def getpid(process_name):
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]

# [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['retroarch']]
# api.toggle_pause()
print(getpid('retroarch'))