import sys
import time
from threading import Thread

import minimalmodbus
import schedule
from DiematicReader import DiematicReader
from DiematicHomie import DiematicHomie

class DiematicToMqttWorker(Thread):
    def __init__(self):
        super(DiematicToMqttWorker, self).__init__()

        self.cancelRequested = False
        self.diematic = None
        self.diematicHomie = DiematicHomie()

    def run(self):
        minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

        instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 10)
        instrument.serial.baudrate = 9600
        instrument.serial.bytesize = 8
        instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        instrument.serial.stopbits = 1
        instrument.serial.timeout = 1
        instrument.debug = False
        instrument.mode = minimalmodbus.MODE_RTU

        diematicReader = DiematicReader(instrument)

        schedule.every(15).seconds.do(self.publish)

        while not self.cancelRequested:
            try:
                self.diematic = diematicReader.read()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                pass
        
        print("Worker finished")

    def stop(self):
        self.cancelRequested = True

    def publish(self):
        self.diematicHomie.send(self.diematic)
