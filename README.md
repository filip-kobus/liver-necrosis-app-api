# 🏥 Liver Necrosis Prediction API

This project provides a **Flask API** for predicting the stage of **liver necrosis** based on patient data.  
The API accepts **basic** and **detailed** patient records in **JSON format** and returns a **predicted stage** using machine learning models.

---

## :exclamation: Model
The model used was a Decision Tree Classifier. For detailed information, refer to the repository:

[Cirrhosis Classification Model](https://github.com/filip-kobus/cirrhosis-classification-model)

## :exclamation: UI Implementation
The UI was built with React, focusing on responsiveness and user-friendly design. For detailed information, refer to the repository:

[UI Implementation Repository](https://github.com/Szymon-Stasiak/liver-necrosis-app-ui)


## 📌 Features
✅ REST API using **Flask**  
✅ Supports **Basic** and **Detailed** prediction models  
✅ Takes JSON input and returns the predicted **liver necrosis stage**  
✅ Uses **Pickle** to load pre-trained models  
✅ Includes an automated **API testing script**  

---

## 📂 Project Structure
```
📁 liver-necrosis-app
│── 📁 models                     # Contains trained ML models (.pkl)
│   ├── basic_model.pkl
│   ├── detailed_model.pkl
│
│── 📁 request_example             # Example JSON requests
│   ├── basic.json
│   ├── detailed.json
│
│── app.py                         # Main API server
│── test_api.py                     # Script to test API endpoints
│── requirements.txt                 # Dependencies
│── README.md                       # Project Documentation
```

---

## 🚀 Setup & Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo/liver-necrosis-api.git
cd liver-necrosis-api
```

### 2️⃣ **Create Virtual Enviroment**
```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements
```

### 4️⃣ **Run the API**
```bash
python app.py
```
API will start at: `http://127.0.0.1:5000/`

---

## 📡 API Endpoints

### ➤ **Predict Stage (Basic Model)**
**Endpoint:** `/predict/basic`  
**Method:** `POST`  
**Example Request:**
```json
{
    "Age [days]": 10950,
    "Edema": 1,
    "Bilirubin [mg/dl]": 2.4,
    "Albumin [gm/dl]": 4.1,
    "Platelets [ml/1000]": 210.5,
    "Prothrombin [s]": 11
}
```
**Example Response:**
```json
{"Stage": 3}
```

### ➤ **Predict Stage (Detailed Model)**
**Endpoint:** `/predict/detailed`  
**Method:** `POST`  
**Example Request:**
```json
{
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
```
**Example Response:**
```json
{"Stage": 4}
```

---

## 🛠 Running API Tests
You can test the API using `test_api.py`:

```bash
python test_api.py
```

Expected Output:
```
🚀 Running API Tests...

🔹 Testing Basic Model API:
Response Code: 200
Response JSON: {"Stage": 3}

🔹 Testing Detailed Model API:
Response Code: 200
Response JSON: {"Stage": 4}
```

---

## 📜 License
This project is **open-source**. Modify and use as needed.

