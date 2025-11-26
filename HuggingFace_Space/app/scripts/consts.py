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
    "age",
    "alcohol_consumption_per_week",
    "bmi",
    "cholesterol_total",
    "diabetes_risk_score",
    "diastolic_bp",
    "glucose_fasting",
    "glucose_postprandial",
    "hba1c",
    "hdl_cholesterol",
    "heart_rate",
    "insulin_level",
    "ldl_cholesterol",
    "physical_activity_minutes_per_week",
    "screen_time_hours_per_day",
    "sleep_hours_per_day",
    "systolic_bp",
    "triglycerides",
    "waist_to_hip_ratio",
]

# Mappings

TRUTH_MAPPING = {"False": 0.0, "True,": 1.0}

ACTIVITY_LEVEL_MAPPING = {"High": 0.0, "Low": 1.0, "Moderate": 2.0}

ALCOHOL_GROUP_MAPPING = {"Heavy": 0.0, "Light": 1.0, "Moderate": 2.0}

BMI_GROUP_MAPPING = {"Normal": 0.0, "Obese": 1.0, "Overweight": 2.0, "Underweight": 3.0}

DIABETES_STAGE_MAPPING = {
    "Gestational": 0.0,
    "No Diabetes": 1.0,
    "Pre-Diabetes": 2.0,
    "Type 1": 3.0,
    "Type 2": 4.0,
}

EDUCATION_LEVEL_MAPPING = {
    "Graduate": 0.0,
    "Highschool": 1.0,
    "No formal": 2.0,
    "Postgraduate": 3.0,
}

EMPLOYMENT_STATUS_MAPPING = {"Employed": 0.0, "Retired": 1.0, "Student": 2.0, "Unemployed": 3.0}

ETHNICITY_MAPPING = {"Asian": 0.0, "Black": 1.0, "Hispanic": 2.0, "Other": 3.0, "White": 4.0}

GENDER_MAPPING = {"Female": 0.0, "Male": 1.0, "Other": 2.0}

INCOME_LEVEL_MAPPING = {
    "High": 0.0,
    "Low": 1.0,
    "Lower-Middle": 2.0,
    "Middle": 3.0,
    "Upper-Middle": 4.0,
}

SMOKING_STATUS_MAPPING = {"Current": 0.0, "Former": 1.0, "Never": 2.0}


