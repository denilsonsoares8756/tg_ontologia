from fastapi import FastAPI
from app.services.pipeline import run_pipeline

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/predict")
def predict(data: dict):
    result = run_pipeline(data)
    return result