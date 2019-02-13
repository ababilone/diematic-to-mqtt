
from models.DiematicBurner import DiematicBurner
from models.DiematicCircuit import DiematicCircuit
from models.DiematicConfiguration import DiematicConfiguration
from models.DiematicDomesticHotWater import DiematicDomesticHotWater
from models.DiematicSensors import DiematicSensors

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