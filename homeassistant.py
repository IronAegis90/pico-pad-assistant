import json

class AutoDiscovery(object):

    def __init__(self, topic, message):
        self._topic = topic
        self._message = message

    @property
    def topic(self):
        return self._topic
    
    @property
    def message(self):
        return self._message

class MqttButton:

    def __init__(self, key, home_assistant_config):
        self._key = key
        self._home_assistant_config = home_assistant_config

    @property
    def state_topic(self):
        return 'pico-pad-assistant/%s/button/%s/event' % (self._home_assistant_config.device_id, self._key.number)

    @property
    def auto_discovery(self):
        return AutoDiscovery(
            '%s/event/%s_%s/config' % (self._home_assistant_config.auto_discovery_topic, self._home_assistant_config.device_id, self._key.number), 
            json.dumps({
                "name": 'Button %s' % (self._key.number + 1),
                "unique_id": '%s_switch_%s' % (self._home_assistant_config.device_id, self._key.number),
                "state_topic": self.state_topic, 
                "platform": 'event',
                "event_types": [
                    "press",
                    "hold",
                    "release"
                ],
                "device": {
                    "name": self._home_assistant_config.device_name,
                    "identifiers": self._home_assistant_config.device_id,
                    "manufacturer": "Pimoroni",
                    "model": "Pico W",
                    "hw_version": "1.0",
                    "sw_version": "1.0"
                }
            }))
    
class MqttLight:

    def __init__(self, key, home_assistant_config):
        self._key = key
        self._home_assistant_config = home_assistant_config

    @property
    def command_topic(self):
        return 'pico-pad-assistant/%s/light/%s/command' % (self._home_assistant_config.device_id, self._key.number)
    
    @property
    def rgb_command_topic(self):
        return 'pico-pad-assistant/%s/light/%s/rgb' % (self._home_assistant_config.device_id, self._key.number)

    @property
    def auto_discovery(self):
        return AutoDiscovery(
            '%s/light/%s_%s/config' % (self._home_assistant_config.auto_discovery_topic, self._home_assistant_config.device_id, self._key.number), 
            json.dumps({
                "name": 'Button %s Light' % (self._key.number + 1),
                "unique_id": '%s_button_%s_light' % (self._home_assistant_config.device_id, self._key.number),
                "command_topic": self.command_topic, 
                "rgb_command_topic": self.rgb_command_topic, 
                "platform": 'light',
                "device": {
                    "name": self._home_assistant_config.device_name,
                    "identifiers": self._home_assistant_config.device_id,
                    "manufacturer": "Pimoroni",
                    "model": "Pico W",
                    "hw_version": "1.0",
                    "sw_version": "1.0"
                }
            }))