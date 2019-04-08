from input_bus import *
from datetime import datetime, timedelta
from sensor import *

class Regulator(Thread)
    
    def __init__(self, history_lenght, refresh_delay):
        self.history_lenght = history_lenght
        self.refresh_delay = refresh_delay.total_seconds()
        self.input_bus = input_bus = InputBus(history_lenght)
        
    def add_input(self, sensor):
        self.input_bus.add_sensor(sensor)
        sensor.start()
    
    def run(self):
        while(True):
            actualize()
            time.sleep(self.refresh_delay)
    
    def actualize(self):
        return input_bus.read_inputs()
    
