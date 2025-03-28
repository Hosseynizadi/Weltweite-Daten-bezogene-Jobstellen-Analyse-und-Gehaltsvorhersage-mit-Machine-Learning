import streamlit as st 


    
st.markdown("""
<style>
    .conclusion-section {
        border-left: 4px solid #3498db;
        padding: 0.5rem 1rem;
        margin: 1rem 0;
        background: #f8f9fa;
    }
    .emphasis-text {
        color: #2c3e50;
        font-size: 1.1em;
        line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

def app():
    
    st.header("Fazit")

    col1, col2 = st.columns([0.7, 0.3])
    with col1:
        st.markdown("""
        <div class="emphasis-text">
        
        🧩 **Vom Rohmaterial zur Prognose**  
        Die intensive Datensammlung durch Web Scraping – trotz initialer Hürden bei Zugriffsbeschränkungen und DSGVO –
        legte das Fundament für unsere Analysen. Aus über 3.000 Jobprofilen filterten wir:
        
        <div class="conclusion-section">
        🔍 <strong>Kernmuster heraus:</strong><br>
        - Starker Gehaltsanstieg bei Cloud-Kompetenzen (+23%)<br>
        - 15% Lohngefälle EU-USA bei Senior-Positionen<br>
        - Remote-Optionen beeinflussen Gehälter regional unterschiedlich
        </div>
        
        💡 **Modellierungserfolge**  
        Die Kombination aus Random-Forest-Regression und Natural Language Processing für Skill-Extraction ermöglichte:
        
        <div class="conclusion-section">
        - Vorhersagegenauigkeit (R²) von 0.87<br>
        - Identifikation von 12 Schlüsselfaktoren<br>
        - Automatisierte Trenderkennung in Jobbeschreibungen
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1534/1534959.png", width=120)
        st.markdown("""
        <div style="background:#e3f2fd; padding:1rem; border-radius:10px;">
        <small>„Die Daten zeigen klar: Spezialwissen in<br>
        <strong>MLOps</strong> (+19%) und<br>
        <strong>Data Governance</strong> (+27%)<br>
        bringt Premiumgehälter"</small>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
 <div class="emphasis-text">
    <strong>🔍 Gesamteinschätzung</strong>       
    Dieses Projekt unterstreicht, dass selbst komplexe Gehaltsgeflechte durch systematische Datenanalyse entschlüsselbar sind. 
    Die identifizierten Muster bieten sowohl Bewerbern <span style="color: #27ae60;">(Verhandlungsgrundlage)</span> als auch Unternehmen 
    <span style="color: #2980b9;">(Marktbenchmarks)</span> konkreten Mehrwert.
</div>
""", unsafe_allow_html=True)

    st.divider()

    st.header("Ausblick")
    st.write("""Um die Präzision unserer Gehaltsvorhersagen weiter zu steigern, sind mehrere spannende Erweiterungen geplant:  

**1. Globale Datensynergie**  
Durch die Integration weiterer Jobplattformen (Glassdoor, StepStone, regionale Anbieter) und die Nutzung von Echtzeitdatenströmen soll der Datensatz quantitativ und qualitativ wachsen. Ein Fokus liegt auf der Erfassung branchenspezifischer Nuancen und nicht-westlicher Märkte wie China oder Indien.  

**2. Predictive Power Boost**  
Die Einbindung neuer Parameter wird das Modell verfeinern:  
- 🔍 **Unternehmensbewertungen** (Kununu/Glassdoor-Scores)  
- 🎓 **Zertifizierungen** (Cloud, KI-Spezialisierungen)  
- 🌱 **Emerging Tech** (Einfluss von LLMs, Quantum Computing)  

**3. Dynamische Marktanalysen**  
Durch vergleichende Studien zwischen USA, Europa und China sollen regionale Unterschiede in Bezug auf:  
- 💸 Wirtschaftliche Rahmenbedingungen  
- 📜 Regulatorische Vorgaben (z.B. KI-Regulierung EU vs. China)  
- 🌍 Kulturelle Einflüsse auf Gehaltsverhandlungen  

herausgearbeitet werden.  

**4. Interaktive Zukunftsszenarien**  
Geplante Features wie ein "Was-wäre-wenn"-Modul ermöglichen Nutzer:innen, die Auswirkungen von Karriereentscheidungen (Weiterbildungen, Standortwechsel) simulieren zu lassen.  

Mit diesen Schritten soll die Plattform nicht nur zum Prognose-Tool, sondern zu einem lebendigen Ökosystem für Arbeitsmarkttransparenz und Data-Science-Education werden.""")