class DiematicCircuit(object):
    def __init__(self, ambientTemperature, daySetPointTemperature, nightSetPointTemperature, antiFreezeSetPointTemperature, derogation, sensorInfluence, startTemperature = None):
        self.ambientTemperature = ambientTemperature
        self.daySetPointTemperature = daySetPointTemperature
        self.nightSetPointTemperature = nightSetPointTemperature
        self.antiFreezeSetPointTemperature = antiFreezeSetPointTemperature
        self.derogation = derogation
        self.sensorInfluence = sensorInfluence
        self.startTemperature = startTemperature

        self.isDhw = self.derogation & 0x10 == 0x10
        self.isAuto = self.derogation & 0x8 == 0x8
        self.isDay = self.derogation & 0x4 == 0x04
        self.isNight = self.derogation & 0x2 == 0x2
        self.isAntifreeze = self.derogation & 0x1 == 0x1