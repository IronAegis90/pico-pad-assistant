import adafruit_logging as logging
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import config
import json
import homeassistant
import os
import socketpool
import ssl
import wifi

from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware

mqttConfig = config.MQTT()

pmk = PMK(Hardware())

keys = pmk.keys

def mqtt_on_connect(client, userdata, flags, rc):
    auto_discovery = homeassistant.AutoDiscovery()

    for key in keys:
        client.publish(auto_discovery.topic(homeassistant.Domains().BUTTON, key), auto_discovery.message(homeassistant.Domains().BUTTON, key))

def mqtt_on_message(client, topic, message):
    print(f"New message on topic {topic}: {message}")

for key in keys:
    @pmk.on_press(key)
    def pmk_on_press(key):
        print("Key {} pressed".format(key.number))
        key.set_led(0, 0, 255)

    @pmk.on_release(key)
    def pmk_on_release(key):
        print("Key {} released".format(key.number))
        if key.rgb == [255, 0, 0]:
            key.set_led(0, 255, 0)
        else:
            key.set_led(64, 64, 64)

    @pmk.on_hold(key)
    def pmk_on_hold(key):
        print("Key {} held".format(key.number))
        key.set_led(255, 0, 0)

wifi.radio.connect(os.getenv('WIFI_SSID'), os.getenv('WIFI_PASSWORD'))

socket_pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

mqtt_client = MQTT.MQTT(
    broker = mqttConfig.broker(),
    port = mqttConfig.port(),
    username = mqttConfig.username(),
    password = mqttConfig.password(),
    socket_pool = socket_pool,
    ssl_context = ssl_context
)

mqtt_client.enable_logger(logging, logging.DEBUG)

mqtt_client.on_connect = mqtt_on_connect
mqtt_client.on_message = mqtt_on_message

mqtt_client.connect()

while True:
    pmk.update()