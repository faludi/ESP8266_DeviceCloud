# ESP8266_DeviceCloud
Example for posting data to Device Cloud for data graphing, storage and analysis (digi.com/products/cloud/digi-device-cloud), using MicroPython (http://micropython.org).

## Getting Started:
1. Set up a Device Cloud developer account at http://myacct.digi.com
2. Enter your Device Cloud username and password into the `esp8266_devicecloud.py` file where indicated
3. Upload the edited `esp8266_devicecloud.py` file to your ESP8266. Changing the filename to `main.py` will run it automatically on boot.
4. This simple example uploads the numbers 0 to 499 to Device Cloud. Customize the program to upload your sensor data, device events or any other useful information, for graphing and storage on Device Cloud then access your data via the Device Cloud API.

## Helpful Resources
### MicroPython for ESP8266
To load MicroPython on an ESP8266: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

### To connect an ESP8266 to WiFi:
1. Enter your WiFi network name and password in the `boot.py` file found in the "utilities" directory
2. Upload the `boot.py` file to your ESP8266 to connect to a WiFi network on startup
