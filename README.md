# diematic-to-mqtt

### Introduction

Create an [Homie](https://homieiot.github.io/) device from a connected Diematic boiler from De Dietrich. 

>This has only been tested with a GTU C 123 FF

### Published properties

* Burner
    * Total start count
    * Total operating hours
    * Total fuel consumption

* Circuit a, b, c
    * Ambient temperature
    * Day set point temperature
    * Night set point temperature
    * Anti freeze set point temperature
    * Derogation
    * Sensor influence
    * Start temperature

* Configuration

    * Firmware version
    * Year
    * Month
    * Day
    * Day of week
    * Hour
    * Minute

* Domestic hot water

    * Temperature

* Sensors

    * External temperature
    * Heater

### Usage

* Check homie-python.json for MQTT/Homie device configuration
* Check serial por in DiematicToMqttWorker
* Check gal per hour in DiematicBurner
* Launch with 'python DiematicToMqtt.py'
* Enjoy your boiler in MQTT or maybe OpenHAB

### To-Do

* Publish more properties (Registers mapping table)[datasheets/modbus-registers-dedietrich.xlsx]
* Allow two way communication?
* Add some settings
    * serial port in DiematicToMqttWorker
    * gal per hour - depending on the boiler nozzle - in DiematicBurner

### More

* [Homie](https://homieiot.github.io/)
* [homie-python](https://github.com/bodiroga/homie-python)
* [minimalmodbus](https://github.com/pyhys/minimalmodbus)
* [OpenHAB](https://www.openhab.org/)