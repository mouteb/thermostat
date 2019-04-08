from flask import Flask
from temperature_sensor import TemperatureSensor
from datetime import datetime, timedelta
from regulator import *

app = Flask(__name__)

temperature_sensor = TemperatureSensor(4,"Indoor humidity/temperature")

regulator = Regulator(timedelta(days=1),timedelta(seconds=15))
regulator.add_input(temperature_sensor)
regulator.start()

@app.route('/')
def index():
    mesured_field = regulator.actualize()
    page = str()
    for value in mesured_field:
        print(value)
        page = page + "<p>" + value[0]+": " + value[1] +" = " + str(value[2][0])+value[3]+".</p>"
    for value in mesured_field[1][2]:
        page = page + "<p>" + str(value)+".</p>"
    return page

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
