from sklearn.tree import DecisionTreeClassifier

# Encode time values
_TIME_ENCODING = {
    "lunch": 0,
    "dinner": 1,
    "closing": 2
}

def _encode_time(time_str: str) -> int:
    return _TIME_ENCODING.get(time_str.lower(), -1)

def predict_surplus(quantity: int, time_str: str) -> str:
    X = [
        [3, 0], [2, 0], [4, 1],
        [6, 2], [5, 2], [8, 2], [7, 2]
    ]
    y = ["No", "No", "No", "Yes", "Yes", "Yes", "Yes"]

    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    input_time = _encode_time(time_str)
    if input_time == -1:
        return "Invalid time input."

    prediction = clf.predict([[quantity, input_time]])[0]

    return "Surplus Likely – Trigger Alert" if prediction == "Yes" else "Few servings – No action needed"
