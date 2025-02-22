from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from predictFuncs import * 
from graphFuncs import *

app = Flask(__name__)
CORS(app)  

@app.get("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sYear = int(request.form.get('startYear'))
    # eYear = request.form.get('endYear')    
    month = int(request.form.get('month'))

    predictions = {}
    predictions["temp"] = LTpredict(sYear, month) 
    predictions["seaLevel"] = SLpredict(sYear, month)
    predictions["co2"] = COpredict(sYear, month)
    predictions["ch4"] = CHpredict(sYear, month)

    plots = {}
    plots["ltPlot"] = LTplot(sYear)
    plots["slPlot"] = SLplot(sYear)
    plots["coPlot"] = COplot(sYear)


    return render_template('output.html', data = predictions, plots = plots)
    # return f"Predicted Data: Temperature - {predictions['temp']}, CO₂ Level - {predictions['co2']} ppm, sea level - {predictions['seaLevel']}"

@app.route('/plot', methods=['POST'])
def plot():
    sYear = int(request.form.get('startYear'))
    # eYear = request.form.get('endYear')    
    month = int(request.form.get('month'))

    plots = {}
    plots["ltPlot"] = LTplot(sYear)
    plots["slPlot"] = SLplot(sYear)
    plots["coPlot"] = COplot(sYear)

    return render_template('plot.html', plot = plots)
    
if __name__ == '__main__':
    app.run(debug=True, port=8080)
