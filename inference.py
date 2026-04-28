
import os
import json
import numpy as np
import joblib
import tensorflow as tf

def model_fn(model_dir):
    """Load model and scaler from the model directory."""
    model = tf.keras.models.load_model(os.path.join(model_dir, 'diabetes_model.keras'))
    scaler = joblib.load(os.path.join(model_dir, 'scaler.pkl'))
    return model, scaler

def input_fn(request_body, request_content_type):
    """Parse incoming request data."""
    if request_content_type == 'application/json':
        data = json.loads(request_body)
        return np.array(data['instances'])
    raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model_and_scaler):
    """Scale input and run prediction."""
    model, scaler = model_and_scaler
    scaled = scaler.transform(input_data)
    predictions = model.predict(scaled)
    return predictions

def output_fn(predictions, response_content_type):
    """Format the prediction output."""
    results = []
    for prob in predictions:
        result = {
            "probability": float(prob[0]),
            "prediction": "Diabetic" if prob[0] > 0.5 else "Not Diabetic",
            "confidence": f"{max(prob[0], 1-prob[0])*100:.1f}%"
        }
        results.append(result)
    return json.dumps(results)
