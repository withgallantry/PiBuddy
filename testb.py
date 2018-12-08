from bluepy.btle import Scanner, DefaultDelegate, Peripheral


class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered device", dev.addr
        elif isNewData:
            print "Received new data from", dev.addr


class PiBuddy():
    def __init__(self, address):
        self.device = Peripheral(address)
        self.read = self.device.getCharacteristics(uuid="6E400003-B5A3-F393-E0A9-E50E24DCCA9E")[0]
        self.readHandle = self.read.getHandle()

    def getCurrentStatus(self):
        return self.device.readCharacteristic(self.readHandle)


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(2.0)

for dev in devices:
    # print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        if "PiBuddy" in dev.getValueText(adtype):
            print "Found PiBuddy at: ", dev.addr
            print "Connecting..."
            buddy = PiBuddy(dev.addr)
            current = buddy.getCurrentStatus()
            print current
