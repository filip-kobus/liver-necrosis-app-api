from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('./models/basic_model.pkl', 'rb') as f:
    basic_model = pickle.load(f)

with open('./models/detailed_model.pkl', 'rb') as f:
    detailed_model = pickle.load(f)

BASIC_FEATURES = ["Age [days]", "Edema", "Bilirubin [mg/dl]", "Albumin [gm/dl]", 
                  "Platelets [ml/1000]", "Prothrombin [s]"]

DETAILED_FEATURES = ["Age [days]", "Ascites", "Hepatomegaly", "Spiders", "Edema",
                     "Bilirubin [mg/dl]", "Cholesterol [mg/dl]", "Albumin [gm/dl]",
                     "Copper [ug/day]", "Platelets [ml/1000]", "Prothrombin [s]"]

def preprocess_request(data, feature_order):
    """
    Converts JSON input into a DataFrame with the correct feature order.
    """
    try:
        df = pd.DataFrame([data])
        df = df[feature_order]  # Ensure correct feature order
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
        return jsonify({"Stage": int(prediction)})  # Convert NumPy type to standard int
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
        return jsonify({"Stage": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
