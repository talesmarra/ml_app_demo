"""
Main module
"""
import json

from flask import Flask, request, jsonify
import tensorflow as tf
import tensorflow_text

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Sklearn Prediction Container</h1>"


@app.route("/predict", methods=['POST'])
def predict():
    inference_payload = request.json
    examples = tf.constant([inference_payload['text']])
    print(examples)
    reloaded_model = tf.saved_model.load('./model')
    score = tf.sigmoid(reloaded_model.signatures['serving_default'](examples)['classifier']).numpy()[0][0]
    if score > 0.5:
        prediction = 'good'
    else:
        prediction = 'bad'
    prediction += f' with score: {score}'
    return jsonify({'prediction': prediction})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
