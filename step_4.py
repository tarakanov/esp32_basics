from machine import Pin
import dht
import time



PIN_LED = 2
PIN_BUTTON = 12
PIN_DHT = 27

led = Pin(PIN_LED, Pin.OUT)
button = Pin(PIN_BUTTON, Pin.IN, Pin.PULL_UP)
dht_sensor = dht.DHT11(Pin(PIN_DHT))


def get_humidity():
	result = 0
	try:
		dht_sensor.measure()
		result = dht_sensor.humidity()
		print("humidity: " + str(result))
	except:
		pass
	return result


# start
led.on()
time.sleep(0.3)
led.off()

enable_control = False

# work

while True:

	if enable_control:
		led.on()
		get_humidity()
	else:
		led.off()
	time.sleep(1)

	if button.value() == 0:
		enable_control = not enable_control  
	else: 
		enable_control