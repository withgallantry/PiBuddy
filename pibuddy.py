#!/usr/bin/env python
# sudo apt-get install python-serial
#
# This file originates from Bluups PiBuddy Project
# Author: Bluup

from retroarchapi import RetroArchPythonApi

api = RetroArchPythonApi(retroarch_path='/opt/retropie/emulators/retroarch/bin/retroarch',settings_path='settings')
api.toggle_pause()
