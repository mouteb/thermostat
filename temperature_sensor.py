import Adafruit_DHT
from threading import Thread, RLock
from sensor import *


class TemperatureSensor(Sensor):

    def __init__(self, pin_number, name):
        Sensor.__init__(self, pin_number,name)
        self.mesured_quantities.append("Humidity")
        self.mesured_quantities.append("Temperature")
        self.mesured_unities.append("%")
        self.mesured_unities.append("°C")
        
    def read_values(self):
        mesured_values = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302,self.pin_number)
        print("New temperature: " + str(mesured_values[1]))
        print("New humidity: " + str(mesured_values[0]))
        return mesured_values
        
                
