# ESP8266_DeviceCloud
Example of posting data from an ESP8266 WiFi module to Digi's Device Cloud (http://digi.com/products/cloud/digi-device-cloud), using MicroPython (http://micropython.org).

## Getting Started:
1. Set up a Device Cloud developer account
2. Enter your Device Cloud username and password into the esp8266_devicecloud.py file where indicated
3. Upload the edited esp8266_devicecloud.py file to your ESP8266. You can change the filename to main.py if you want it to run automatically on boot.
4. The example will upload the numbers 0 to 499 to Device Cloud. You can customize this program to upload your sensor data, device events or any other useful information to the cloud.

## Helpful Resources
### MicroPython for ESP8266
To load MicroPython on an ESP8266: https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html

### To connect an ESP8266 to WiFi:
1. Enter your WiFi network name and password in the boot.py file found in the "utilities" directory
2. Upload the boot.py file to your ESP8266 to connect to a WiFi network on startup
