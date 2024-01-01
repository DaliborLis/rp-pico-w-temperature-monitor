from machine import Pin
from PicoDHT22 import PicoDHT22
import utime

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'passwd')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22

do_connect()
dht_sensor=PicoDHT22(Pin(28,Pin.IN,Pin.PULL_UP),dht11=True)
while True:
    T,H = dht_sensor.read()
    if T is None:
        print(" sensor error")
    else:
        print("{}'C  {}%".format(T,H))
    #DHT22 not responsive if delay to short
    utime.sleep_ms(500)
