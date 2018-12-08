import pygatt
from binascii import hexlify

adapter = pygatt.GATTToolBackend()

def handle_data(handle, value):
    """
    handle -- integer, characteristic read handle the data was received on
    value -- bytearray, the data returned in the notification
    """
    print("Received data: %s" % hexlify(value))

try:
    adapter.start()
    device = adapter.connect('80:7d:3a:c4:4c:16')

    device.subscribe("6E400003-B5A3-F393-E0A9-E50E24DCCA9E",
                     callback=handle_data)
finally:
    adapter.stop()