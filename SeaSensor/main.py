#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing

from network import Sigfox
import socket
from machine import Pin
from onewire import DS18X20
from onewire import OneWire
import time


# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)
# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)
# make the socket blocking
s.setblocking(True)
# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

openW = OneWire(Pin("P23", mode=Pin.OUT ))
temp = DS18X20(openW)

while True:
    temp.start_conversion()
    tempSend=temp.read_temp_async()
    time.sleep(1)
    
    sendMessage=bytes((temp.read_temp_async() & 0xff, ((temp.read_temp_async() >> 8) & 0xff)))
    print(temp.read_temp_async())
    s.send(sendMessage)
    time.sleep(2)

    # d=DS18X20(Pin('P23', mode=Pin.OUT))
    
    # result=(d.read_temps())
    
    # if result:
    #     val=str(result[0])
    # else:
    #     val="-1"
        
    # print(val)