class DiematicBurner(object):
    def __init__(self, startCount, operatingHours):
        self.galInLiter = 3.785411784
        self.galPerHourForBurner = 0.5
        self.fuelConsumptionPerWorkingHour = self.galPerHourForBurner * self.galInLiter
        
        self.totalStartCount = startCount
        self.totalOperatingHours = operatingHours        
        self.totalFuelConsumption = self.fuelConsumptionPerWorkingHour * self.totalOperatingHours