from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json.get('data')
    with open('data.txt', 'w') as f:
        f.write(data)
    return {'message': 'Datos recibidos'}

@app.route('/fetch', methods=['GET'])
def fetch():
    try:
        with open('data.txt', 'r') as f:
            data = f.read()
        return jsonify({'data': data})
    except FileNotFoundError:
        return jsonify({'data': 'No hay datos aún'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
