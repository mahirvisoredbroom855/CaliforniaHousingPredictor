# ------- Goal for this file 
# Specifies all the features needed by your trained model (like longitude, latitude, etc.)
# Enforces type validation and sensible defaults
# Uses examples and constraints (like ge=0) to ensure clean data
# Validates categorical fields like ocean_proximity using an Enum

from pydantic import BaseModel, Field
from enum import Enum



class OceanProximityEnum(str, Enum):
    near_bay = "NEAR BAY"
    less_than_1h_ocean = "<1H OCEAN"
    inland = "INLAND"
    near_ocean = "NEAR OCEAN"
    island = "ISLAND"

class HousingFeatures(BaseModel): 
    longitude: float = Field(..., example=-122.23)
    latitude: float = Field(..., example=37.88)
    housing_median_age: float = Field(..., example=41.0, ge=0)
    total_rooms: float = Field(..., example=880.0, ge=0)
    total_bedrooms: float = Field(..., example=129.0, ge=0)
    population: float = Field(..., example=322.0, ge=0)
    households: float = Field(..., example=126.0, ge=0)
    median_income: float = Field(..., example=8.3252, ge=0)
    ocean_proximity: OceanProximityEnum = Field(..., example=OceanProximityEnum.near_bay)





