from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open('gwp.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/predict")
def predict_page():
    return render_template('predict.html')

@app.route("/submit")
def submit_page():
    return render_template('submit.html')

@app.route("/pred", methods=['POST'])
def predict():
    quarter = request.form['quarter']
    department = request.form['department']
    day = request.form['day']
    team = request.form['team']
    targeted_productivity = request.form['targeted_productivity']
    smv = request.form['smv']
    over_time = request.form['over_time']
    incentive = request.form['incentive']
    idle_time = request.form['idle_time']
    idle_men = request.form['idle_men']
    no_of_style_change = request.form['no_of_style_change']
    no_of_workers = request.form['no_of_workers']
    month = request.form['month']

    # Convert inputs into array
    total = [[int(quarter), int(department), int(day), int(team),
              float(targeted_productivity), float(smv), int(over_time), int(incentive),
              float(idle_time), int(idle_men), int(no_of_style_change), float(no_of_workers), int(month)]]
    
    print(total)

    # Prediction
    prediction = model.predict(total)
    prediction = prediction[0]  # take first element

    if prediction <= 0.3:
        text = 'The employee is averagely productive.'
    elif 0.3 < prediction <= 0.82:
        text = 'The employee is medium productive.'
    else:
        text = 'The employee is highly productive.'

    return render_template('submit.html', prediction_text=text)

if __name__ == '__main__':
    app.run(debug=True)
