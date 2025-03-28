import streamlit as st
import pandas as pd
import pickle

def app():
    st.header("Gehaltstool")
    st.info("Hier können mittels der Parameter individuelle Gehaltsvorhersagen getroffen werden.")

    # Caching: CSV-Daten nur einmal laden
    @st.cache_data
    def load_data():
        return pd.read_csv("/Users/lucasfranke/DSI Weiterbildung/Projekt/SML_Visual/Tableau2.csv")
    df = load_data()

    # Caching: Modell nur einmal laden
    @st.cache_resource
    def load_model():
        with open("model.pkl", "rb") as f:
            return pickle.load(f)
    model = load_model()

    # Streamlit Widgets
    job_titles = [
        "Data Scientist",
        "Data Engineer",
        "Data Analyst",
        "Machine Learning Engineer",
        "Analyst Consultant"
    ]
    selected_job = st.selectbox("Wählen Sie den Jobtitel", job_titles)

    # Die im Dropdown angezeigten Skills (Benutzerfreundliche Namen)
    skill_options = [
        "Python", "R", "SQL", "Machine Learning", "Deep Learning",
        "Docker", "AWS", "Spark", "Tableau", "scikit-learn", "pandas"
    ]
    selected_skills = st.multiselect("Wählen Sie Ihre Skills", skill_options)

    experience = st.slider("Berufserfahrung (in Jahren)", 0, 55, 0)

    # Extrahiere Regionen aus der Location-Spalte der CSV
    regions = df["Location"].apply(lambda x: x.split(',')[-1].strip()).unique()
    region = st.selectbox("Region/Land", regions)

    # Definiere die Skill-Spalten, wie sie auch im Trainingsmodell verwendet wurden
    skill_columns = [
        "Scikit_Learn", "AWS", "Docker", "Google_Analytics", "apache_airflow",
        "azure", "big_data", "data_pipelines", "deep_learning", "etl",
        "gcp", "hadoop", "java", "kpi", "kafka", "kubernetes", "machine_learning",
        "pandas", "power_bi", "pytorch", "python", "r", "sql", "snowflake",
        "spark", "tableau", "tensorflow"
    ]
    
    # Mapping von im Dropdown verwendeten Skill-Namen zu den tatsächlichen Spaltennamen
    mapping = {
        "Python": "python",
        "R": "r",
        "SQL": "sql",
        "Machine Learning": "machine_learning",
        "Deep Learning": "deep_learning",
        "Docker": "Docker",
        "AWS": "AWS",
        "Spark": "spark",
        "Tableau": "tableau",
        "scikit-learn": "Scikit_Learn",
        "pandas": "pandas"
    }
    
    # Erstelle ein Dictionary für die Skill-Features, sodass alle Skill-Spalten belegt sind
    skill_features = {}
    for col in skill_columns:
        # Suche, ob es einen Mapping-Eintrag gibt, der zu dieser Spalte passt
        found = False
        for user_skill, mapped_col in mapping.items():
            if mapped_col == col:
                # Setze 1, falls der Skill ausgewählt wurde, sonst 0
                skill_features[col] = 1 if user_skill in selected_skills else 0
                found = True
                break
        if not found:
            # Für alle Skills, die nicht im Mapping enthalten sind, wird der Wert standardmäßig 0 gesetzt.
            skill_features[col] = 0

    # Zusammensetzen des Input-DataFrames
    input_dict = {
        "Job_Title": [selected_job],
        "Experience_years": [experience],
        "Region": [region]
    }
    # Füge alle Skill-Spalten hinzu
    input_dict.update(skill_features)
    
    input_data = pd.DataFrame(input_dict)

    # Vorhersage berechnen
    predicted_salary = model.predict(input_data)[0]

    st.markdown("### Vorhergesagtes Gehalt")
    st.success(f"Das erwartete Gehalt beträgt: {predicted_salary:,.2f}")

