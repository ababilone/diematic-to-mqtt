from models.Diematic import Diematic
from models.DiematicBurner import DiematicBurner
from models.DiematicCircuit import DiematicCircuit
from models.DiematicConfiguration import DiematicConfiguration
from models.DiematicDomesticHotWater import DiematicDomesticHotWater
from models.DiematicSensors import DiematicSensors
from utils import int_to_bcd
import logging

class DiematicReader():
    def __init__(self, instrument):
        self.instrument = instrument

    def ir(self, registeraddress, numberOfDecimals = 0, functioncode = 3, signed = False):
        return self.instrument.read_register(registeraddress, numberOfDecimals, functioncode, signed)

    def read(self):

        configuration = DiematicConfiguration(self.ir(3), self.ir(110), self.ir(109), self.ir(108), self.ir(6), self.ir(4), self.ir(5))

        domesticHotWater = DiematicDomesticHotWater(self.ir(62, 1))
        sensors = DiematicSensors(self.ir(7, 1, signed = True), self.ir(75, 1))
        circuitA = DiematicCircuit(self.ir(18, 1), self.ir(14, 1), self.ir(15, 1), self.ir(16, 1), self.ir(17), self.ir(19), self.ir(21, 1))
        circuitB = DiematicCircuit(self.ir(27, 1), self.ir(23, 1), self.ir(24, 1), self.ir(25, 1), self.ir(26), self.ir(28), self.ir(32, 1), self.ir(33, 1))
        circuitC = DiematicCircuit(self.ir(39, 1), self.ir(35, 1), self.ir(36, 1), self.ir(37, 1), self.ir(38), self.ir(40), self.ir(44, 1), self.ir(45, 1))

        burnerStartCount = int_to_bcd(self.ir(77)) * 10 + self.ir(251)
        burnerOperatingHours = int_to_bcd(self.ir(78)) * 10 +  self.ir(252)
        burner = DiematicBurner(burnerStartCount, burnerOperatingHours)

        logging.info("Successfull read of Diematic structure from modbus!")

        return Diematic(circuitA, circuitB, circuitC, domesticHotWater, burner, sensors, configuration)