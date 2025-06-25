import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Load secret from Codex environment variable
key_data = json.loads(os.environ['FIREBASE_KEY_JSON'])
cred = credentials.Certificate(key_data)
firebase_admin.initialize_app(cred)
db = firestore.client()

def log_prediction(quantity, time, prediction):
    doc = {
        "quantity": quantity,
        "time": time,
        "prediction": prediction,
        "timestamp": datetime.utcnow()
    }
    db.collection("predictions").add(doc)
    print("✅ Logged to Firebase:", doc)
