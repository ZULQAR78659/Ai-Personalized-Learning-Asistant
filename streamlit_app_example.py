import streamlit as st
import json
import joblib
import pandas as pd

st.set_page_config(page_title="AI Learning Style Analyzer", page_icon="🎓")
st.title("AI Learning Style Analyzer")

model = joblib.load("learning_style_model.joblib")
with open("feature_columns.json", "r") as f:
    feature_columns = json.load(f)

st.write("Enter the student's information and questionnaire responses.")

# Replace these example widgets with your final Flutter/API inputs.
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=5, max_value=100, value=20)

st.info("For deployment, create one input widget for each questionnaire feature listed in feature_columns.json.")

st.write("Required feature order:")
st.code("\n".join(feature_columns))

st.warning("This example intentionally does not invent questionnaire wording. Use the exact questionnaire fields from your project dataset.")
