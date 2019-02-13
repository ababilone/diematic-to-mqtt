#!/usr/bin/env python
# coding=utf-8
import schedule
import time
from DiematicToMqttWorker import DiematicToMqttWorker

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