import pickle
import json
import pandas as pd

def basic(request):
    with open('./models/basic_model.pkl', 'rb') as f:
        vector = pd.DataFrame([request])
        model = pickle.load(f)
        stage = model.predict(vector)
    return stage

def detailed(request):
    with open('./models/detailed_model.pkl', 'rb') as f:
        vector = pd.DataFrame([request])
        model = pickle.load(f)
        stage = model.predict(vector)
    return stage

if __name__ == "__main__":
    with open("./request_example/basic.json", "r") as f:
        basic_data = json.load(f)
    print(f"Stage for person with basic data: {basic(basic_data)[0]}")

    with open("./request_example/detailed.json", "r") as f:
        detailed_data = json.load(f)
    print(f"Stage for person with detailed data: {detailed(detailed_data)[0]}")