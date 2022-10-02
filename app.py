from logging import exception
from flask import Flask, request, render_template
import flask
import werkzeug

# Create the app object
app = Flask(__name__)


# importing function for calculations
from functions import basic_calculator

# Define calculator
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = basic_calculator(a,b,operation)
    try:
        return render_template('result.html', prediction_text=str(result))
    except ZeroDivisionError:
        return render_template('error.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
    
    
#La app tiene el unico fallo de ZeroDivisionError, no lo he conseguido arreglar ni hacer que se rediriga a otro html de error 404
