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
MODEL_WEIGHTS_FILE_NAME = "model-weights.pt"
MODEL_WEIGHTS_FULL_PATH = BASE_DIR / MODEL_DIRECTORY / MODEL_WEIGHTS_FILE_NAME


# Same feature order names and order as during the model training data set

# Step 1: Get names from csv file
# Step 2: Remove target column and extra ",'"
# Step 3: Use 'find and replace' to find "," with "Find in Selection mode" (https://www.bing.com/videos/riverview/relatedvideo?q=how+to+use+the+find+in+selection+feature+in+vscode&&view=riverview&mmscn=mtsc&mid=168E36685A91BA0776CB168E36685A91BA0776CB&&aps=29&FORM=VMSOVR)
# Step 4: Replace with:
# Line 1: ,
# Line 2: \t"
# Step 5: Click "Replace all"
# Step 6: Add beginning "
FEATURE_NAMES = [
    "abdominal_obesity",
    "activity_level",
    "age",
    "alcohol_consumption_per_week",
    "alcohol_group",
    "bmi",
    "bmi_group",
    "cardiovascular_history",
    "cholesterol_total",
    "diabetes_risk_score",
    "diabetes_stage",
    "diastolic_bp",
    "education_level",
    "employment_status",
    "ethnicity",
    "family_history_diabetes",
    "gender",
    "glucose_fasting",
    "glucose_postprandial",
    "hba1c",
    "hdl_cholesterol",
    "heart_rate",
    "hypertension_history",
    "income_level",
    "insulin_level",
    "ldl_cholesterol",
    "physical_activity_minutes_per_week",
    "screen_time_hours_per_day",
    "sleep_hours_per_day",
    "smoking_status",
    "systolic_bp",
    "triglycerides",
    "waist_to_hip_ratio",
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

GENDER_MAPPING = {"Female": "0.0", "Male": "1.0", "Other": "2.0"}

ETHNICITY_MAPPING = {"Asian": 0.0, "Black": 1.0, "Hispanic": 2.0, "Other": 3.0, "White": 4.0}

EDUCATION_LEVEL_MAPPING = {
    "Graduate": 0.0,
    "Highschool": 1.0,
    "No formal": 2.0,
    "Postgraduate": 3.0,
}

INCOME_LEVEL_MAPPING = {
    "High": 0.0,
    "Low": 1.0,
    "Lower-Middle": 2.0,
    "Middle": 3.0,
    "Upper-Middle": 4.0,
}

EMPLOYMENT_STATUS_MAPPING = {"Employed": 0.0, "Retired": 1.0, "Student": 2.0, "Unemployed": 3.0}

SMOKING_STATUS_MAPPING = {"Current": 0.0, "Former": 1.0, "Never": 2.0}

DIABETES_STAGE_MAPPING = {
    "Gestational": 0.0,
    "No Diabetes": 1.0,
    "Pre-Diabetes": 2.0,
    "Type 1": 3.0,
    "Type 2": 4.0,
}

BMI_GROUP_MAPPING = {"Normal": 0.0, "Obese": 1.0, "Overweight": 2.0, "Underweight": 3.0}

ACTIVITY_LEVEL_MAPPING = {"High": 0.0, "Low": 1.0, "Moderate": 2.0}

ALCOHOL_GROUP_MAPPING = {"Heavy": 0.0, "Light": 1.0, "Moderate": 2.0}


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
