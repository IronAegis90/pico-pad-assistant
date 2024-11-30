import config
import json

class Domains:

    BUTTON = "Button"

class AutoDiscovery:

    def __init__(self):
        self._homeassistant = config.HomeAssistant()
        self._software = config.Software()

    def topic(self, domain, key):
        return 'homeassistant/%s/%s_%s/config' % (domain.lower(), self._homeassistant.device_id(), key.number)

    def message(self, domain, key):
        return json.dumps({
            "name": '%s %s' % (domain, key.number),
            'unique_id': '%s_%s_%s' % (self._homeassistant.device_id(), domain.lower(), key.number),
            "device": {
                "name": self._homeassistant.device_name(),
                "identifiers": self._homeassistant.device_id(),
                "manufacturer": "Pimoroni",
                "model": "Pico W",
                "hw_version": "1.0",
                "sw_version": self._software.version()
            }
        })