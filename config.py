import os

class Wifi:

    def __init__(self):
        self._ssid = os.getenv('WIFI_SSID')
        self._password = os.getenv('WIFI_PASSWORD')

    @property
    def ssid(self):
        return self._ssid
    
    @property
    def password(self):
        return self._password

class HomeAssistant:

    def __init__(self):
        self._device_id = os.getenv("HOMEASSISTANT_DEVICE_ID")
        self._device_name = os.getenv("HOMEASSISTANT_DEVICE_NAME")
        self._auto_discovery_topic = os.getenv("HOMEASSISTANT_AUTO_DISCOVERY_TOPIC")

    @property
    def auto_discovery_topic(self):
        return self._auto_discovery_topic

    @property
    def device_id(self):
        return self._device_id

    @property
    def device_name(self):
        return self._device_name
    
class MQTT:

    def __init__(self):
        self._broker = os.getenv("MQTT_BROKER")
        self._password = os.getenv("MQTT_PASSWORD")
        self._port = os.getenv("MQTT_PORT")
        self._username = os.getenv("MQTT_USERNAME")

    @property
    def broker(self):
        return self._broker
    
    @property
    def password(self):
        return self._password

    @property
    def port(self):
        return self._port
    
    @property
    def username(self):
        return self._username