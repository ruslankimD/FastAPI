import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score
import kagglehub
import os

# Download latest version
path = kagglehub.dataset_download("iammustafatz/diabetes-prediction-dataset")
os.listdir(path)

# Load dataset
data = pd.read_csv(path + '/diabetes_prediction_dataset.csv')

# Define Features and Target
X = data.drop(columns=["diabetes"])  # "diabetes" is the target column
y = data["diabetes"]

# Identify categorical & numerical columns
categorical_features = ["gender", "smoking_history"]
numerical_features = ["age", "hypertension", "heart_disease", "bmi", "HbA1c_level", "blood_glucose_level"]

# Preprocessing Pipeline
preprocess = ColumnTransformer([
    ("num", StandardScaler(), numerical_features),  # Standardize numerical data
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)  # Encode categorical data
])

# Define Model Pipeline
pipeline_forest_best = Pipeline([
    ('preprocess', preprocess),
    ('classifier', RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, random_state=42))
])

# Split data into train & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
pipeline_forest_best.fit(X_train, y_train)

# Evaluate the model
y_pred = pipeline_forest_best.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# Save the trained model
joblib.dump(pipeline_forest_best, "diabetes_model.pkl")
print("Model saved as 'diabetes_model.pkl'")