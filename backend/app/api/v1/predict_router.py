from fastapi import APIRouter, HTTPException, Request
from app.models_schema.housing_features import HousingFeatures
from app.models_schema.prediction_response import PredictionResponse
from app.services.model_service import predict

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_route(features: HousingFeatures, request: Request):  # Add request param
    try:
        model = request.app.state.model  # Access model from app.state

        if model is None:
            raise HTTPException(status_code=503, detail="Model not loaded.")

        print(f"[DEBUG] Input: {features.dict()}")

        result = predict(model, features)
        print(f"[DEBUG] Prediction result: {result}")
        return result

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
