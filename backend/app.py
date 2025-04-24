from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/stocks', methods=['GET'])

def get_stocks():
    return jsonify({"answer":"5"})

if __name__ == '__main__':
    app.run(debug=True,port=5001)