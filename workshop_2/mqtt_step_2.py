# main.py
from umqtt.simple import MQTTClient
from machine import unique_id, Pin
import time


# start

CHIP_ID = 'esp32_' + ''.join(['{0:02x}'.format(b) for b in unique_id()[-2:]])
PIN_LED = 2
led = Pin(PIN_LED, Pin.OUT)
def blink():
	led.on()
	time.sleep(0.3)
	led.off()

blink()

print('Start: my id - ' + CHIP_ID)
# mqtt

BROKER_ADDR = 'broker.emqx.io'
TOPIC = 'esp32_basics'
CLIENT_NAME = CHIP_ID
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=600)

def on_msg(topic, msg):
	print('Recieved: [{}], msg: {}'.format(topic.decode('utf-8'), msg.decode('utf-8')))

mqttc.set_callback(on_msg)


mqttc.connect()
mqttc.subscribe(TOPIC, qos=0)		


# hello, chat!
mqttc.publish(TOPIC, 'Hello! I am ' + CLIENT_NAME)

while True:
	blink()
	mqttc.check_msg()
	time.sleep(1)


# см. скриншоты step_2_*.png