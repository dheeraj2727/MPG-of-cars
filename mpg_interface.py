from flask import Flask, request, jsonify, render_template
from utils import MPG
import config

app = Flask(__name__)

@app.route('/mpg_model')
def home1():
    
    return render_template('mpg_predict.html')

@app.route('/predict_mpg', methods = ['GET', 'POST'])
def predict_mpg():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        Cylinders = float(data('Cylinders'))
        Displacement = float(data('Displacement'))
        Horsepower = float(data('Horsepower'))
        Weight = float(data('Weight'))
        Acceleration = float(data('Acceleration'))
        Model_Year=eval(data('Model_Year'))
        Origin = data('Origin')

        Obj = MPG(Cylinders,Displacement,Horsepower,Weight,Acceleration,Model_Year,Origin)
        predict_mpg = Obj.get_predicted_mpg()
        
        return render_template('mpg_predict.html', prediction = predict_mpg)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
        Cylinders      = data['Cylinders']
        Displacement   = data['Displacement']
        Horsepower      = data['Horsepower']
        Weight = data['Weight']
        Acceleration   = data['Acceleration']
        Model_Year   = data['Model_Year']
        Origin   = data['Origin']

        Obj = MPG(Cylinders,Displacement,Horsepower,Weight,Acceleration,Model_Year,Origin)
        predict_mpg = Obj.get_predicted_mpg()
        
        return render_template('mpg_predict.html', prediction = predict_mpg)

    return jsonify({"Message" : "Unsuccessful"})

if __name__== "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)