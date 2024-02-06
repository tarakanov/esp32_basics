from machine import Pin
import time


PIN_LED = 2
led = Pin(PIN_LED, Pin.OUT)


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

	enable_control = not enable_control


# write to esp32 - mpremote cp step_2.py :main.py