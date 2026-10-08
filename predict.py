import joblib
import pandas as pd

MODEL_PATH = "learning_style_model.joblib"

model = joblib.load(MODEL_PATH)


def predict_learning_style(student_data: dict):
    """Predict the learning-style class from a dictionary of input features."""
    X = pd.DataFrame([student_data])
    prediction = model.predict(X)[0]
    result = {"prediction": prediction}

    if hasattr(model.named_steps["model"], "predict_proba"):
        probabilities = model.predict_proba(X)[0]
        classes = model.named_steps["model"].classes_
        result["probabilities"] = {
            str(c): float(p) for c, p in zip(classes, probabilities)
        }
    return result
