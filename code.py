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

wifi_config = config.Wifi()
mqtt_config = config.MQTT()
home_assistant_config = config.HomeAssistant()

pmk = PMK(Hardware())

keys = pmk.keys

buttons = {}
lights = {}

for key in keys:
    buttons[key.number] = homeassistant.MqttButton(key, home_assistant_config)
    lights[key.number] = homeassistant.MqttLight(key, home_assistant_config)

def mqtt_on_connect(client, userdata, flags, rc):
    for key in keys:
        button = buttons[key.number]
        light = lights[key.number]

        client.publish(button.auto_discovery.topic, button.auto_discovery.message)
        client.publish(light.auto_discovery.topic, light.auto_discovery.message)
       
        client.subscribe(light.command_topic)
        client.subscribe(light.rgb_command_topic)

def mqtt_on_message(client, topic, message):
    print(f"New message on topic {topic}: {message}")

for key in keys:
    @pmk.on_press(key)
    def pmk_on_press(key):
        button = buttons[key.number]

        mqtt_client.publish(
            button.state_topic, 
            json.dumps({
                "event_type": "press"
            }))


    @pmk.on_release(key)
    def pmk_on_release(key):
        button = buttons[key.number]

        mqtt_client.publish(
            button.state_topic, 
            json.dumps({
                "event_type": "release"
            }))

    @pmk.on_hold(key)
    def pmk_on_hold(key):
        button = buttons[key.number]

        mqtt_client.publish(
            button.state_topic, 
            json.dumps({
                "event_type": "hold"
            }))

wifi.radio.connect(wifi_config.ssid, wifi_config.password)

socket_pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

mqtt_client = MQTT.MQTT(
    broker = mqtt_config.broker,
    port = mqtt_config.port,
    username = mqtt_config.username,
    password = mqtt_config.password,
    socket_pool = socket_pool,
    ssl_context = ssl_context
)

mqtt_client.on_connect = mqtt_on_connect
mqtt_client.on_message = mqtt_on_message

mqtt_client.connect()

while True:
    #mqtt_client.loop(timeout=1)
    pmk.update()