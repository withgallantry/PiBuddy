import pygatt
import logging
logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.DEBUG)

adapter = pygatt.GATTToolBackend()

def print_this(h, stuff):
    print(stuff)

adapter.start()
devices = adapter.scan()
for device in devices:
    print device
    # if "PiBuddy" in device["name"]:
    #     print("found device")
    #     break

device = adapter.connect(device["address"])
chars = device.discover_characteristics() # I get some type of a warning here. "UUID b'ffe1' is of unknown type"
# value = device.char_read("00002a05-0000-1000-8000-00805f9b34fb") #this address was found by printing the `chars` array
device.subscribe('6e400003-b5a3-f393-e0a9-e50e24dcca9e', print_this) #ExpectedResponseTimeout