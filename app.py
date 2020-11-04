# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import math
import re

from datetime import datetime


app = Flask(__name__)
CORS(app)
historial = []
number_regex = "^-?[0-9]\d*(\.\d+)?$"
                                #########################################
                                #################RECIPES#################
                                #########################################





@app.route('/suma/',methods=['POST'])
def suma():
    

    data = json.loads(request.data)
    number1 = data.get('number1', None)
    number2 = data.get('number2', None)
    operationType = "suma"

    result = None


    list = [data,number1,number2]
    for element in list:
        if (not element or element == ""):
            return jsonify({
            "RESULT": "No ha brindado toda la informacion necesaria",
            "RETURNCODE" : "-1",
            "METHOD" : "POST"
            })



    if (not re.search(number_regex,number1) or not re.search(number_regex,number2)):
        return jsonify({
            "RESULT": "No han ingresado numeros validos",
            "RETURNCODE" : "1",
            "METHOD" : "POST"
        })

    result = float(number1) + float(number2)
    now = datetime.now()
    data = {
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "number1": number1,
        "number2": number2,
        "operation_type": operationType,
        "result": result
    }



    historial.append([now,float(number1),float(number2),operationType,result])


    return jsonify({
        "RESULT": data,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })



@app.route('/resta/',methods=['POST'])
def resta():
    

    data = json.loads(request.data)
    number1 = data.get('number1', None)
    number2 = data.get('number2', None)
    operationType = "resta"

    result = None


    list = [data,number1,number2]
    for element in list:
        if (not element or element == ""):
            return jsonify({
            "RESULT": "No ha brindado toda la informacion necesaria",
            "RETURNCODE" : "-1",
            "METHOD" : "POST"
            })

    if (not re.search(number_regex,number1) or not re.search(number_regex,number2)):
        return jsonify({
            "RESULT": "No han ingresado numeros validos",
            "RETURNCODE" : "1",
            "METHOD" : "POST"
        })

    result = float(number1) - float(number2)
    now = datetime.now()
    data = {
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "number1": number1,
        "number2": number2,
        "operation_type": operationType,
        "result": result
    }

    historial.append([now,float(number1),float(number2),operationType,result])
    return jsonify({
        "RESULT": data,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })

@app.route('/multiplicacion/',methods=['POST'])
def multiplicacion():
    

    data = json.loads(request.data)
    number1 = data.get('number1', None)
    number2 = data.get('number2', None)
    operationType = "multiplicacion"

    result = None


    list = [data,number1,number2]
    for element in list:
        if (not element or element == ""):
            return jsonify({
            "RESULT": "No ha brindado toda la informacion necesaria",
            "RETURNCODE" : "-1",
            "METHOD" : "POST"
            })

    if (not re.search(number_regex,number1) or not re.search(number_regex,number2)):
        return jsonify({
            "RESULT": "No han ingresado numeros validos",
            "RETURNCODE" : "1",
            "METHOD" : "POST"
        })

    result = float(number1) * float(number2)
    now = datetime.now()
    data = {
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "number1": number1,
        "number2": number2,
        "operation_type": operationType,
        "result": result
    }

    historial.append([now,float(number1),float(number2),operationType,result])
    return jsonify({
        "RESULT": data,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })

@app.route('/division/',methods=['POST'])
def division():
    

    data = json.loads(request.data)
    number1 = data.get('number1', None)
    number2 = data.get('number2', None)
    operationType = "division"

    result = None


    list = [data,number1,number2]
    for element in list:
        if (not element or element == ""):
            return jsonify({
            "RESULT": "No ha brindado toda la informacion necesaria",
            "RETURNCODE" : "-1",
            "METHOD" : "POST"
            })

    if (not re.search(number_regex,number1) or not re.search(number_regex,number2)):
        return jsonify({
            "RESULT": "No han ingresado numeros validos",
            "RETURNCODE" : "1",
            "METHOD" : "POST"
        })



    if (number2 == "0"):
        return jsonify({
            "RESULT": "Division por 0",
            "RETURNCODE" : "2",
            "METHOD" : "POST"
        })

    result = float(number1) / float(number2)
    now = datetime.now()
    data = {
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "number1": number1,
        "number2": number2,
        "operation_type": operationType,
        "result": result
    }

    historial.append([now,float(number1),float(number2),operationType,result])
    return jsonify({
        "RESULT": data,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })

@app.route('/potencia/',methods=['POST'])
def potencia():
    

    data = json.loads(request.data)
    number1 = data.get('number1', None)
    number2 = data.get('number2', None)
    operationType = "potencia"

    result = None


    list = [data,number1,number2]
    for element in list:
        if (not element or element == ""):
            return jsonify({
            "RESULT": "No ha brindado toda la informacion necesaria",
            "RETURNCODE" : "-1",
            "METHOD" : "POST"
            })

    if (not re.search(number_regex,number1) or not re.search(number_regex,number2)):
        return jsonify({
            "RESULT": "No han ingresado numeros validos",
            "RETURNCODE" : "1",
            "METHOD" : "POST"
        })

    result = pow( float(number1), float(number2))
    now = datetime.now()
    data = {
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "number1": number1,
        "number2": number2,
        "operation_type": operationType,
        "result": result
    }

    historial.append([now,float(number1),float(number2),operationType,result])
    return jsonify({
       "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "RESULT": data,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })


@app.route('/raiz/',methods=['POST'])
def raiz():

    data = json.loads(request.data)
    number1 = data.get('number1', None)
    number2 = data.get('number2', None)
    operationType = "raiz"

    result = None


    list = [data,number1,number2]
    for element in list:
        if (not element or element == ""):
            return jsonify({
            "RESULT": "No ha brindado toda la informacion necesaria",
            "RETURNCODE" : "-1",
            "METHOD" : "POST"
            })

    if (not re.search(number_regex,number1) or not re.search(number_regex,number2)):
        return jsonify({
            "RESULT": "No han ingresado numeros validos",
            "RETURNCODE" : "1",
            "METHOD" : "POST"
        })


    if (float(number1) < 0 and float(number2)%2 == 0):
        return jsonify({
            "RESULT": "Raiz par de numero negativo",
            "RETURNCODE" : "2",
            "METHOD" : "POST"
        })


    result = pow( float(number1), 1/float(number2))
    now = datetime.now()
    data = {
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "number1": number1,
        "number2": number2,
        "operation_type": operationType,
        "result": result
    }

    historial.append([now,float(number1),float(number2),operationType,result])
    return jsonify({
        "date": now.strftime("%d/%m/%Y %H:%M:%S"),
        "RESULT": data,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })

@app.route('/historial/',methods=['GET'])
#0:sucess
#1:Missing username
#2: No users found
def search_users():

    return jsonify({
        "RESULT": historial,
        "RETURNCODE" : "0",
        "METHOD" : "POST"
    })


@app.route('/')
def index():
    return jsonify({
            "MESSAGE": "BackEnd Python CUK",
            "RETURNCODE" : "0",
            "METHOD" : "POST"
        })

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


