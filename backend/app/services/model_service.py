# ---- Goal for this file
# Build a service (model_service.py) that:

# Receives validated input (HousingFeatures)
# Converts it to a format your .pkl model expects
# Calls .predict() on the model
# Returns the prediction in a structured PredictionResponse

import pandas as pd
from app.models_schema.housing_features import HousingFeatures

from app.models_schema.prediction_response import PredictionResponse, ModelInfo

def predict(model, features: HousingFeatures) -> PredictionResponse:
    input_data = pd.DataFrame([features.dict()])

    # Drop 'ocean_proximity' since the model wasn't trained on it
    if "ocean_proximity" in input_data.columns:
        input_data.drop("ocean_proximity", axis=1, inplace=True)

    print("[DEBUG] Model prediction input:")
    print(input_data)

    try:
        predicted_value = model.predict(input_data)[0]
    except Exception as e:
        print("[ERROR] Model prediction failed:", e)
        raise e

    response = PredictionResponse(
        predicted_median_house_value=float(predicted_value),
        input_parameters=features,
        model_info=ModelInfo(version="1.0.0", training_mse=4500.75)
    )

    return response
