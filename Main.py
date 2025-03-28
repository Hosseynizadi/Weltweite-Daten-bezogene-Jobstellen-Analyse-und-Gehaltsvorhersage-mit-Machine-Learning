# Importiere notwendige Bibliotheken und Module
import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importiere die Seiten/Module für die App
# Wichtig: Die Python-Skripte müssen im gleichen Verzeichnis sein wie diese Datei!
import main_page
import fazit_page
import visual_page
import prediction_page
import salaray_analysis_page

# Definiere die Seiten der App, die verschiedene Aspekte von Streamlit vorstellen
pages = {
    "1. Projektvorstellung": main_page,
    "2. Visualisierung": visual_page,
    "3. Gehaltstool": salaray_analysis_page,
    "4. Predictions": prediction_page,
    "5. Fazit & Ausblick": fazit_page
}

# Erstelle eine Seitenleiste für die Navigation im Projekt
st.sidebar.title("Navigation")
select = st.sidebar.radio("Gehe zu:", list(pages.keys()))

# Starte die ausgewählte Seite
pages[select].app()

