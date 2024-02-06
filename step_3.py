from machine import Pin
import time


PIN_LED = 2
PIN_BUTTON = 12

led = Pin(PIN_LED, Pin.OUT)
button = Pin(PIN_BUTTON, Pin.IN, Pin.PULL_UP)


# start
led.on()
time.sleep(0.3)
led.off()
enable_control = False


# work
while True:

	if enable_control:
		led.on()
	else:
		led.off()
	time.sleep(1)

	if button.value() == 0:
		enable_control = not enable_control  
	else: 
		enable_control

# write to esp32 - mpremote cp step_3.py :main.py