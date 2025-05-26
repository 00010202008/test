from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_location', methods=['POST'])
def log_location():
    data = request.json
    lat = data.get('latitude')
    lon = data.get('longitude')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('log.txt', 'a') as f:
        f.write(f"{timestamp} - Lat: {lat}, Lon: {lon}\n")

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
