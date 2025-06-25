from surplus_predictor import predict_surplus
from firebase_log import log_prediction

if __name__ == "__main__":
    quantity = 6
    time = "closing"
    
    result = predict_surplus(quantity, time)
    print(f"Prediction: {result}")
    
    log_prediction(quantity, time, result)
