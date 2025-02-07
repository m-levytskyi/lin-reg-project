from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Linear Regression Service Running"

@app.route('/linreg', methods=['POST'])
def linear_regression():
    try:
        # Extract data from request
        data = request.get_json()
        X = np.array(data['X']).reshape(-1, 1)  # Independent variable (reshape for sklearn)
        y = np.array(data['y'])                 # Dependent variable

        # Perform linear regression
        model = LinearRegression()
        model.fit(X, y)

        # Prepare the response
        response = {
            'coefficient': model.coef_.tolist(),
            'intercept': model.intercept_,
            'score': model.score(X, y)
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
