import os
import ipaddress
import mdns
import wifi
import socketpool
from adafruit_httpserver.server import Server
from adafruit_httpserver.request import Request
from adafruit_httpserver.response import Response, FileResponse, JSONResponse
import adafruit_httpserver.methods as Methods
import adafruit_httpserver.mime_types as MT
from adafruit_httpserver.status import Status

from templates.controls import controls

from src.controls.controls import ControlClass


ap_ssid = "rc-wifi"
ap_password = "password"

controlClass = ControlClass()
print("Starting Up")
print()

wifi.radio.start_ap(ssid=ap_ssid, channel=1, password=ap_password)

# Print access point settings
print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))
print("My IP address is", str(wifi.radio.ipv4_address_ap))

mdns_server = mdns.Server(wifi.radio)
mdns_server.hostname = "constance"
mdns_server.advertise_service(service_type="_http", protocol="_tcp", port=5000)

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/rc", debug=True)

# page routes
@server.route("/", Methods.GET)
def rootHandler(request: Request):
    return FileResponse(
        request,
        filename="controls.html",
        root_path="/markup",
        content_type="text/html",
        status=Status(200, "ok")
    )
    
# api routes
@server.route("/reverser/<rev_param>", Methods.POST)
def reverserHandler(request: Request, rev_param):
    res = controlClass.setReverser(new=rev_param)
    return JSONResponse(
        request,
        {"reverser": res},
        status=Status(200, "ok")
    )

@server.route("/notch/<notch_param>", Methods.POST)
def notchHandler(request: Request, notch_param):
    throttleResult = controlClass.setThrottle(newSpeed=notch_param)
    res = ""

    if(throttleResult != None):
        str(throttleResult)
    else:
        res = "0"
    return JSONResponse(
        request,
        {"throttle": res},
        status=Status(200, "ok")
    )

@server.route("/estop", Methods.POST)
def eStopHandler(request: Request):
    res = controlClass.eStop()
    return JSONResponse(
        request,
        {"stop": res},
        status=Status(200, "ok")
    )

print(f"Listening on http://{str(wifi.radio.ipv4_address_ap)}:80")
server.serve_forever(str(wifi.radio.ipv4_address_ap), 80)
