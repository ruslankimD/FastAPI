from pydantic import BaseModel, Field

class DiabetesRequest(BaseModel):
   #Each field is a parameter that calculates the input data.
    gender: str = Field(..., pattern="^(Male|Female)$", description="Gender: Male or Female")
    age: float = Field(..., gt=0, description="Age in years")
    hypertension: int = Field(..., ge=0, le=1, description="0 - No, 1 - Yes")
    heart_disease: int = Field(..., ge=0, le=1, description="0 - No, 1 - Yes")
    smoking_history: str = Field(..., description="Smoking history: never, former, current, etc.")
    bmi: float = Field(..., gt=0, description="Body Mass Index")
    HbA1c_level: float = Field(..., description="HbA1c level")
    blood_glucose_level: int = Field(..., gt=0, description="Blood glucose level")

    def to_features(self):
        return [
            self.gender,
            self.age,
            self.hypertension,
            self.heart_disease,
            self.smoking_history,
            self.bmi,
            self.HbA1c_level,
            self.blood_glucose_level,
        ]