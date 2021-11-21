from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('decisionTree.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        a = float(request.form['a'])
        b = float(request.form['b'])
        c = int(request.form['c'])
        d = int(request.form['d'])
        e = int(request.form['e'])
        f = int(request.form['f'])
        g = int(request.form['g'])
        h = int(request.form['h'])
        i = int(request.form['i'])

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

