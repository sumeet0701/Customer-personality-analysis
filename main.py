import os
import sys
import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from cpa.logger.log import logging
from cpa.config.configuration import CpaConfiguration
from cpa.exception.exception_handler import CpaException
from cpa.pipeline.training_pipeline import TrainingPipeline

# pipe = pickle.load(open('Model/pipe.pkl', 'rb'))


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    try:
        return render_template("index.html")
    except Exception as e:
            raise CpaException(e, sys) from e



@app.route('/train',methods=['POST','GET'])
def train():
    if request.method == 'POST':
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            logging.info("Training Completed!")
            return render_template("index.html")

        except Exception as e:
            raise CpaException(e, sys) from e



@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def predict():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Income =float(request.form['Income'])
            Recency =int(request.form['Recency'])
            Age =int(request.form['Age'])
            TotalSpendings =int(request.form['TotalSpendings'])
            Children =int(request.form['Children'])
            MonthEnrollement =int(request.form['MonthEnrollement'])

            data = [Income,Recency,Age,TotalSpendings,Children,MonthEnrollement]
            model = pickle.load(open(CpaConfiguration().get_prediction_config().trained_model_path,'rb'))
            output = model.predict([data])[0]
            print(output)

            return render_template('results.html', prediction = str(output))

        except Exception as e:
            raise CpaException(e, sys) from e

    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(host="127.0.0.1", port=5000,debug=True)