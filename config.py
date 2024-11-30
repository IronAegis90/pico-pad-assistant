import os

class HomeAssistant:

    def __init__(self):
        self._device_id = os.getenv("HOMEASSISTANT_DEVICE_ID")
        self._device_name = os.getenv("HOMEASSISTANT_DEVICE_NAME")

    def device_id(self):
        return self._device_id

    def device_name(self):
        return self._device_name
    
class MQTT:

    def __init__(self):
        self._broker = os.getenv("MQTT_BROKER")
        self._password = os.getenv("MQTT_PASSWORD")
        self._port = os.getenv("MQTT_PORT")
        self._username = os.getenv("MQTT_USERNAME")

    def broker(self):
        return self._broker
    
    def password(self):
        return self._password

    def port(self):
        return self._port
    
    def username(self):
        return self._username
    
class Software:

    def __init__(self):
        self._version = os.getenv("SOFTWARE_VERSION")

    def version(self):
        return self._version