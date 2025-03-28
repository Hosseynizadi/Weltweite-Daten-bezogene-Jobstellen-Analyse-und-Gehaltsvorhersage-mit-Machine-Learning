import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pycountry

import ast  # Für die Verarbeitung der Skills-Liste

def app():

    st.header("Interaktives Dashboard zur Datenanalyse")
    st.info("Über die Dropdowns können die Parameter für eine Visualisierung ausgewählt werden.")

    # Daten laden
    @st.cache_data
    def load_data():
        df = pd.read_csv("Tableau2.csv")
        # Skills-String zu Liste konvertieren
        df['Skills'] = df['Skills'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
        return df

    df = load_data()

    # Sidebar für Filter
    job_bezeichnung = st.selectbox(
        "Wählen Sie eine Job-Bezeichnung:",
        options=df['Job_Title'].unique()
    )

    visualisierung = st.selectbox(
        "Wählen Sie eine Visualisierung:",
        options=[
            "Gehaltsverteilung nach Job",
            "Gehaltsverteilung nach Skills",
            "Gehaltsverteilung nach Ländern",
            "Verhältnis von Erfahrung zu Jobs"
        ]
    )

    st.write(f"Sie haben die Visualisierung **{visualisierung}** und die Job-Bezeichnung **{job_bezeichnung}** ausgewählt.")

    # Daten filtern
    filtered_df = df[df['Job_Title'] == job_bezeichnung]

    # Visualisierungen
    if visualisierung == "Gehaltsverteilung nach Job":
        plt.figure(figsize=(10, 6))
        sns.histplot(filtered_df['Avg_Salary'], bins=20, kde=True)
        plt.title(f"Gehaltsverteilung für {job_bezeichnung}")
        plt.xlabel("Durchschnittsgehalt")
        plt.ylabel("Anzahl")
        st.pyplot(plt)

    elif visualisierung == "Gehaltsverteilung nach Skills":
        # Skills explodieren und aggregieren
        skills_df = filtered_df.explode('Skills')
        skills_avg = skills_df.groupby('Skills')['Avg_Salary'].mean().sort_values(ascending=False)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x=skills_avg.values, y=skills_avg.index, palette="viridis")
        plt.title(f"Durchschnittsgehalt nach Skills für {job_bezeichnung}")
        plt.xlabel("Durchschnittsgehalt")
        st.pyplot(plt)

    elif visualisierung == "Gehaltsverteilung nach Ländern":
        # Extrahiere Länder aus der Location-Spalte
        filtered_df['Country'] = filtered_df['Location'].apply(lambda x: x.split(",")[-1].strip())
        
        # Konvertiere Länder zu ISO-Codes
        def get_iso_code(country_name):
            try:
                return pycountry.countries.search_fuzzy(country_name)[0].alpha_3
            except:
                return None
        
        filtered_df['Country_ISO'] = filtered_df['Country'].apply(get_iso_code)
        country_avg = filtered_df.groupby('Country_ISO')['Avg_Salary'].mean().reset_index()
        
        # Erstelle Choropleth-Karte
        fig = px.choropleth(
            country_avg,
            locations="Country_ISO",
            color="Avg_Salary",
            hover_name="Country_ISO",
            color_continuous_scale="Viridis",
            title=f"Durchschnittsgehalt für {job_bezeichnung} nach Ländern"
    )
        st.plotly_chart(fig)
    
        # Zeige Warnung, wenn Länder nicht erkannt wurden
        if filtered_df['Country_ISO'].isnull().any():
            st.warning("Einige Länder konnten nicht in ISO-Codes konvertiert werden.")

    elif visualisierung == "Verhältnis von Erfahrung zu Jobs":
        plt.figure(figsize=(10, 6))
        sns.regplot(
            data=filtered_df,
            x='Experience_years',
            y='Avg_Salary',
            scatter_kws={'alpha':0.5},
            line_kws={'color':'red'}
        )
        plt.title(f"Zusammenhang zwischen Erfahrung und Gehalt für {job_bezeichnung}")
        plt.xlabel("Berufserfahrung (Jahre)")
        plt.ylabel("Durchschnittsgehalt")
        st.pyplot(plt)