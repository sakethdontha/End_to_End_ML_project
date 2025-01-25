from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlproject.pipeline.prediction import PredictionPipeline
import logging

app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to show the predictions in a web UI
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            gre_score =float(request.form['gre_score'])
            toefl_score =float(request.form['toefl_score'])
            university_rating =int(request.form['university_rating'])
            sop =int(request.form['sop'])
            lor  =int(request.form['lor'])
            cgpa =float(request.form['cgpa'])
            research =int(request.form['research'])
       
         
            data = [gre_score,toefl_score,university_rating,sop,lor,cgpa,research]
            data = np.array(data).reshape(1, 7)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)
            predict=predict*100
            print(f"Raw Prediction: {predict}")
            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)