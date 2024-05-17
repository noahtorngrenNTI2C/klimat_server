#!/usr/bin/env python3
# Noah Törngren 2024-05-17
# biblotek för att kommunicera med hjälp av serial
import serial

# Deklarering av bilbloteket för att communisera med arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

# hjälpfunktion för att läsa sensorn
def readSensor():
    line = ser.readline().decode('ascii').rstrip()
    return line

# funktion för att få temperaturen från sensorn, retunerar en string
def getTemperature():
    line = readSensor()
    text = line.split(" ")
    try:
        temp = text[0]
    except:
        temp = "nan"
    return temp

# funktion för att få luftfuktigheten retunerar en string
def getHumidity():
    line = readSensor()
    text = line.split(" ")
    try:
        hum = text[1]
    except:
        hum = "nan"
    
    return hum

# funktion för att se om det regnar retunerar en string
def getRain():
    line = readSensor()
    text = line.split(" ")
    try:
        rain = text[2]
    except:
        rain = "nan"
    return rain
