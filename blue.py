import pexpect
from subprocess import Popen
import time
import subprocess


class BLE:
    def discover(self):
        proc = Popen(['sudo', 'timeout', '5s', 'hcitool', 'lescan'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        lines = proc.stdout.readlines()
        print lines

    def connect(self, mac_str, random=1):
        if random == 0:
            output = Popen(['sudo', 'hcitool', 'lecc', mac_str])
        elif random == 1:
            output = Popen(['sudo', 'hcitool', 'lecc', '--random', mac_str])
        print output
        time.sleep(1)
        con = pexpect.spawn('sudo gatttool -b ' + mac_str + ' -I')
        con.expect('\[LE\]>', timeout=600)
        con.sendline('connect')
        con.expect('\[LE\]>', timeout=600)

    def writeCmd(self, handle, command):
        con.sendline('char-write-cmd ' + handle + command)
        con.expect('\[LE\]>', timeout=600)

    def disconnect(self):
        con.sendline('disconnect')
        con.expect('\[LE\]>', timeout=600)
        con.sendline('exit')


x = BLE()
x.discover()
# x.disconnect()