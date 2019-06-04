import sys
import socket
import machine
import time
import network
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect('Yooooooo', 'aaaaaaa')
  while not sta_if.isconnected():
    pass
print('network config:', sta_if.ifconfig())
print('***************')
print('****** from  localhost *********')