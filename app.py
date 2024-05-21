# File: app.py

from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load the model and preprocessor
model = load_model('esg_model.keras')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([data['features']])
    # Define the column names as per the preprocessor's expectations
    feature_names = ['Year', 'Country of Headquarters', 'Standard Industry Classification Code',
                     'Fiscal Year-end Month',
                     'Long-Term Debt - Total', 'Revenue - Total', 'Stockholders Equity - Total',
                     'Com Shares Outstanding - Issue',
                     'Net Income (Loss) - Consolidated', 'price - close monthly', 'currency']

    # Convert the features into a DataFrame with appropriate column names
    df_features = pd.DataFrame(features, columns=feature_names)

    preprocessed_features = preprocessor.transform(df_features)
    prediction = model.predict(preprocessed_features)
    # Round the prediction to two decimal places
    rounded_prediction = round(float(prediction[0][0]), 2)

    return jsonify({'prediction': rounded_prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
