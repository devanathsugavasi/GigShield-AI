# GigShield FastAPI entry point
from fastapi import FastAPI

app = FastAPI(
    title="GigShield API",
    description="AI-Powered Parametric Income Protection for Q-Commerce Delivery Partners",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}
