# AIDI1010_Heart_Disease_Prediction

This is a **Heart Disease Prediction Web Application** built with **Flask**.  
It uses a **TPOT-generated machine learning pipeline** trained on the Cleveland Heart Disease dataset to predict the likelihood of heart disease based on patient clinical features.

---

**Live Demo on Render:** [Click here]()

> **Note:** If the app is loading slowly on first access, the Render free-tier web server may be starting up. Please be patient—it can take up to 30–60 seconds for the first request to respond.

This is a **Heart Disease Prediction Web Application** built with **Flask**.  
It uses a **TPOT-generated machine learning pipeline** trained on the Cleveland Heart Disease dataset to predict the likelihood of heart disease based on patient clinical features.

---

## **Features**

- Input **13 clinical features** from the Cleveland dataset:
  - `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`
- Uses **TPOT pipeline** for automated preprocessing, scaling, and prediction.
- Displays prediction results clearly:
  - **No Heart Disease Detected**
  - **Heart Disease Detected**
- Mobile-friendly and responsive HTML interface.

---

## **Project Structure**

├─ app.py # Flask application
├─ files/
│ ├─ tpot_model.pkl # Pre-trained TPOT model
│ └─ scaler.pkl # Preprocessing scaler
├─ templates/
│ └─ index.html # HTML form and display
├─ requirements.txt # Python dependencies
├─ .gitignore # Files/folders to ignore in Git
└─ README.md # This file

---

## **Installation (Local Setup)**

### 1️ Clone the repository

```bash
git clone https://github.com/vishalp99/AIDI1010_Heart_Disease_Prediction.git
cd AIDI1010_Heart_Disease_Prediction

```

### 2 Create a virtual environment 

```bash
python -m venv venv

```

### 3 Activate the virtual environment 

```bash

venv/Scripts/activate

```

### 4 Install dependencies

```bash

pip install -r requirements.txt

```

### 5 Run the Flask app 

```bash

python app.py 

```

### 6 Open in browser 

```bash

http://127.0.0.1:5000/

```

---
## **Sample Test Entries**

| Feature  | Value |
| -------- | ----- |
| age      | 35    |
| sex      | 0     |
| cp       | 0     |
| trestbps | 115   |
| chol     | 180   |
| fbs      | 0     |
| restecg  | 0     |
| thalach  | 175   |
| exang    | 0     |
| oldpeak  | 0.0   |
| slope    | 2     |
| ca       | 0     |
| thal     | 3     |


| Feature  | Value |
| -------- | ----- |
| age      | 63    |
| sex      | 1     |
| cp       | 3     |
| trestbps | 150   |
| chol     | 250   |
| fbs      | 1     |
| restecg  | 0     |
| thalach  | 120   |
| exang    | 1     |
| oldpeak  | 2.5   |
| slope    | 0     |
| ca       | 2     |
| thal     | 7     |

---

## **Dependencies**

- Python 3.11+

- Flask

- numpy

- scikit-learn

- tpot

---

## **Notes**

This project is for educational purposes only.
Do not use this app for real medical diagnosis.
Use realistic test values based on the Cleveland Heart Disease dataset.

--- 

## **License**

This project is released for educational use.

---