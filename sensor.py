from statistics import mean
from threading import Thread, RLock
import time


class Sensor(Thread):

    NUMBER_OF_VALUES = 10
    DELAY_INTERVAL = 5

    def __init__(self, pin_number, name):
        Thread.__init__(self)
        self.pin_number = pin_number
        self.name = name
        self.mesured_values = list()
        self.mesured_quantities = list()
        self.mesured_unities = list()
        self.lock = RLock()
        self.new_reading()
        
    def run(self):
        while(True):
            self.new_reading()
            time.sleep(Sensor.DELAY_INTERVAL)

    def read_values(self):
        pass
    
    def new_reading(self):
        new_value = self.read_values()
        valid_data = True
        for value in new_value:
            if value is None:
                valid_data = False
                break
        if valid_data:
            with self.lock:
                 if len(self.mesured_values)>Sensor.NUMBER_OF_VALUES-1:
                     self.mesured_values.pop(0)
                 self.mesured_values.append(new_value)

    
    def get_mesured_values(self):
        returned_values = list()
        copied_values = list(self.mesured_values)
        for i in range(len(self.mesured_values[0])):
            filtered = [item[i] for item in copied_values]
            M = max(filtered)
            m = min(filtered)
            print("Liste: " + str(filtered))
            print("max: " + str(M))
            print("min: " + str(m))
            if len(self.mesured_values)>2:                    
                filtered.remove(m)
                filtered.remove(M)
            mean_value = mean(filtered)
            returned_values.append(mean_value)
        return returned_values
        
                
