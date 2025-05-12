from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS

logging.basicConfig(level=logging.DEBUG)

# Load trained model and vectorizer
try:
    model = joblib.load("model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    logging.info("Model and vectorizer loaded successfully.")
except Exception as e:
    logging.error(f"Error loading model or vectorizer: {e}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        user_input = data["message"]  # Match key from JS
        logging.debug(f"Received input: {user_input}")

        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        logging.debug(f"Prediction: {prediction}")

        return jsonify({"reply": prediction})
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": "An error occurred during prediction."}), 500

if __name__ == "__main__":
    app.run(debug=True)
