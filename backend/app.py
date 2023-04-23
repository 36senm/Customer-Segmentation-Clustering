from urllib import response
from flask import Flask, request, jsonify
import pandas as pd
import pickle


app = Flask(__name__)

fraud_clases = ["0", "1"]
column = ['distance_from_home',
          'distance_from_last_transaction',
          'ratio_to_median_purchase_price',
          'repeat_retailer',
          'used_chip',
          'used_pin_number',
          'online_order']
       
with open("dt_pipe_model.pkl", "rb") as f:
    model_fraud = pickle.load(f)


@app.route("/")
def home():
    return "<h1>Backend App Fraud Detection</h1>"


@app.route("/fraud", methods=['GET', 'POST'])
def fraud_inference ():
    if request.method == 'POST':
        data = request.json
        new_data = [data['distance_from_home'],
                    data['distance_from_last_transaction'],
                    data['ratio_to_median_purchase_price'],
                    data['repeat_retailer'],
                    data['used_chip'],
                    data['used_pin_number'],
                    data['online_order']]
        new_data = pd.DataFrame([new_data], columns=column)
        res = model_fraud.predict(new_data)
        response = {'code': 200, 'status': 'Success', 
                    'result':{'prediction': str(res[0]),
                    'classes': fraud_clases[res[0]]}}
        return jsonify(response)

    return "Silahkan gunakan method post untuk mengakses model"
app.run(debug=True)