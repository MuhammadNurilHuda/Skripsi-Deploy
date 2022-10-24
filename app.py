from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

col = [['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    model = joblib.load("diabetes_model.pkl")
    result = model.predict(to_predict)
    return result[0]

@app.route('/', methods=['GET', 'POST'])
def main():
    model = joblib.load("diabetes_model.pkl")
    if request.method== 'POST' :
        Pregnancies = int(request.form.get('Pregnancies'))
        Glucose = int(request.form.get('Glucose'))
        BloodPressure = int(request.form.get('BloodPressure'))
        SkinThickness = int(request.form.get('SkinThickness'))
        Insulin = int(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = int(request.form.get('Age'))
    
        X = pd.DataFrame([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]], columns=col)
        prediction = model.predict(X)[0]
        # to_predict_list = request.form.to_dict()
        # to_predict_list = list(to_predict_list.values())
        # to_predict_list = list(map(int, to_predict_list))
        # result = ValuePredictor(to_predict_list)
        
        if int(prediction)==1:
            prediction = 'positif diabetes'
        else:
            prediction = 'negatif diabetes'

    else:
        prediction = ""

    return render_template('index.html', prediction = prediction)


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port='5000')