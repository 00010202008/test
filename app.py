from flask import Flask, request, send_from_directory
import datetime

app = Flask(__name__)

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Handle geolocation data
@app.route('/store')
def store_data():
    lat = request.args.get('lat')
    long = request.args.get('long')
    uagent = request.args.get('uagent')
    timestamp = datetime.datetime.now().isoformat()

    log_entry = f"[{timestamp}] lat={lat}, long={long}, uagent={uagent}\n"

    with open("logs.txt", "a") as f:
        f.write(log_entry)

    return "Logged"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
