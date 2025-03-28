import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# CSV laden und Spaltennamen bereinigen
df = pd.read_csv("C:/Users/izadi/OneDrive/Documents/hossein/DSI_Weiterbildung/AbschlussProjekt/Tableau2.csv")
df.columns = df.columns.str.strip()

# Regionsextraktion: Länder in Regionen einteilen
def assign_region(location):
    country = location.split(',')[-1].strip().lower()
    if any(x in country for x in ["usa", "canada", "mexico", "brazil"]):
        return "Amerika"
    elif any(x in country for x in ["germany", "france", "uk", "italy", "spain", "sweden", "netherlands"]):
        return "Europa"
    elif any(x in country for x in ["india", "china", "japan", "south korea", "singapore"]):
        return "Asien"
    else:
        return "Other"

df["Region_Group"] = df["Location"].apply(assign_region)

# Extrahiere Jahr aus dem "Created"-Feld
df["Created"] = pd.to_datetime(df["Created"], errors="coerce")
df["Year"] = df["Created"].dt.year

# Berechne einen KI-Faktor aus relevanten KI-Skill-Spalten (zum Beispiel machine_learning und deep_learning)
ki_skills = ["machine_learning", "deep_learning"]
df["KI_Factor"] = df[ki_skills].sum(axis=1)

# Definiere die Features und das Ziel
skill_columns = [
    "Scikit_Learn", "AWS", "Docker", "Google_Analytics", "apache_airflow",
    "azure", "big_data", "data_pipelines", "deep_learning", "etl",
    "gcp", "hadoop", "java", "kpi", "kafka", "kubernetes", "machine_learning",
    "pandas", "power_bi", "pytorch", "python", "r", "sql", "snowflake",
    "spark", "tableau", "tensorflow"
]
features = ["Job_Title", "Experience_years", "Region_Group", "Year", "KI_Factor"] + skill_columns
target = "Avg_Salary"

# Entferne Zeilen mit fehlenden Zielwerten oder Jahreswerten
df = df.dropna(subset=[target, "Year"])

# Aufteilen in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Preprocessing: One-Hot-Encoding für kategoriale Variablen Job_Title und Region_Group
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Job_Title", "Region_Group"])
    ],
    remainder="passthrough"
)

# Erstelle eine Pipeline mit Preprocessing und RandomForestRegressor
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Trainiere das Modell
pipeline.fit(X_train, y_train)

# Speichere das Modell
with open("future_salary_rf_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("RandomForest-Modell erfolgreich trainiert und gespeichert.")
