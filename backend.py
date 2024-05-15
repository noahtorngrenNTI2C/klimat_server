from flask import Flask, render_template
import get_sensor_value

app = Flask(__name__, template_folder='template')

# create some routes
@app.route('/')
def index():
    try:
        temp = get_sensor_value.getTemperature()
    except:
        temp = "nan"
    
    try:
        hum = get_sensor_value.getHumidity()
    except:
        hum = "nan"
    
    try: 
        rain = get_sensor_value.getRain()
    except:
        rain = "nan"

    return render_template('index.html',hum=hum,temp=temp,rain=rain) # plus allt som ska sättas in

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)