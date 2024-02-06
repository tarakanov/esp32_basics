from machine import Pin, PWM
import dht
import time


PIN_LED = 2
PIN_BUTTON = 12
PIN_DHT = 27
PIN_FAN = 14
MAX_DUTY_CYCLE = 65_535
FAN_HIGH_SPEED = (MAX_DUTY_CYCLE * 12) // 12
FAN_LOW_SPEED = (MAX_DUTY_CYCLE * 1) // 12
FAN_OFF = (MAX_DUTY_CYCLE * 0) // 12

led = Pin(PIN_LED, Pin.OUT)
button = Pin(PIN_BUTTON, Pin.IN, Pin.PULL_UP)
dht_sensor = dht.DHT11(Pin(PIN_DHT))
pwm_fan = PWM(Pin(PIN_FAN), freq=25_000, duty_u16=MAX_DUTY_CYCLE)


def get_humidity():
	result = 0
	try:
		dht_sensor.measure()
		result = dht_sensor.humidity()
		print("humidity: " + str(result))
	except:
		pass
	return result

def fan_off():
	pwm_fan.duty_u16(FAN_OFF)

def fan_on():
	pwm_fan.duty_u16(FAN_HIGH_SPEED)

def run(trigger_lvl):
	humidity = get_humidity()
	if humidity > trigger_lvl:
		fan_on()
	else:
		fan_off()


# start
led.on()
time.sleep(0.3)
led.off()

enable_control = False

# work
while True:

	if enable_control:
		led.on()
		run(30)
	else:
		led.off()
		fan_off()
	time.sleep(1)

	if button.value() == 0:
		enable_control = not enable_control  
	else: 
		enable_control


# write to esp32 - mpremote cp step_6.py :main.py
