from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Linear Regression Service Running"

@app.route('/preprocess', methods=['POST'])
def preprocess_data():
    try:
        # Extract data from request
        data = request.get_json()
        X = np.array(data['X'])

        # Simple preprocessing: Remove NaNs and normalize the data
        X_cleaned = X[~np.isnan(X)]
        X_normalized = (X_cleaned - X_cleaned.mean()) / X_cleaned.std()

        # Prepare the response
        response = {
            'X_cleaned': X_cleaned.tolist(),
            'X_normalized': X_normalized.tolist()
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
