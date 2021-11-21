from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('decisionTree.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    Source_Type=1
    Edu_Type=1
    if request.method == 'POST':
        # satisfaction_level = float(request.form['Satisfaction Level'])
        # last_evaluation = float(request.form['Last Evaluation'])
        # number_project = int(request.form['Number of Projects'])
        # average_montly_hours = int(request.form['Average Monthly Hours'])
        # time_spend_company = int(request.form['Time Spend Company'])
        # Work_accident = int(request.form['Work Accident'])
        # promotion_last_5years = int(request.form['Promotion Last 5 years'])
        # Departments = int(request.form['Department'])
        # salary = int(request.form['Salary'])

        a = float(request.form['Satisfaction Level'])
        b = float(request.form['Last Evaluation'])
        c = int(request.form['Number of Projects'])
        d = int(request.form['Average Monthly Hours'])
        e = int(request.form['Time Spend Company'])
        f = int(request.form['Work Accident'])
        g = int(request.form['Promotion Last 5 years'])
        h = int(request.form['Department'])
        i = int(request.form['Salary'])
  
        d = {'satisfaction_level': [a], 'last_evaluation': [b],'number_project': [c], 'average_montly_hours': [d],'time_spend_company': [e],'Work_accident': [f],'promotion_last_5years': [g],'Departments': [h],'salary': [i]}
        de = pd.DataFrame(data=d)
        prediction=model.predict(de)
        output=prediction
        if output<0:
            return render_template('index.html',prediction_texts="Sorry wrong input try again")
        else:
            if output == 1:
                output = 100
            if output == 0:
                output = 0
            return render_template('index.html',prediction_text="Your Chances of leaving are {} %".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

