import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from cryptography.hazmat.primitives import serialization  # Needed for fixing PEM

# Load secret from Codex environment variable
key_data = json.loads(os.environ['FIREBASE_KEY_JSON'])
key_data["private_key"] = key_data["private_key"].replace("\\n", "\n")  # 🔥 Fix here

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
