from flask import Flask, jsonify, request
from joblib import load

model = load('knn_model.joblib')
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_data = [data['feature1'], data['feature2'], ...]  # Replace with your own feature names
    prediction = model.predict([input_data])[0]
    response = {'prediction': prediction}
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run()
