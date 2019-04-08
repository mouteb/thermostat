from flask import Flask
from temperature_sensor import TemperatureSensor
from input_bus import *
from datetime import datetime, timedelta

app = Flask(__name__)

temperature_sensor = TemperatureSensor(4,"Indoor humidity/temperature")
temperature_sensor.start()

input_bus = InputBus(timedelta(minutes=5))
input_bus.add_sensor(temperature_sensor)

@app.route('/')
def index():
    mesured_field = input_bus.read_inputs()
    print(mesured_field)
    page = str()
    for value in mesured_field:
        print(value)
        page = page + "<p>" + value[0]+": " + value[1] +" = " + str(value[2][0])+value[3]+".</p>"
    for value in mesured_field[1][2]:
        page = page + "<p>" + str(value)+".</p>"
    return page

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
