from surplus_predictor import predict_surplus

# Sample inputs
quantity = 6
time = "closing"

# Call the predictor function
result = predict_surplus(quantity, time)

print(f"Surplus predicted for quantity {quantity} at {time}: {result}")
