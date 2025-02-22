from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from predictFuncs import * 

app = Flask(__name__)
CORS(app)  

@app.get("/")
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))

    predictions = {}
    predictions["temp"] = LTpredict(year, month) 
    predictions["seaLevel"] = SLpredict(year, month)
    predictions["co2"] = COpredict(year, month)
    predictions["ch4"] = CHpredict(year, month)

    return render_template('output.html', data = predictions)
    # return f"Predicted Data: Temperature - {predictions['temp']}, CO₂ Level - {predictions['co2']} ppm, sea level - {predictions['seaLevel']}"

if __name__ == '__main__':
    app.run(debug=True, port=8080)
