from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
import pandas as pd
import logging
from FastAPI.request import DiabetesRequest
import os

# FastAPI initialization
app = FastAPI()

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Loading the model
try:
    model_path = os.path.join(os.path.dirname(__file__), 'diabetes_model.pkl')
    model = joblib.load(model_path)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Model loading error: {e}")
    raise RuntimeError("Model loading error")


# Root endpoint
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is running! Use /docs to test."}


# Endpoint of prediction
@app.post("/predict")
def predict(request: DiabetesRequest):
    try:
        # Convert to DataFrame
        input_data = pd.DataFrame([request.model_dump()])

        prediction = model.predict(input_data)[0]

        return {"prediction": int(prediction)}

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=400, detail=str(e))