#!/usr/bin/env python
# coding=utf-8

from DiematicToMqttWorker import DiematicToMqttWorker

def main():
   
    diematicToMqttWorker = DiematicToMqttWorker()
    diematicToMqttWorker.run()

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("Quitting.")