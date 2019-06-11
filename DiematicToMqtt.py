#!/usr/bin/python3
# coding=utf-8
import schedule
import time
from DiematicToMqttWorker import DiematicToMqttWorker
from logging.handlers import RotatingFileHandler
import logging
rotatingFileHandler = RotatingFileHandler('/var/log/diematic/diematic.log', maxBytes=5*1024*1024, backupCount=5)
logging.basicConfig(handlers=[rotatingFileHandler], level=logging.INFO)

diematicToMqttWorker = DiematicToMqttWorker()

def main():
   
    diematicToMqttWorker.start()

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':

    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        diematicToMqttWorker.stop()
        print("Quitting.")