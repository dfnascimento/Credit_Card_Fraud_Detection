import os
import joblib
from flask import Blueprint, jsonify, request
from flasgger.utils import swag_from
from config import *
from api.transaction_features import TransactionFeatures
from datetime import datetime

predict = Blueprint('predict', __name__ )

try:
    model = joblib.load(MODEL_PATH)
    print(f"Modelo carregado: {MODEL_PATH}")
except Exception as e:
    print(f"Erro ao carregar modelo: {e}")
    model = None
  
try:
    scaler = joblib.load(SCALER_PATH)
    print(f"Scaler carregado: {SCALER_PATH}")
except:
    print("Scaler não encontrado, usando dados originais")
    scaler = None



@predict.route('/', methods=['GET'])
def get_predict():
    try:
        # Verificar se o modelo está carregado
        if model is None:
            return jsonify({"error": "Modelo não carregado"}), 500

        # Obter dados do request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "Nenhum JSON enviado"}), 400

        # Validar e criar objeto de transação
        transaction = TransactionFeatures(data)
        df_transaction = transaction.to_dataframe()
        
        df_transaction = transaction.pre_processing(df_transaction)
        
        # Aplicar scaler se existir
        if scaler is not None:
            df_transaction[['Amount', 'Hour']] = scaler.transform(df_transaction[['Amount', 'Hour']] )

        # Fazer predição 
        prediction = int(model.predict(df_transaction)[0])
        
        response = {
            "prediction": prediction,  # 0 ou 1
            "timestamp": datetime.now().isoformat()
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": f"Erro na predição: {str(e)}"}), 500
