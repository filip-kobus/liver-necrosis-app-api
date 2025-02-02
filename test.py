import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# Sample JSON data for testing
basic_test_data = {
    "Age [days]": 10950,
    "Edema": 1,
    "Bilirubin [mg/dl]": 2.4,
    "Albumin [gm/dl]": 4.1,
    "Platelets [ml/1000]": 210.5,
    "Prothrombin [s]": 11
}

detailed_test_data = {
    "Age [days]": 18250,
    "Ascites": 0,
    "Hepatomegaly": 1,
    "Spiders": 0,
    "Edema": 2,
    "Bilirubin [mg/dl]": 8.9,
    "Cholesterol [mg/dl]": 250.3,
    "Albumin [gm/dl]": 3.2,
    "Copper [ug/day]": 150.0,
    "Platelets [ml/1000]": 180.0,
    "Prothrombin [s]": 14
}

def test_basic():
    """
    Test the /predict/basic endpoint.
    """
    url = f"{BASE_URL}/predict/basic"
    response = requests.post(url, json=basic_test_data)
    print("\n🔹 Testing Basic Model API:")
    print(f"Response Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

def test_detailed():
    """
    Test the /predict/detailed endpoint.
    """
    url = f"{BASE_URL}/predict/detailed"
    response = requests.post(url, json=detailed_test_data)
    print("\n🔹 Testing Detailed Model API:")
    print(f"Response Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

if __name__ == "__main__":
    print("🚀 Running API Tests...")
    
    # Test basic model API
    test_basic()
    
    # Test detailed model API
    test_detailed()
