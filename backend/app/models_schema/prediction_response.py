# ---- Goals for this file
# ✅ A structured success response after a prediction is made.
# ⚠️ (Optional) error response models for advanced error handling later.
# 📦 Package them in a separate file, just like the input schema.

from pydantic import BaseModel
from typing import Optional, List
from app.models_schema.housing_features import HousingFeatures


class ModelInfo(BaseModel):
    version: Optional[str] = None
    training_mse: Optional[float] = None


class PredictionResponse(BaseModel):
    predicted_median_house_value: float
    input_parameters: HousingFeatures
    model_info: Optional[ModelInfo] = None


class ErrorDetail(BaseModel):
    loc: Optional[List[str]] = None
    msg: str
    type: Optional[str] = None

class HTTPErrorResponse(BaseModel):
    detail: str | List[ErrorDetail]
