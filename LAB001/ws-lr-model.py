# To start this web service run at the command line:
# flask --app ws-lr-model.py run

from flask import Flask, request, jsonify
from datetime import datetime
import pickle
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    now = datetime.now()
    return f"<h1>Hello FIAP - {now}</h1>"

@app.route("/calc/<a>/<b>")
def calc(a, b):
    output = {"sum": float(a) + float(b),
              "mult": float(a) * float(b),
              "max" : max([float(a),float(b)]),
              "min" : min([float(a),float(b)]),
              "average" : (float(a)+float(b))/2,
              "power" : float(a)**float(b)}              
                            
    return jsonify(output)

@app.route("/echo", methods = ['POST'])
def echo_service():
    #Obter os dados enviado via HTTP o JSON
    json_data = request.get_json()

    json_data["_status"] = "Echo Service"
    json_data["_college"] = "FIAP"
    json_data["_now"] = str(datetime.now())
    json_data["_luck_number"] = random.random()*1000
    
    return jsonify(json_data)

@app.route("/diabetes", methods = ['POST'])
def diabetes_model():
    # Ler o modelo de rl
    filename = 'lr_model.sav'
    lr_model = pickle.load(open(filename, 'rb'))

    #Obter os dados enviado via HTTP o JSON
    test_data = request.get_json()

    #Usar JSON recebido para teste, no modelo de RL previamente treinado
    prediction = lr_model.predict(test_data)

    # Retorna resultado
    return jsonify(list(prediction))


