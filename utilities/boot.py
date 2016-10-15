# This file is executed on every boot (including wake-boot from deepsleep)

def do_connect():
    import network, ubinascii
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect('wifi network name', 'your wifi password')
        while not wlan.isconnected():
            pass
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print('network config:', wlan.ifconfig(), 'MAC:', mac.upper())

do_connect()


