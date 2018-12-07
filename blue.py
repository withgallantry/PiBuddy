import pexpect
from subprocess import Popen
import time
import os


class BLE:
    def getDevice(self, name):
        sensorName = ''
        while sensorName != "PiBuddy":
            os.system("hcitool lescan> scan.txt & pkill --signal SIGINT hcitool")
            scan = open("scan.txt", "r")
            readscan = scan.read()
            if "PiBuddy" in readscan:
                thing = readscan.split('\n')
                print thing
                sensorName = "PiBuddy"

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
x.getDevice('PiBuddy')
# x.disconnect()
