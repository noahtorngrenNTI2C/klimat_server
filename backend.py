# Noah Törngren 2024-05-17
from flask import Flask, render_template
import get_sensor_value

app = Flask(__name__, template_folder='template')

# create some routes
@app.route('/')
def index():
    
    temp = get_sensor_value.getTemperature()
    
    hum = get_sensor_value.getHumidity()

    rainResult = get_sensor_value.getRain()

    def rain():
        print(rainResult)
        if rainResult == "1":
            return "Ja"
        else:
            return "Nej"
    
    

    return render_template('index.html',hum=hum,temp=temp,rain=rain()) # plus allt som ska sättas in

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)