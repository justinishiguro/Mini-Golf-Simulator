import os
import socketpool
import wifi
import ipaddress
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.methods import HTTPMethod
from adafruit_httpserver.mime_type import MIMEType
from adafruit_requests import Session

import ssl
import board
import time
import busio



# Connect to WiFi
print("Connecting to WiFi...")
ipv4 = ipaddress.IPv4Address("192.168.1.233")
netmask = ipaddress.IPv4Address("255.255.255.0")
gateway = ipaddress.IPv4Address("172.20.10.2")
wifi.radio.set_ipv4_address(ipv4=ipv4,netmask=netmask,gateway=gateway)
#  connect to your SSID

print(os.getenv("CIRCUITPY_WIFI_SSID"))
print(os.getenv('CIRCUITPY_WIFI_PASSWORD'))
wifi.radio.connect(str(os.getenv('CIRCUITPY_WIFI_SSID')), str(os.getenv('CIRCUITPY_WIFI_PASSWORD')))
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)
print("Connected to WiFi!")

url = "https://httpbin.org/"


ssl_context = ssl.create_default_context()
session = Session(socket_pool = pool, ssl_context = ssl_context)
response = session.get(url)
print(response.text)

session.close()


#  the HTML script
#  setup as an f string
#  this way, can insert string variables from code.py directly
#  of note, use {{ and }} if something from html *actually* needs to be in brackets
#  i.e. CSS style formatting
def webpage():
    html = f"""<!DOCTYPE html>
<html>

<div>hello</div>

</html>"""
    return html

#  route default static IP
@server.route("/")
def base(request: HTTPRequest):  # pylint: disable=unused-argument
    #  serve the HTML f string
    #  with content type text/html
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")

# Define request handler for root path
print("starting server..")
# startup the server
try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s:80" % wifi.radio.ipv4_address)
#  if the server fails to begin, restart the pico w
    ip_text = "IP: %s" % wifi.radio.ipv4_address
    print(ip_text)
except OSError:
    time.sleep(5)
    print("restarting..")
    microcontroller.reset()
ping_address = ipaddress.ip_address("8.8.4.4")
clock = time.monotonic()


# Start server loop
while True:
    try:
        #  every 30 seconds, ping server & update temp reading
        if (clock + 30) < time.monotonic():
            if wifi.radio.ping(ping_address) is None:
                print("lost connection")
            else:
                print("connected")
            clock = time.monotonic()
        server.poll()
    #################################################("im  server")
    except Exception as e:
        print(e)
        continue
