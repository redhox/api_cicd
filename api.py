# Import des librairies uvicorn, pickle, FastAPI, File, UploadFile, BaseModel
from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np 
from pydantic import BaseModel
import pickle
import pandas as pd
import json
# import mlflow
import os
# import boto3

# Création des tags
tags = [
       {
              "name": "Hello",
              "description": "Hello World (c'est un hello world)",
       },
       {
              "name": "Predict",
              "description": "Prediction en cicd",
       },
]


# Création de l'application
app = FastAPI(
       title="API de prediction en cicd",
       description= "Predictions qui a pour but d'etre un test de production cicd",
       version= "1.0.0",
       openapi_tags= tags
)
with open("model_1.pkl", 'rb') as file:
    svm_1 = pickle.load(file)
with open("model_2.pkl", 'rb') as file:
    svm_2 = pickle.load(file)




# Création du modèle de données pour le modéle 1 ('Gender', 'Age', 'Physical Activity Level', 'Heart Rate', 'Daily Steps', 'BloodPressure_high', 'BloodPressure_low', 'Sleep Disorder'])
class Credit(BaseModel):
    Gender: int
    Age: int
    Physical_Activity_Level: int
    Heart_Rate: int
    Daily_Steps: int
    BloodPressure_high: float
    BloodPressure_low: float
    # Sleep_Disorder: bool

@app.post("/predict", tags=["Predict"])
def predict(credit: dict):
    try:
        with open("model_1.pkl", "rb") as file:
            model = pickle.load(file)
    except FileNotFoundError:
        return {"error": "Model file not found"}

    try:
        cred = Credit(**credit)
        data = pd.DataFrame([cred.model_dump()])
        rename_dict = {
            "Daily_Steps": "Daily Steps",
            "Heart_Rate": "Heart Rate",
            "Physical_Activity_Level": "Physical Activity Level",
        }
        data.rename(columns=rename_dict, inplace=True)
        prediction = model.predict(data)

        # Ensure prediction is a JSON serializable type
        if isinstance(prediction, np.ndarray):
            prediction = prediction.tolist()

        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}

class Credit2(BaseModel):
    Physical_Activity_Level: int
    Heart_Rate: int
    Daily_Steps: int

# Point de terminaison avec paramètre
@app.get("/hello", tags=["Hello"])
def hello(name: str='World'):
        return {"message": f"Hello {name}"}

@app.post("/predict2", tags=["Predict"])
def predict(credit2: dict):
    try:
        with open("model_2.pkl", "rb") as file:
            model2 = pickle.load(file)
    except FileNotFoundError:
        return {"error": "Model file not found"}

    try:
        cred = Credit2(**credit2)
        data = pd.DataFrame([cred.model_dump()])
        rename_dict = {
            "Daily_Steps": "Daily Steps",
            "Heart_Rate": "Heart Rate",
            "Physical_Activity_Level": "Physical Activity Level",
        }
        data.rename(columns=rename_dict, inplace=True)
        prediction = model2.predict(data)

        # Ensure prediction is a JSON serializable type
        if isinstance(prediction, np.ndarray):
            prediction = prediction.tolist()

        return {"prediction": prediction}
    except Exception as e:
        return {"error": str(e)}
# Démarage de l'application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)