# Information for streamlit user input section; keys must match with FEATURE_NAMES list content
INPUT_METADATA = {
    "abdominal_obesity": {
        "title": "Are you Abdominaly Obese?",
        "widget_type": "radio",
        "options": TRUTH_MAPPING.keys(),
        "horizontal": True,
    },
    "activity_level": {
        "title": "How active are you?",
        "widget_type": "radio",
        "options": ["Low", "Moderate", "High"],
        "horizontal": True,
    },
    "age": {
        "title": "How old are you?",
        "widget_type": "slider",
        "min_value": 18.0,
        "max_value": 90.0,
        "value": 50.0,
        "step": 1.0,
    },
    "alcohol_consumption_per_week": {
        "title": "How many alcoholic beverages do you consume per week?  \n*Beer: 12 oz (5% ABV)*  \n*Wine: 5 oz (12% ABV)*  \n*Liquor: 1.5 oz (40% ABV)*",
        "widget_type": "slider",
        "min_value": 0.0,
        "max_value": 10.0,
        "value": 3.0,
        "step": 1.0,
    },
    "alcohol_group": {
        "title": "What category do you most fit into?  \n*Light (≤7 drinks/week - women, ≤14 - men)*,  \n*Medium (7 drinks/week - women, 14 - men)*  \n*Heavy (≥ 8 drinks/week - women, ≥ 15 drinks/week - men)*",
        "widget_type": "radio",
        "options": ["Light", "Moderate", "Heavy"],
        "horizontal": True,
    },
    "bmi": {
        "title": "What is your Body Mass Index?",
        "widget_type": "slider",
        "min_value": 15.0,
        "max_value": 39.20,
        "value": 25.0,
        "step": 0.1,
    },
    "bmi_group": {
        "title": "What is your BMI Category?  \n*<18.5 - Underweight*  \n*18.5 - 24.9 - Normal*  \n*25.0 - 29.9 - Overweight*  \n*≥ 30.0 Obese*",
        "widget_type": "radio",
        "options": ["Underweight", "Normal", "Overweight", "Obese"],
        "horizontal": True,
        "preselected_index": 2,
    },
    "cardiovascular_history": {
        "title": "Do your have previous cardiovascular issues?",
        "widget_type": "radio",
        "options": TRUTH_MAPPING.keys(),
        "horizontal": True,
    },
    "hdl_cholesterol": {
        "title": "What are your High-Density Lipoprotein Cholesterol levels?",
        "widget_type": "slider",
        "min_value": 20.0,
        "max_value": 98.20,
        "value": 54.0,
        "step": 1.0,
    },
    "ldl_cholesterol": {
        "title": "What are your Low-Density Lipoprotein Cholesterol levels?",
        "widget_type": "slider",
        "min_value": 50.0,
        "max_value": 263.0,
        "value": 103.0,
        "step": 1.0,
    },
    "triglycerides": {
        "title": "What are your Triglyceride levels?",
        "widget_type": "slider",
        "min_value": 30.0,
        "max_value": 344.0,
        "value": 121.0,
        "step": 1.0,
    },
    "cholesterol_total": {
        "title": "What are your Total Cholesterol levels?  \n*Calculated using > HDL+LDL+VLDL = HDL+LDL+(Triglycerides/5)*",
        "widget_type": "slider",
        "min_value": 100.0,
        "max_value": 318.0,
        "value": 185.0,
        "step": 1.0,
    },
    "diabetes_risk_score": {
        "title": "What is your diabetes risk score?",
        "widget_type": "slider",
        "min_value": 2.7,
        "max_value": 67.2,
        "value": 30.0,
        "step": 0.1,
    },
    "diabetes_stage": {
        "title": "What is your diabetes stage at?",
        "widget_type": "radio",
        "options": DIABETES_STAGE_MAPPING.keys(),
        "horizontal": True,
        "preselected_index": 1,
    },
    "systolic_bp": {
        "title": "What is your Systolic Blood Pressure (Pressure when your heart pumps blood)?",
        "widget_type": "slider",
        "min_value": 90.0,
        "max_value": 179.0,
        "value": 115.0,
        "step": 1.0,
    },
    "diastolic_bp": {
        "title": "What is your Diastolic Blood Pressure? (Pressure when the heart relaxes between beats.)",
        "widget_type": "slider",
        "min_value": 50.0,
        "max_value": 110.0,
        "value": 75.0,
        "step": 1.0,
    },
    "education_level": {
        "title": "What is your highest Education Level?",
        "widget_type": "radio",
        "options": ["No formal", "Highschool", "Graduate", "Postgraduate"],
        "horizontal": True,
        "preselected_index": 2,
    },
    "employment_status": {
        "title": "What is your current Employment Status?",
        "widget_type": "radio",
        "options": ["Student", "Employed", "Retired", "Unemployed"],
        "horizontal": True,
        "preselected_index": 1,
    },
    "ethnicity": {
        "title": "What is your Ethnicity?",
        "widget_type": "radio",
        "options": ETHNICITY_MAPPING.keys(),
        "horizontal": True,
        "preselected_index": 4,
    },
    "family_history_diabetes": {
        "title": "Does your family have History of Diabetes?",
        "widget_type": "radio",
        "options": TRUTH_MAPPING.keys(),
        "horizontal": True,
    },
    "gender": {
        "title": "What is your Gender?",
        "widget_type": "radio",
        "options": GENDER_MAPPING.keys(),
        "horizontal": True,
    },
    "glucose_fasting": {
        "title": "What is your Blood Glucose levels when fasting?",
        "widget_type": "slider",
        "min_value": 60.0,
        "max_value": 172.0,
        "value": 111.0,
        "step": 1.0,
    },
    "glucose_postprandial": {
        "title": "What is your Postprandial Glocose level (Blood glucose levels ~ 2 hours after a meal)?",
        "widget_type": "slider",
        "min_value": 60.0,
        "max_value": 287.0,
        "value": 160.0,
        "step": 1.0,
    },
    "hba1c": {
        "title": "What is your Hemoglobin A1c? (Percentage of Average Hemogloben, in your red blood cells, coated in glucose over 2-3 months.)",
        "widget_type": "slider",
        "min_value": 4.0,
        "max_value": 9.8,
        "value": 6.5,
        "step": 0.01,
    },
    "heart_rate": {
        "title": "What is your Latest Heart Rate (BPM)?",
        "widget_type": "slider",
        "min_value": 40.0,
        "max_value": 105.0,
        "value": 69.0,
        "step": 1.0,
    },
    "hypertension_history": {
        "title": "Do your have previous Hypertension issues?",
        "widget_type": "radio",
        "options": TRUTH_MAPPING.keys(),
        "horizontal": True,
    },
    "income_level": {
        "title": "What is your income level?  \n\
            *\$0 - \$30,000 = Low*  \n*\$30,001 - \$58,020 =\
            Lower-Middle*  \n*\$58,021 - \$94,000 = Middle*\
            \n*\$94,001 - \$153,000 = Upper-Middle*  \n\
            *>\$153,001 = High",
        "widget_type": "radio",
        "options": ["Low", "Lower-Middle", "Middle", "Upper-Middle", "High"],
        "horizontal": True,
        "preselected_index": 2,
    },
    "insulin_level": {
        "title": "What is your latest Insulin Level after fasting 8-12hrs?",
        "widget_type": "slider",
        "min_value": 2.0,
        "max_value": 32.2,
        "value": 9.0,
        "step": 0.01,
    },
    "physical_activity_minutes_per_week": {
        "title": "How many minutes do you spend performing a physical activity per week?",
        "widget_type": "slider",
        "min_value": 0.0,
        "max_value": 833.0,
        "value": 120.0,
        "step": 1.0,
    },
    "screen_time_hours_per_day": {
        "title": "How many hours do you spend watching a screen (Phone, Table, TV, etc.)?",
        "widget_type": "slider",
        "min_value": 0.5,
        "max_value": 16.7,
        "value": 6.0,
        "step": 0.1,
    },
    "sleep_hours_per_day": {
        "title": "How many hours of sleep do you normally get?",
        "widget_type": "slider",
        "min_value": 3.0,
        "max_value": 10.0,
        "value": 7.0,
        "step": 0.1,
    },
    "smoking_status": {
        "title": "What is your current Smoking Status?",
        "widget_type": "radio",
        "options": SMOKING_STATUS_MAPPING.keys(),
        "horizontal": True,
        "preselected_index": 2,
    },
    "waist_to_hip_ratio": {
        "title": "What is your Waist to Hip Ratio?",
        "widget_type": "slider",
        "min_value": 0.67,
        "max_value": 1.06,
        "value": 0.85,
        "step": 0.01,
    },
}
