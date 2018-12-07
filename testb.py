import sys
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral

button_service_uuid = UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
button_char_uuid    = UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

p = Peripheral("80:7D:3A:C4:4C:16", "random")
ButtonService=p.getServiceByUUID(button_service_uuid)

try:
    ch = ButtonService.getCharacteristics(button_char_uuid)[0]
    if (ch.supportsRead()):
        while 1:
            val = binascii.b2a_hex(ch.read())
            print ("0x" + val)
            time.sleep(1)

finally:
    p.disconnect()