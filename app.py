from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/capteurs', methods=['GET'])
def get_data():
    data = {"temperature": 24.5, "humidite": 65, "timestamp": "2025-05-03T14:10:00"}
    response = jsonify(data)
    response.headers["Content-Type"] = "application/json"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
