"""
This module defines constants for file paths and feature names used in the application.
"""

from pathlib import Path

# Get the Grandparent's directory by taking the absolute path of consts.py and going up two levels.
BASE_DIR = Path(__file__).resolve().parents[1]

CONFIG_DIRECTORY = "./configs"
CONFIG_FILE_NAME = "config.json"
CONFIG_PATH = BASE_DIR / CONFIG_DIRECTORY / CONFIG_FILE_NAME

# Use if Needed
SCALER_DIRECTORY = "./scalers"

# Use if Needed
FEATURE_SCALER_FILE_NAME = "feature-scaler.joblib"
FEATURE_SCALER_PATH = BASE_DIR / SCALER_DIRECTORY / FEATURE_SCALER_FILE_NAME

# Use if Needed
LABEL_SCALER_FILE_NAME = "label-scaler.joblib"
LABEL_SCALER_PATH = BASE_DIR / SCALER_DIRECTORY / LABEL_SCALER_FILE_NAME

MODEL_DIRECTORY = "model_weights"
MODEL_WEIGHTS_FILE_NAME = "ENTER MODEL WEIGHTS FILE NAME HERE (ex. 'trained-model.pt')"
MODEL_WEIGHTS_FULL_PATH = BASE_DIR / MODEL_DIRECTORY / MODEL_WEIGHTS_FILE_NAME


# Same feature order names and order as during the model training data set
FEATURE_NAMES = [
    "ADD",
    "FEATURE",
    "NAMES",
    "HERE",
]

# Create list of features that will be only validated during the streamlit user input field
STREAMLIT_VALIDATED = [
    "ADD",
    "STREAMLIT",
    "VALIDATED",
    "NAMES",
    "HERE",
]

# Mappings
EXAMPLE_MAPPING = {
    "entertainment": 0.0,
    "food_dining": 1.0,
    "gas_transport": 2.0,
}

EXAMPLE_MAPPING_2 = {
    "M": 0.0,
    "F": 1.0,
}


# Information for streamlit user input section; keys must match with FEATURE_NAMES list content
INPUT_METADATA = {
    "ADD": {
        "title": "TITLE FOR USER INPUT FIELD",
        "widget_type": "selectbox",
        "options": EXAMPLE_MAPPING.keys(),
    },
    "FEATURE": {
        "title": "TITLE FOR USER INPUT FIELD",
        "widget_type": "number_input",
        "min_value": 1.0,
        "max_value": 30000.00,
        "value": 25.0,
    },
    "NAMES": {
        "title": "TITLE FOR USER INPUT FIELD",
        "widget_type": "radio",
        "options": EXAMPLE_MAPPING_2.keys(),
    },
    "HERE": {
        "title": "TITLE FOR USER INPUT FIELD",
        "widget_type": "slider",
        "min_value": -90.0,
        "max_value": 90.0,
        "value": 20.0,
        "step": 0.01,
    },
}
