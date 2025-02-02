from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import cirrhosis_stages
import json

app = Flask(__name__)

CORS(app)

with open('./models/basic_model.pkl', 'rb') as f:
    basic_model = pickle.load(f)

with open('./models/detailed_model.pkl', 'rb') as f:
    detailed_model = pickle.load(f)

BASIC_FEATURES = ["Age [days]", "Edema", "Bilirubin [mg/dl]", "Albumin [gm/dl]",
                  "Platelets [ml/1000]", "Prothrombin [s]"]

DETAILED_FEATURES = ["Age [days]", "Ascites", "Hepatomegaly", "Spiders", "Edema",
                     "Bilirubin [mg/dl]", "Cholesterol [mg/dl]", "Albumin [gm/dl]",
                     "Copper [ug/day]", "Platelets [ml/1000]", "Prothrombin [s]"]

TRANSFORMATION = {
    "Yes":0,
    "No":1,
    "Yes but no diuretics":2
}

def preprocess_request(data, feature_order):
    """
    Converts JSON input into a DataFrame with the correct feature order.
    """
    try:
        for key, value in data.items():
            if value in TRANSFORMATION.keys():
                print(f"{data[key]} - {TRANSFORMATION[value]}")
                data[key] = TRANSFORMATION[value]
        data['Age [days]'] = data['Age']*365
        data.pop('Age')
        df = pd.DataFrame([data])
        df = df[feature_order]
        return df
    except KeyError as e:
        return f"Missing feature: {e}", 400  # Return error if a feature is missing


@app.route('/predict/basic', methods=['POST'])
def predict_basic():
    """
    Endpoint to predict stage using the basic model.
    """
    try:
        request_data = request.get_json()
        vector = preprocess_request(request_data, BASIC_FEATURES)

        if isinstance(vector, tuple):  # Check if preprocessing returned an error
            return jsonify({"error": vector[0]}), vector[1]

        prediction = basic_model.predict(vector)[0]
        return jsonify({"Stage": int(prediction),
                        "Accuracy": float(51.25),
                        "StageName": cirrhosis_stages.cirrhosis_stages[int(prediction)-1]["stage"],
                        "Description": cirrhosis_stages.cirrhosis_stages[int(prediction)-1]["description"]
                        }
                       )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/predict/detailed', methods=['POST'])
def predict_detailed():
    """
    Endpoint to predict stage using the detailed model.
    """
    try:
        request_data = request.get_json()
        vector = preprocess_request(request_data, DETAILED_FEATURES)

        if isinstance(vector, tuple):  # Check if preprocessing returned an error
            return jsonify({"error": vector[0]}), vector[1]

        prediction = detailed_model.predict(vector)[0]
        return jsonify({"Stage": int(prediction),
                        "Accuracy": float(50.22),
                        "StageName": cirrhosis_stages.cirrhosis_stages[int(prediction)-1]["stage"],
                        "Description": cirrhosis_stages.cirrhosis_stages[int(prediction)-1]["description"]}
                       )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
