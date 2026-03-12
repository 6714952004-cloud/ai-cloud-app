from fastapi import FastAPI
from ai.model import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Server Running"}

@app.get("/ai")
def ai(text: str):
    result = predict(text)
    return {"response": result}