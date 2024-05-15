#!/usr/bin/env python3
import serial


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

def readSensor():
    line = ser.readline().decode('ascii').rstrip()
    return line

def getTemperature():
    line = readSensor()
    text = line.split(" ")
    temp = text[0]
    return temp

def getHumidity():
    line = readSensor()
    text = line.split(" ")
    hum = text[1]
    return hum

def getRain():
    line = readSensor()
    text = line.split(" ")
    rain = text[2]
    
    return rain
