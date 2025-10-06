import os
import joblib
from flask import Flask, request, jsonify
from flasgger import Swagger
from datetime import datetime
from api.predict import predict
from config import *


app = Flask(__name__)

app.register_blueprint(predict, url_prefix='/predict')


@app.route('/')
def home():
    return jsonify({
        "message": "API de Detecção de Fraudes - Cartão de Crédito",
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "endpoints": {
            "predict": "/predict (POST)",

        }
    })


if __name__ == '__main__':
    app.run(debug=True)