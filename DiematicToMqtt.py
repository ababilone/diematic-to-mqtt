#!/usr/bin/env python
# coding=utf-8

from DiematicToMqttWorker import DiematicToMqttWorker

def main():
   
    diematicToMqttWorker = DiematicToMqttWorker()
    diematicToMqttWorker.run()

    # if needed, could be used as a Thread
    # diematicToMqttWorker.start()
    # diematicToMqttWorker.stop()

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Quitting.")