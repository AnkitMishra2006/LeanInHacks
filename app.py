from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 




if __name__ == '__main__':
    app.run(port=5001, debug=True)