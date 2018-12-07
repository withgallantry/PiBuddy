import pexpect
from subprocess import Popen
import time
import os


class BLE:
    con = None

    def getDevice(self, name):
        sensorName = ''
        while sensorName != "PiBuddy":
            os.system("hcitool lescan> scan.txt & pkill --signal SIGINT hcitool")
            scan = open("scan.txt", "r")
            readscan = scan.read()
            if "PiBuddy" in readscan:
                items = readscan.split('\n')
                for i in range(len(items)):
                    if "PiBuddy" in items[i]:
                        mac = items[i].split(' ')[0]
                        sensorName = "PiBuddy"
                        return mac

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
        self.con = con

    def writeCmd(self, handle, command):
        self.con.sendline('char-write-cmd ' + handle + command)
        self.con.expect('\[LE\]>', timeout=600)

    def read(self):
        something = self.con.sendline('char-read-uuid 6E400003-B5A3-F393-E0A9-E50E24DCCA9E')
        self.con.expect('\[LE\]>', timeout=600)
        print self.con.after
        print something

    def disconnect(self):
        self.con.sendline('disconnect')
        self.con.expect('\[LE\]>', timeout=600)
        self.con.sendline('exit')


x = BLE()
macAddress = x.getDevice('PiBuddy')
print macAddress
x.connect(macAddress)
time.sleep(1)
x.read()
x.disconnect()
