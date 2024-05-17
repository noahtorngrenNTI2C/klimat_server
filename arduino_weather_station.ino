// Noah Törngren

// alla biblotek
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

//Adafruit_BME280 bme; // I2C
Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI

unsigned long delayTime;

int sensorAnalogPin = A0;
int sensorDigitalpin = 8;

int sensorAnalogValue = 0;
int sensorDigitalValue = 0;


void setup() {
    Serial.begin(9600);
    pinMode(sensorDigitalpin, INPUT);
    while(!Serial);    // time to get serial running
    Serial.println(F("BME280 test"));

    unsigned status;
    
    // default settings
    status = bme.begin();  
    // You can also pass in a Wire library object like &Wire2
    // status = bme.begin(0x76, &Wire2)
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); Serial.println(bme.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1) delay(10);
    }
    
    Serial.println("-- Default Test --");
    delayTime = 500;

    Serial.println();
}


void loop() { 
    
    // alla mätvärden sparade som variabler
    float temp = getTemp();
    float hum = getHum();
    bool rain = getRainSensor();

    // skickar värderena till raspberrypi
    Serial.println(String(temp) + " " + String(hum) + " " + String(rain));

    delay(delayTime);
}

// funktion för att läsa av temeraturen på bme280 sensorn. Funktionen retunerar en float
float getTemp(){
  return bme.readTemperature();
}

// funktion för att läsa av luftfuktigheten på bme280 sensorn. Funktionen retunerar en float
float getHum(){
  return bme.readHumidity();
}

// funktion för att mäta om det regnar eller inte med rain sensorn. Retunerar boolean
bool getRainSensor() {

  if (analogRead(sensorAnalogPin) <900){
    return true;
  } else{
    return false;
  }
  
}
