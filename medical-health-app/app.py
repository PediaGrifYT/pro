from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

# Load ML model
with open("health_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Label Encoder
with open("label_encoder.pkl", "rb") as file:
    le = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.json['symptoms']
        
        # Convert input symptoms into feature array (One-Hot Encoding)
        input_features = np.zeros((1, len(data)))
        for symptom in data:
            if symptom in data:
                index = data.index(symptom)
                input_features[0, index] = 1

        # Predict disease
        prediction = model.predict(input_features)[0]
        disease_name = le.inverse_transform([prediction])[0]

        return jsonify({'disease': disease_name})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
