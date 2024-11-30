# pico-pad-assistant

Integrate the Pimoroni Pico RGB Keypd into Home Assistant using MQTT

# Prerequisites

* Raspberry Pi Pico W
* Home Assistant
* MQTT Broker

## Raspberry Pi Pico W Setup

1. Connect the Pico to your computer. Press and hold the `BOOTSEL` button while inserting the USB cable. A new `Mass Storage Device` should appear File Explorer.
2. Download the `MicroPython` UF2 Bootloader. Found [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
3. Copy the `MicroPython` UF2 Bootloader to the Pico storage location. The Pico should reboot and a new file system will be mounted.

## Home Assistant

