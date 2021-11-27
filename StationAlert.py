#!/bin/sh
# this is built by Alaskaradar with the help of many others that have come before
# Thank you for your trials and posts online to help me with my project.
from __future__ import absolute_import
from __future__ import print_function
import time
import sys
from time import sleep
from socket import *
from select import *
from tkinter import *
import subprocess
import os
import RPi.GPIO as GPIO
import threading
from threading import Thread
import re
from six.moves import range

Relay1 = [26]
Relay2 = [20]
Relay3 = [21]


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Relay1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Relay2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Relay3, GPIO.OUT, initial=GPIO.LOW)
    print("|=====================================================|")
    print("|                 Internet tower light                |")
    print("|-----------------------------------------------------|")
    print("|                                                     |")
    print("|                  Internet monitoring                |")
    print("|                  Remote Light station               |")
    print("|                                                     |")
    print("|                      Raspberry pi                   |")
    print("|                      relay hat                      |")
    print("|                                          Alaskaradar|")
    print("|_____________________________________________________|")
    print("|             System online and Standing by           |")
    print("|_____________________________________________________|")


def main():
    while True:	
        s = socket(AF_INET, SOCK_DGRAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(('', 50000))
        rx = s.recvfrom(2048)
        print('Received:' ,repr(rx))
        #rx = s.recv(1024)

        #for line in rx:
        if "RED" in str(rx):
            print(" Siren Triggered")
            GPIO.output(Relay1, GPIO.HIGH)
            GPIO.output(Relay3, GPIO.HIGH)
            #timer()

        #for line in rx:
        if "YELLOW" in str(rx):
            print("Page Received")
            GPIO.output(Relay1, GPIO.HIGH)
            GPIO.output(Relay2, GPIO.HIGH)
            #timer()

        #for line in rx:
        if "GREEN" in str(rx):
            print("Victor QRU Page received")
            GPIO.output(Relay1, GPIO.HIGH)
            GPIO.output(Relay2, GPIO.HIGH)
            GPIO.output(Relay3, GPIO.HIGH)
            #timer()

        #for line in rx:
        if "CHANGEME" in str(rx):
            print("Relay test")
            GPIO.output(Relay1, GPIO.HIGH)
            GPIO.output(Relay2, GPIO.HIGH)
            GPIO.output(Relay3, GPIO.HIGH)
            print("on")
            sleep(1.0)
            GPIO.output(Relay1, GPIO.LOW)
            GPIO.output(Relay2, GPIO.LOW)
            GPIO.output(Relay3, GPIO.LOW)
            print("off")
            sleep(1.0)
            GPIO.output(Relay1, GPIO.HIGH)
            GPIO.output(Relay2, GPIO.HIGH)
            GPIO.output(Relay3, GPIO.HIGH)
            print("on")
            sleep(1.0)
            GPIO.output(Relay1, GPIO.LOW)
            GPIO.output(Relay2, GPIO.LOW)
            GPIO.output(Relay3, GPIO.LOW)
            print("off")
            print(" ")
            print("System Standing By.....")
            main()


#def timer():
#    for remaining in range(120, 0, -1):
#        sys.stdout.write(str(remaining)+' Seconds Remaining.\r')
#        sys.stdout.flush()
#        time.sleep(1)

    sys.stdout.write("\rSystem Standing By....\n")
    main()


def destroy():
    GPIO.output(Relay1, GPIO.HIGH)
    GPIO.output(Relay2, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
