import homie
from homie import HomieNode
from models.Diematic import Diematic
from models.DiematicBurner import DiematicBurner
from models.DiematicCircuit import DiematicCircuit
from models.DiematicConfiguration import DiematicConfiguration
from models.DiematicDomesticHotWater import DiematicDomesticHotWater
from models.DiematicSensors import DiematicSensors

config = homie.loadConfigFile("homie-python.json")
Homie = homie.Homie(config)

diematicBurnerNode = Homie.Node("diematic-burner", "diematic-burner")
diematicCircuitANode = Homie.Node("diematic-circuit-a", "diematic-circuit")
diematicCircuitBNode = Homie.Node("diematic-circuit-b", "diematic-circuit")
diematicCircuitCNode = Homie.Node("diematic-circuit-c", "diematic-circuit")
diematicConfigurationNode = Homie.Node("diematic-configuration", "diematic-configuration")
diematicDomesticHotWaterNode = Homie.Node("diematic-domestic-hot-water", "diematic-domestic-hot-water")
diematicSensorsNode = Homie.Node("diematic-sensors", "diematic-sensors")

class DiematicHomie:
    def __init__(self):
        Homie.setFirmware("diematic-to-mqtt", "0.0.1")

        self.advertiseDiematicBurner()
        self.advertiseDiematicCircuit(diematicCircuitANode)
        self.advertiseDiematicCircuit(diematicCircuitBNode)
        self.advertiseDiematicCircuit(diematicCircuitCNode)
        self.advertiseDiematicConfiguration()
        self.advertiseDiematicDomesticHotWater()
        self.advertiseDiematicSensors()

        Homie.setup()

    def advertiseDiematicBurner(self):
        diematicBurnerNode.advertise("total-start-count")
        diematicBurnerNode.advertise("total-operating-hours")
        diematicBurnerNode.advertise("total-fuel-consumption")

    def sendDiematicBurner(self, diematicBurner):
        """
        :type diematicBurner: DiematicBurner
        """

        diematicBurnerNode.setProperty("total-start-count").send(diematicBurner.totalStartCount)
        diematicBurnerNode.setProperty("total-operating-hours").send(diematicBurner.totalOperatingHours)
        diematicBurnerNode.setProperty("total-fuel-consumption").send(diematicBurner.totalFuelConsumption)       
    
    def advertiseDiematicCircuit(self, diematicCircuitNode):
        """
        :type diematicCircuitNode: HomieNode
        """
        
        diematicCircuitNode.advertise("ambient-temperature")
        diematicCircuitNode.advertise("day-set-point-temperature")
        diematicCircuitNode.advertise("night-set-point-temperature")
        diematicCircuitNode.advertise("anti-freeze-set-point-temperature")
        diematicCircuitNode.advertise("start-temperature")
        diematicCircuitNode.advertise("is-dhw")
        diematicCircuitNode.advertise("is-auto")
        diematicCircuitNode.advertise("is-day")
        diematicCircuitNode.advertise("is-night")
        diematicCircuitNode.advertise("is-anti-freeze")

    def sendDiematicCircuit(self, diematicCircuitNode, diematicCircuit):
        """
        :type diematicCircuitNode: HomieNode
        :type diematicCircuit: DiematicCircuit
        """
        
        diematicCircuitNode.setProperty("ambient-temperature").send(diematicCircuit.ambientTemperature)
        diematicCircuitNode.setProperty("day-set-point-temperature").send(diematicCircuit.daySetPointTemperature)
        diematicCircuitNode.setProperty("night-set-point-temperature").send(diematicCircuit.nightSetPointTemperature)
        diematicCircuitNode.setProperty("anti-freeze-set-point-temperature").send(diematicCircuit.antiFreezeSetPointTemperature)
        diematicCircuitNode.setProperty("start-temperature").send(diematicCircuit.startTemperature)
        diematicCircuitNode.setProperty("is-dhw").send(diematicCircuit.isDhw)
        diematicCircuitNode.setProperty("is-auto").send(diematicCircuit.isAuto)
        diematicCircuitNode.setProperty("is-day").send(diematicCircuit.isDay)
        diematicCircuitNode.setProperty("is-night").send(diematicCircuit.isNight)
        diematicCircuitNode.setProperty("is-anti-freeze").send(diematicCircuit.isAntifreeze)

    def advertiseDiematicConfiguration(self):
        diematicConfigurationNode.advertise("firmeware-version")
        diematicConfigurationNode.advertise("year")
        diematicConfigurationNode.advertise("month")
        diematicConfigurationNode.advertise("day")
        diematicConfigurationNode.advertise("day-of-week")
        diematicConfigurationNode.advertise("hour")
        diematicConfigurationNode.advertise("minute")

    def sendDiematicConfiguration(self, diematicConfiguration):
        """
        :type diematicConfiguration: DiematicConfiguration
        """

        diematicConfigurationNode.setProperty("firmeware-version").send(diematicConfiguration.firmwareVersion)
        diematicConfigurationNode.setProperty("year").send(diematicConfiguration.year)
        diematicConfigurationNode.setProperty("month").send(diematicConfiguration.month)
        diematicConfigurationNode.setProperty("day").send(diematicConfiguration.day)
        diematicConfigurationNode.setProperty("day-of-week").send(diematicConfiguration.dayOfWeek)
        diematicConfigurationNode.setProperty("hour").send(diematicConfiguration.hour)
        diematicConfigurationNode.setProperty("minute").send(diematicConfiguration.minute)

    def advertiseDiematicDomesticHotWater(self):
        diematicDomesticHotWaterNode.advertise("temperature")

    def sendDiematicDomesticHotWater(self, diematicDomesticHotWater):
        """
        :type diematicDomesticHotWater: DiematicDomesticHotWater
        """

        diematicDomesticHotWaterNode.setProperty("temperature").send(diematicDomesticHotWater.temperature)

    def advertiseDiematicSensors(self):
        diematicSensorsNode.advertise("external-temperature")
        diematicSensorsNode.advertise("heater-temperature")

    def sendDiematicSensors(self, diematicSensors):
        """
        :type diematicSensors: DiematicSensors
        """

        diematicSensorsNode.setProperty("external-temperature").send(diematicSensors.externalTemperature)
        diematicSensorsNode.setProperty("heater-temperature").send(diematicSensors.heaterTemperature)

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