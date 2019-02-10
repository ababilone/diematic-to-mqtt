
from DiematicBurner import DiematicBurner
from DiematicCircuit import DiematicCircuit
from DiematicConfiguration import DiematicConfiguration
from DiematicDomesticHotWater import DiematicDomesticHotWater
from DiematicSensors import DiematicSensors

class Diematic(object):
    def __init__(self, circuitA, circuitB, circuitC, domesticHotWater, burner, sensors, configuration):
        """
        :type circuitA: DiematicCircuit
        :type circuitB: DiematicCircuit
        :type circuitC: DiematicCircuit
        """

        self.circuitA = circuitA
        self.circuitB = circuitB
        self.circuitC = circuitC
        self.domesticHotWater = domesticHotWater
        self.burner = burner       
        self.sensors = sensors
        self.configuration = configuration