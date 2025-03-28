import streamlit as st
import pandas as pd
import numpy as np
import pickle

@st.cache_resource
def load_future_model():
    with open("future_salary_rf_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_future_model()

def app():

    st.header("Zukunftsprognose Gehaltsentwicklung")
    st.info("Prognose der Gehaltsentwicklung unter steigendem KI-Einsatz, differenziert nach Regionen.")

    # Auswahl der Parameter
    job_titles = ["Data Scientist", "Data Engineer", "Data Analyst", "Machine Learning Engineer", "Analyst Consultant"]
    selected_job = st.selectbox("Jobtitel", job_titles)

    experience = st.slider("Berufserfahrung (in Jahren)", 0, 55, 5)
    region = st.selectbox("Region", ["Amerika", "Europa", "Asien"])
    future_year = st.slider("Prognosejahr", 2025, 2035, 2025)

    ki_increase = st.slider("Erwartete Steigerung des KI-Einsatzes (%)", 0, 200, 50)
    # Beispiel: Basis-KI-Faktor 1, gesteigert um den prozentualen Anstieg
    ki_factor = 1 * (1 + ki_increase / 100)

    # Für die restlichen Skill-Spalten setzen wir beispielhaft 0 (oder mittlere Werte)
    default_skills = {col: 0 for col in [
        "Scikit_Learn", "AWS", "Docker", "Google_Analytics", "apache_airflow",
        "azure", "big_data", "data_pipelines", "deep_learning", "etl",
        "gcp", "hadoop", "java", "kpi", "kafka", "kubernetes", "machine_learning",
        "pandas", "power_bi", "pytorch", "python", "r", "sql", "snowflake",
        "spark", "tableau", "tensorflow"
    ]}

    # Zusammensetzen des Input-Dictionarys
    input_dict = {
        "Job_Title": [selected_job],
        "Experience_years": [experience],
        "Region_Group": [region],
        "Year": [future_year],
        "KI_Factor": [ki_factor]
    }
    input_dict.update(default_skills)

    input_data = pd.DataFrame(input_dict)

    # Vorhersage berechnen
    raw_prediction = model.predict(input_data)[0]

    # Setze Extrapolationsgrenzen: z.B. zwischen 50.000 und 999.999
    predicted_salary = np.clip(raw_prediction, 50000, 999999)

    st.markdown("### Prognostiziertes Gehalt")
    st.success(f"Das erwartete Gehalt im Jahr {future_year} beträgt: {predicted_salary:,.2f}")
