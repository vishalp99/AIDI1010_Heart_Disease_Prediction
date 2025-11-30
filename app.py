from flask import Flask, render_template, request
import numpy as np
import pickle

# --- Load TPOT model ---
with open('files/tpot_model.pkl', 'rb') as f:
    model = pickle.load(f)

# --- Initialize Flask app ---
app = Flask(__name__)

# --- Features expected by the TPOT pipeline ---
features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
            'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

# --- Define which features are numeric (for reference) ---
num_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

# --- Home route ---
@app.route('/')
def main():
    return render_template('index.html')

# --- Prediction route ---
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # --- Get form values ---
        age = float(request.form['age'])
        sex = int(request.form['sex'])
        cp = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])

        # --- Create input dictionary ---
        input_dict = {
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal
        }

        # --- Convert to array in correct order ---
        input_list = [input_dict[col] for col in features]
        input_array = np.array(input_list).reshape(1, -1)

        # --- Predict using TPOT pipeline ---
        prediction = model.predict(input_array)[0]

        # --- Output message ---
        output = "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"

        return render_template('index.html', prediction_text=output)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")


# --- Run the app ---
if __name__ == "__main__":
    app.run(debug=True)
