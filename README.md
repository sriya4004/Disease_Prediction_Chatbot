🩺 Disease Prediction Chatbot
A simple web-based chatbot that predicts diseases based on user symptoms using a Naive Bayes machine learning model.

📁 Project Structure
bash
Copy
Edit
Disease-Predictor-Chatbot/
│
├── app.py                # Flask backend
├── train_model.py        # Script to train and save the ML model
├── model.pkl             # Trained ML model (generated)
├── vectorizer.pkl        # Trained vectorizer (generated)
│
├── index.html            # Frontend UI
├── script.js             # Frontend JS logic
├── style.css             # Frontend styling
│
└── README.md             # Project documentation
🚀 Features
Predict diseases from text-based symptom input

Voice input support (via Web Speech API)

Simple ML model using sklearn

Web interface using HTML, CSS, and JS

Flask backend with CORS enabled

🔧 Requirements
Python 3.x

pip

Install Python dependencies:
bash
Copy
Edit
pip install flask flask-cors scikit-learn joblib
🧠 Step 1: Train the Model
bash
Copy
Edit
python train_model.py
This script trains a MultinomialNB classifier using a small dataset of symptoms and diseases. It saves:

model.pkl (trained model)

vectorizer.pkl (text vectorizer)

🔌 Step 2: Start the Flask Backend
bash
Copy
Edit
python app.py
This starts the backend server on:

cpp
Copy
Edit
http://127.0.0.1:5000/
🌐 Step 3: Serve the Frontend
Do NOT open index.html directly.

Instead, open a second terminal and run:

bash
Copy
Edit
python -m http.server 8000
Then go to:

bash
Copy
Edit
http://localhost:8000/index.html
This loads your chatbot page properly and allows fetch requests to work.

💬 Example Inputs
Input Symptoms	Predicted Disease
fever rash swollen glands	measles
dizziness blurred vision headache	hypertension
stomach pain diarrhea vomiting	food poisoning

🛠 Troubleshooting
❌ Failed to fetch
Cause: Opening index.html directly as a file (e.g., file:///...)

Fix: Always use http://localhost:8000/index.html

❌ CORS or blocked fetch
Make sure Flask server has:

python
Copy
Edit
from flask_cors import CORS
CORS(app)
🏁 Optional: One-Click Startup Script
You can create a .bat file to start both the Flask server and the frontend server.

Let me know if you'd like this added!
![image](https://github.com/user-attachments/assets/0c7408fc-4117-45ae-81e5-a0ec1639c8f8)


👩‍💻 Made By
Sriya Pandey
Computer Science Engineer, Chandigarh University
