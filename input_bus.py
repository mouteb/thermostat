from datetime import datetime

class InputBus():
    
    def __init__(self, history_date):
        self.history_date = history_date
        self.sensors = list()
        self.histories = list()
        self.dates = list()
        
    def add_sensor(self,sensor):
        self.sensors.append(sensor)
        self.histories.append(list())
    
    def read_inputs(self):
        self.dates.append(datetime.now())
        mesured_values = list()
        for sensor_index, sensor in enumerate(self.sensors):
            readed_values = sensor.get_mesured_values()
            self.histories[sensor_index].append(readed_values)
            for i, readed_value in enumerate(readed_values):
                mesured_values.append((sensor.name, sensor.mesured_quantities[i],[item[i] for item in self.histories[sensor_index]],sensor.mesured_unities[i]))
            #remove old histories
        print(self.dates[-1])
        print(datetime.now() - self.history_date)
        while len(self.dates)>0 and self.dates[-1]<datetime.now() - self.history_date:
              print("supprimée")
              print(datetime.now()- self.history_date)
              self.dates.pop(-1)
        return mesured_values
