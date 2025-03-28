import streamlit as st

# Konfiguration der Seite
st.set_page_config(
    page_title="Gehaltsvorhersage in Data Science",
    page_icon="💼",
    layout="wide"
)

# CSS-Styling im Kopf der App einbinden (wichtig: kommt VOR der Nutzung der Klassen!)
st.markdown("""
<style>
    .highlight-box {
        border-left: 4px solid #2ecc71;
        padding: 1rem;
        margin: 1rem 0;
        background: #f8f9fa;
        border-radius: 5px;
    }
    .target-group {
        font-size: 1.1em;
        color: #2c3e50;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)


def app():

    # --- Titel & Einführung ---
    st.title("🎯 Gehaltsvorhersage in datengetriebenen Berufen")
    st.markdown("""
    *Eine Machine-Learning-Plattform für transparente Gehaltsprognosen in Data Science, Engineering und Analytics*  
    """)

    st.divider()

    # --- Zielgruppe ---
    st.header("👥 Für wen ist diese Plattform?")
    st.markdown("""
    <div class="highlight-box">
        <div class="target-group">✅ <strong>Studierende</strong></div>
        <p>Planung von Karrierewegen & realistische Gehaltsbenchmarks</p>
        <div class="target-group">✅ <strong>Jobsuchende</strong></div>
        <p>Bewertung von Angeboten in Data Science, Engineering und Analytics</p>
        <div class="target-group">✅ <strong>DSI-Teilnehmer:innen & Dozent:innen</strong></div>
        <p>Praktische Fallstudie für Data Science im Realeinsatz</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- Datensammlung ---
    st.header("🌍 Datengrundlage")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Herausforderungen
        - 🔒 Zugriffsbeschränkungen (LinkedIn, Indeed)
        - 🛡️ DSGVO-konforme Datenbeschaffung
        - 🌐 Multinationale Jobdaten
        """)

    with col2:
        st.markdown("""
        ### Unsere Lösung
        - 🤖 [Adzuna-API](https://www.adzuna.de) für globale Jobdaten
        - 📊 **3.000+** analysierte Stellenanzeigen
        - 🧹 Automatisierte Bereinigungspipeline
        """)
