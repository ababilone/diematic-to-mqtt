# coding=utf-8

import homie
from homie import HomieNode
from models.Diematic import Diematic
from models.DiematicBurner import DiematicBurner
from models.DiematicCircuit import DiematicCircuit
from models.DiematicConfiguration import DiematicConfiguration
from models.DiematicDomesticHotWater import DiematicDomesticHotWater
from models.DiematicSensors import DiematicSensors

config = homie.loadConfigFile("homie-python.json")
device = homie.Device(config)

diematicBurnerNode = device.addNode("diematic-burner", "Burner", "diematic-burner")
diematicCircuitANode = device.addNode("diematic-circuit-a", "Circuit A", "diematic-circuit")
diematicCircuitBNode = device.addNode("diematic-circuit-b", "Circuit B", "diematic-circuit")
diematicCircuitCNode = device.addNode("diematic-circuit-c", "Circuit C", "diematic-circuit")
diematicConfigurationNode = device.addNode("diematic-configuration", "Configuration", "diematic-configuration")
diematicDomesticHotWaterNode = device.addNode("diematic-domestic-hot-water", "Domestic hot water", "diematic-domestic-hot-water")
diematicSensorsNode = device.addNode("diematic-sensors", "Sensors", "diematic-sensors")

class DiematicHomie:
    def __init__(self):
        device.setFirmware("diematic-to-mqtt", "0.0.1")

        self.burner = self.addPropertyDiematicBurner()
        self.addPropertyDiematicCircuit(diematicCircuitANode)
        self.addPropertyDiematicCircuit(diematicCircuitBNode)
        self.addPropertyDiematicCircuit(diematicCircuitCNode)
        self.addPropertyDiematicConfiguration()
        self.addPropertyDiematicDomesticHotWater()
        self.addPropertyDiematicSensors()

        device.setup()

    def addPropertyDiematicBurner(self):
        diematicBurnerNode.addProperty("total-start-count", "Total start count", "#", "integer")
        diematicBurnerNode.addProperty("total-operating-hours", "Total operating hours", "#", "integer")
        diematicBurnerNode.addProperty("total-fuel-consumption", "Total fuel consumption", "l", "integer")

    def sendDiematicBurner(self, diematicBurner):
        """
        :type diematicBurner: DiematicBurner
        """

        diematicBurnerNode.getProperty("total-start-count").update(diematicBurner.totalStartCount)
        diematicBurnerNode.getProperty("total-operating-hours").update(diematicBurner.totalOperatingHours)
        diematicBurnerNode.getProperty("total-fuel-consumption").update(diematicBurner.totalFuelConsumption)       
    
    def addPropertyDiematicCircuit(self, diematicCircuitNode):
        """
        :type diematicCircuitNode: HomieNode
        """
        
        diematicCircuitNode.addProperty("ambient-temperature", "Ambient temperature", "°C", "float")
        diematicCircuitNode.addProperty("day-set-point-temperature", "Day set point temperature", "°C", "float")
        diematicCircuitNode.addProperty("night-set-point-temperature", "Night set point temperature", "°C", "float")
        diematicCircuitNode.addProperty("anti-freeze-set-point-temperature", "Anti freeze set point temperature", "°C", "float")
        diematicCircuitNode.addProperty("start-temperature", "Start temperature", "°C", "float")
        diematicCircuitNode.addProperty("is-dhw", "Is domestic hot water", None, "boolean")
        diematicCircuitNode.addProperty("is-auto", "Is auto", None, "boolean")
        diematicCircuitNode.addProperty("is-day", "Is day", None, "boolean")
        diematicCircuitNode.addProperty("is-night", "Is night", None, "boolean")
        diematicCircuitNode.addProperty("is-anti-freeze", "Is anti freeze", None, "boolean")

    def sendDiematicCircuit(self, diematicCircuitNode, diematicCircuit):
        """
        :type diematicCircuitNode: HomieNode
        :type diematicCircuit: DiematicCircuit
        """
        
        diematicCircuitNode.getProperty("ambient-temperature").update(diematicCircuit.ambientTemperature)
        diematicCircuitNode.getProperty("day-set-point-temperature").update(diematicCircuit.daySetPointTemperature)
        diematicCircuitNode.getProperty("night-set-point-temperature").update(diematicCircuit.nightSetPointTemperature)
        diematicCircuitNode.getProperty("anti-freeze-set-point-temperature").update(diematicCircuit.antiFreezeSetPointTemperature)
        diematicCircuitNode.getProperty("start-temperature").update(diematicCircuit.startTemperature)
        diematicCircuitNode.getProperty("is-dhw").update(diematicCircuit.isDhw)
        diematicCircuitNode.getProperty("is-auto").update(diematicCircuit.isAuto)
        diematicCircuitNode.getProperty("is-day").update(diematicCircuit.isDay)
        diematicCircuitNode.getProperty("is-night").update(diematicCircuit.isNight)
        diematicCircuitNode.getProperty("is-anti-freeze").update(diematicCircuit.isAntifreeze)

    def addPropertyDiematicConfiguration(self):
        diematicConfigurationNode.addProperty("firmware-version", "Firmware version", None, "string")
        diematicConfigurationNode.addProperty("year", "Year", None, "interger")
        diematicConfigurationNode.addProperty("month", "Month", None, "interger")
        diematicConfigurationNode.addProperty("day", "Day", None, "interger")
        diematicConfigurationNode.addProperty("day-of-week", "Day of week", None, "interger")
        diematicConfigurationNode.addProperty("hour", "Hour", None, "interger")
        diematicConfigurationNode.addProperty("minute", "Minute", None, "interger")

    def sendDiematicConfiguration(self, diematicConfiguration):
        """
        :type diematicConfiguration: DiematicConfiguration
        """

        diematicConfigurationNode.getProperty("firmware-version").update(diematicConfiguration.firmwareVersion)
        diematicConfigurationNode.getProperty("year").update(diematicConfiguration.year)
        diematicConfigurationNode.getProperty("month").update(diematicConfiguration.month)
        diematicConfigurationNode.getProperty("day").update(diematicConfiguration.day)
        diematicConfigurationNode.getProperty("day-of-week").update(diematicConfiguration.dayOfWeek)
        diematicConfigurationNode.getProperty("hour").update(diematicConfiguration.hour)
        diematicConfigurationNode.getProperty("minute").update(diematicConfiguration.minute)

    def addPropertyDiematicDomesticHotWater(self):
        diematicDomesticHotWaterNode.addProperty("temperature", "Temperature", "°C", "float")

    def sendDiematicDomesticHotWater(self, diematicDomesticHotWater):
        """
        :type diematicDomesticHotWater: DiematicDomesticHotWater
        """

        diematicDomesticHotWaterNode.getProperty("temperature").update(diematicDomesticHotWater.temperature)

    def addPropertyDiematicSensors(self):
        diematicSensorsNode.addProperty("external-temperature", "External temperature", "°C", "float")
        diematicSensorsNode.addProperty("heater-temperature", "Heater temperature", "°C", "float")

    def sendDiematicSensors(self, diematicSensors):
        """
        :type diematicSensors: DiematicSensors
        """

        diematicSensorsNode.getProperty("external-temperature").update(diematicSensors.externalTemperature)
        diematicSensorsNode.getProperty("heater-temperature").update(diematicSensors.heaterTemperature)

    def send(self, diematic):
        """
        :type diematic: Diematic
        """

        self.sendDiematicBurner(diematic.burner)
        self.sendDiematicCircuit(diematicCircuitANode, diematic.circuitA)
        self.sendDiematicCircuit(diematicCircuitBNode, diematic.circuitB)
        self.sendDiematicCircuit(diematicCircuitCNode, diematic.circuitC)
        self.sendDiematicConfiguration(diematic.configuration)
        self.sendDiematicDomesticHotWater(diematic.domesticHotWater)
        self.sendDiematicSensors(diematic.sensors)