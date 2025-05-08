# ----- Core Goals For This File
# Initialize the FastAPI app
# Set up CORS so the React frontend can communicate with the backend
# Include the router for the prediction API
# Load your ML model once at startup using FastAPI lifespan (recommended)

import os
import joblib
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.predict_router import router as predict_router


# Define app lifespan: executes before/after app starts
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        model_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../ml_model/my_california_housing_model.pkl")
        )
        app.state.model = joblib.load(model_path)
        print(f"[INFO] Model loaded successfully from: {model_path}")
    except Exception as e:
        app.state.model = None
        print(f"[ERROR] Failed to load model: {e}")
    
    yield  # App is running
    print("[INFO] Shutting down app...")  # Optional: cleanup code here


# Initialize FastAPI app with lifespan handler
app = FastAPI(
    title="California Housing Price Predictor API",
    version="1.0.0",
    description="An API to predict median house value in California districts",
    lifespan=lifespan
)


# --- CORS SETUP ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8080"
    # Add production frontend domain here later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- ROUTERS ---
app.include_router(predict_router, prefix="/api/v1")
