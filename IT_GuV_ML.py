import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# CSV laden und Spaltennamen bereinigen
df = pd.read_csv("C:/Users/izadi/OneDrive/Documents/hossein/DSI_Weiterbildung/AbschlussProjekt/Tableau2.csv")
df.columns = df.columns.str.strip()  # Entfernt führende/nachfolgende Leerzeichen

# Überprüfe die vorhandenen Spaltennamen (optional)
print("Verfügbare Spalten:", df.columns.tolist())

# Feature Engineering: Extraktion der Region aus der Location-Spalte
def extract_region(location):
    parts = location.split(',')
    return parts[-1].strip() if len(parts) > 1 else "Unknown"

df["Region"] = df["Location"].apply(extract_region)

# Definiere die Spalten, die bereits die Skills repräsentieren
skill_columns = [
    "Scikit_Learn", "AWS", "Docker", "Google_Analytics", "apache_airflow",
    "azure", "big_data", "data_pipelines", "deep_learning", "etl",
    "gcp", "hadoop", "java", "kpi", "kafka", "kubernetes", "machine_learning",
    "pandas", "power_bi", "pytorch", "python", "r", "sql", "snowflake",
    "spark", "tableau", "tensorflow"
]

# Auswahl der Features: Jobtitel, Berufserfahrung, alle Skill-Spalten und Region
features = ["Job_Title", "Experience_years"] + skill_columns + ["Region"]
target = "Avg_Salary"

# Entferne Zeilen mit fehlenden Zielwerten
df = df.dropna(subset=[target])

# Aufteilen in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Preprocessing: One-Hot-Encoding für die kategorialen Variablen Job_Title und Region
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["Job_Title", "Region"])
    ],
    remainder="passthrough"  # Die numerischen Features (Experience_years und Skill-Spalten) bleiben unverändert
)

# Pipeline mit Vorverarbeitung und linearer Regression
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Trainiere das Modell
pipeline.fit(X_train, y_train)

# Speichere das trainierte Modell in einer Datei (z.B. model.pkl)
with open("model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("Modell erfolgreich trainiert und gespeichert.")
