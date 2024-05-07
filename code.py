import os
import ipaddress
import mdns
import wifi
import socketpool
from adafruit_httpserver.server import Server
from adafruit_httpserver.request import Request
from adafruit_httpserver.response import Response
import adafruit_httpserver.methods as Methods
import adafruit_httpserver.mime_types as MT

from templates.controls import controls

from src.controls.controls import setReverser
from src.controls.controls import setThrottle
from src.controls.controls import eStop

print()
print("Connection to WiFi")

# need to come back and make this dynamic...
# set static IP address
ipv4 = ipaddress.IPv4Address("192.168.0.89")
netmask = ipaddress.IPv4Address("255.255.255.0")
gateway = ipaddress.IPv4Address("192.168.1.1")
wifi.radio.set_ipv4_address(ipv4=ipv4, netmask=netmask, gateway=gateway)
# Connect to ssid
wifi.radio.connect(
    os.getenv('CIRCUITPY_WIFI_SSID'),
    os.getenv('CIRCUITPY_WIFI_PASSWORD')
)
print("Connected to WiFi")

mdns_server=mdns.Server(wifi.radio)
mdns_server.hostname="009-rc"
mdns_server.instance_name="009-rc"

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool)

#page routes
@server.route("/", Methods.GET)
def rootHandler(request: Request):
    with Response(
        request,
        content_type=MT.MIMETypes.REGISTERED.get('html')
    ) as response:
        response.send(f"{controls}")

#api routes
@server.route("/reverser/<rev_param>", Methods.POST)
def reverserHandler(request: Request, rev_param):
    setReverser(rev_param)
    with Response(
        request,
        status=[204, "No Content"]
    ) as response:
        response.send()
@server.route("/notch/<notch_param>", Methods.POST)
def notchHandler(request: Request, notch_param):
    setThrottle(notch_param)
    with Response(
        request,
        status=[204, "No Content"]
    ) as response:
        response.send()
@server.route("/estop", Methods.POST)
def eStopHandler(request: Request):
    eStop()
    with Response(
        request,
        status=[204, "No Content"]
    ) as response:
        response.send()

print(f"Listening on http://{wifi.radio.ipv4_address}:80")
server.serve_forever(str(wifi.radio.ipv4_address))
