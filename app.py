from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route to render HTML
@app.route('/')
def home():
    return render_template('index.html')

# API to get sensor data
@app.route('/health-monitoring-system/get-sensor-data.php', methods=['GET'])
def get_sensor_data():
    # Here, you'll fetch data from your IoT device
    sensor_data = {
        'temperature': 37,  # Example value, replace with actual sensor value
        'pulse': 80  # Example value, replace with actual pulse rate
    }
    return jsonify(sensor_data)

# API to control device (buzzer)
@app.route('/health-monitoring-system/control-device.php', methods=['POST'])
def control_device():
    action = request.json.get('action')
    if action == 'ON':
        # Code to turn on buzzer
        return jsonify({'message': 'Buzzer turned ON'})
    elif action == 'OFF':
        # Code to turn off buzzer
        return jsonify({'message': 'Buzzer turned OFF'})
    return jsonify({'message': 'Invalid action'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
