# Custom RC with QTPY esp32-s3 as web-page server and motor control

## Overview

To make an affordable remote control for small model trains, it's possible to use a small lipo batter, a h-bridge to control the motor, and a QTPY esp32-s3 to communicate with the h-bridge and run a web server that the user can load as a web page to control the motor remotely.

## Working With the Repo

This needs the following installed:

* The [Adafruit Libarary and Driver Bundle](https://circuitpython.org/libraries)
* [Adafruit CircuitPython HTTPServer Lib](https://docs.circuitpython.org/projects/httpserver/en/latest/index.html)
* [Adafruit CircuitPython Motor Lib](https://docs.circuitpython.org/projects/motor/en/latest/)

I worked on this as a virtual environment and needed to do the following inside the repo before installing the httpserver and motor libraries:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After that, you can `pip3 install adafruit-circuitpython-motor` or `pip3 install adafruit-circuitpython-httpserver`.
