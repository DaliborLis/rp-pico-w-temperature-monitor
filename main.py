from machine import Pin
from PicoDHT22 import PicoDHT22
import utime
import usocket as socket

SERVER_IP="10.0.0.25"
SERVER_PORT=8080

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = socket.getaddrinfo(SERVER_IP, SERVER_PORT)[0][-1]
    s.connect(addr)
    return s

def send_data_over_socket(s, data):
    data_length = len(request)
    total_sent = 0
    while total_sent < data_length:
        sent = s.send(data[total_sent:])
        if sent == 0:
            raise Exception("sending data: socket connection broken")
        total_sent = total_sent + sent

do_connect()

# DHT22 libray is available at
# https://github.com/danjperron/PicoDHT22
dht_sensor = PicoDHT22(Pin(28,Pin.IN,Pin.PULL_UP),dht11=True)

while True:
    T,H = dht_sensor.read()
    if T is None:
        print(" sensor error")
    else:
        print("{}'C  {}%".format(T,H))
        data = '{{"temperature": "{}", "humidity": "{}", "room": "obyvak"}}'.format(T,H)
        s = None
        try:
            s = connect_to_server()
            request = 'POST /tempMonitor/reportTH HTTP/1.1\r\nHost: {}:{} \r\nAccept: */*\r\nContent-Type: application/json\r\nContent-Length: {}\r\n\r\n{}'.format(SERVER_IP, SERVER_PORT, len(data), data).encode('UTF-8')
            print(request)
            send_data_over_socket(s, request)
        except OSError as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            if s != None:
                print("Closing socket")
                s.close()
    #DHT22 not responsive if delay to short
    utime.sleep_ms(15000)
