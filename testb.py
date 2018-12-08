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


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(2.0)

for dev in devices:
    # print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
    for (adtype, desc, value) in dev.getScanData():
        if "PiBuddy" in dev.getValueText(adtype):
            print "Found PiBuddy at: ", dev.addr
            print "Connecting..."
            buddy = PiBuddy(dev.addr)
            services = buddy.getServices()
            print services
