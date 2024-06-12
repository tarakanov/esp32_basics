# boot.py
def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('wifi_name', 'wifi_pass')
        while not sta_if.isconnected():
            pass # wait till connection
    print('network config:', sta_if.ifconfig())
    
connect()
