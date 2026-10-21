"""
Dizionario traduzioni multilingua (Italiano, Inglese, Svedese, Catalano, Spagnolo)
e generatore del System Prompt per Gemini 1.5 Flash.
"""

from typing import Dict

LANGUAGES: Dict[str, Dict[str, str]] = {
    "it": {"label": "🇮🇹 Italiano", "name": "Italiano"},
    "en": {"label": "🇬🇧 English", "name": "English"},
    "sv": {"label": "🇸🇪 Svenska", "name": "Svenska"},
    "ca": {"label": "🏴󠁥󠁳󠁣󠁴󠁿 Català", "name": "Català"},
    "es": {"label": "🇪🇸 Español", "name": "Español"},
}

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "it": {
        "app_title": "SlideLens",
        "app_subtitle": "Analisi intelligente di slide per conferenze e congressi",
        "lang_selector_label": "🌐 Lingua / Language",
        "tab_upload": "📁 Carica Immagine",
        "tab_camera": "📷 Scatta Foto",
        "upload_label": "Seleziona o trascina la foto di una slide (JPG, PNG, WEBP)",
        "camera_label": "Inquadra la slide e scatta una foto",
        "preview_caption": "Anteprima della slide selezionata",
        "analyze_btn": "⚡ Analizza Slide",
        "spinner_text": "Analisi della slide in corso con gemini-1.5-flash (OCR, grafici e fonti)...",
        "section_key_concept": "💡 Concetto Chiave",
        "section_main_points": "📌 Punti Principali",
        "section_sources": "📚 Fonti Citate",
        "section_ocr": "🔍 OCR Completo (Testo, Numeri e Grafici)",
        "no_key_concept": "Nessun concetto chiave rilevato.",
        "no_main_points": "Nessun punto principale estratto.",
        "no_sources": "Nessuna fonte bibliografica o nota rilevata nella slide.",
        "no_ocr": "Nessun testo OCR estratto.",
        "error_missing_key": (
            "Variabile d'ambiente `GEMINI_API_KEY` non trovata. "
            "Impostala nel tuo ambiente (`export GEMINI_API_KEY=...`), nel file `.env` "
            "oppure inseriscila nelle impostazioni avanzate qui sotto."
        ),
        "api_expander": "⚙️ Configurazione API Key (opzionale)",
        "api_input_label": "GEMINI_API_KEY (lascia vuoto per usare la variabile d'ambiente)",
        "error_analysis": "Si è verificato un errore durante l'analisi della slide",
        "download_btn": "📥 Scarica Appunti (.md)",
    },
    "en": {
        "app_title": "SlideLens",
        "app_subtitle": "Smart slide analysis for conferences & congresses",
        "lang_selector_label": "🌐 Language",
        "tab_upload": "📁 Upload Image",
        "tab_camera": "📷 Take Photo",
        "upload_label": "Select or drag & drop a slide photo (JPG, PNG, WEBP)",
        "camera_label": "Frame the slide and take a photo",
        "preview_caption": "Selected slide preview",
        "analyze_btn": "⚡ Analyze Slide",
        "spinner_text": "Analyzing slide with gemini-1.5-flash (OCR, charts & references)...",
        "section_key_concept": "💡 Key Concept",
        "section_main_points": "📌 Main Points",
        "section_sources": "📚 Cited Sources",
        "section_ocr": "🔍 Full OCR (Text, Numbers & Charts)",
        "no_key_concept": "No key concept detected.",
        "no_main_points": "No main points extracted.",
        "no_sources": "No bibliographic sources or notes detected on the slide.",
        "no_ocr": "No OCR text extracted.",
        "error_missing_key": (
            "Environment variable `GEMINI_API_KEY` not found. "
            "Set it in your environment (`export GEMINI_API_KEY=...`), in `.env`, "
            "or enter it in the advanced settings below."
        ),
        "api_expander": "⚙️ API Key Configuration (optional)",
        "api_input_label": "GEMINI_API_KEY (leave empty to use environment variable)",
        "error_analysis": "An error occurred while analyzing the slide",
        "download_btn": "📥 Download Notes (.md)",
    },
    "sv": {
        "app_title": "SlideLens",
        "app_subtitle": "Smart bildanalys för konferenser och kongresser",
        "lang_selector_label": "🌐 Språk / Language",
        "tab_upload": "📁 Ladda upp Bild",
        "tab_camera": "📷 Ta Foto",
        "upload_label": "Välj eller dra och släpp ett foto av en presentationsbild (JPG, PNG, WEBP)",
        "camera_label": "Rama in bilden och ta ett foto",
        "preview_caption": "Förhandsgranskning av vald bild",
        "analyze_btn": "⚡ Analysera Bild",
        "spinner_text": "Analyserar bild med gemini-1.5-flash (OCR, diagram och källor)...",
        "section_key_concept": "💡 Huvudbudskap",
        "section_main_points": "📌 Viktiga Punkter",
        "section_sources": "📚 Citerade Källor",
        "section_ocr": "🔍 Fullständig OCR (Text, Siffror och Diagram)",
        "no_key_concept": "Inget huvudbudskap hittades.",
        "no_main_points": "Inga viktiga punkter extraherades.",
        "no_sources": "Inga bibliografiska källor eller fotnoter hittades på bilden.",
        "no_ocr": "Ingen OCR-text extraherades.",
        "error_missing_key": (
            "Miljövariabeln `GEMINI_API_KEY` hittades inte. "
            "Ange den i din miljö (`export GEMINI_API_KEY=...`), i `.env` "
            "eller fyll i den under avancerade inställningar nedan."
        ),
        "api_expander": "⚙️ Konfigurera API-nyckel (valfritt)",
        "api_input_label": "GEMINI_API_KEY (lämna tomt för att använda miljövariabel)",
        "error_analysis": "Ett fel uppstod vid analys av bilden",
        "download_btn": "📥 Ladda ner Anteckningar (.md)",
    },
    "ca": {
        "app_title": "SlideLens",
        "app_subtitle": "Anàlisi intel·ligent de diapositives per a conferències i congressos",
        "lang_selector_label": "🌐 Idioma / Language",
        "tab_upload": "📁 Puja Imatge",
        "tab_camera": "📷 Fes Foto",
        "upload_label": "Selecciona o arrossega la foto d'una diapositiva (JPG, PNG, WEBP)",
        "camera_label": "Enquadra la diapositiva i fes una foto",
        "preview_caption": "Previsualització de la diapositiva seleccionada",
        "analyze_btn": "⚡ Analitza la Diapositiva",
        "spinner_text": "Analitzant la diapositiva amb gemini-1.5-flash (OCR, gràfics i fonts)...",
        "section_key_concept": "💡 Concepte Clau",
        "section_main_points": "📌 Punts Principals",
        "section_sources": "📚 Fonts Citades",
        "section_ocr": "🔍 OCR Complet (Text, Números i Gràfics)",
        "no_key_concept": "Cap concepte clau detectat.",
        "no_main_points": "No s'han extret punts principals.",
        "no_sources": "No s'han detectat fonts bibliogràfiques ni notes a la diapositiva.",
        "no_ocr": "No s'ha extret cap text OCR.",
        "error_missing_key": (
            "No s'ha trobat la variable d'entorn `GEMINI_API_KEY`. "
            "Defineix-la al teu entorn (`export GEMINI_API_KEY=...`), al fitxer `.env` "
            "o introdueix-la a la configuració avançada a sota."
        ),
        "api_expander": "⚙️ Configuració de Clau API (opcional)",
        "api_input_label": "GEMINI_API_KEY (deixa-ho buit per usar la variable d'entorn)",
        "error_analysis": "S'ha produït un error durant l'anàlisi de la diapositiva",
        "download_btn": "📥 Descarrega Apunts (.md)",
    },
    "es": {
        "app_title": "SlideLens",
        "app_subtitle": "Análisis inteligente de diapositivas para conferencias y congresos",
        "lang_selector_label": "🌐 Idioma / Language",
        "tab_upload": "📁 Subir Imagen",
        "tab_camera": "📷 Tomar Foto",
        "upload_label": "Selecciona o arrastra la foto de una diapositiva (JPG, PNG, WEBP)",
        "camera_label": "Encuadra la diapositiva y toma una foto",
        "preview_caption": "Vista previa de la diapositiva seleccionada",
        "analyze_btn": "⚡ Analizar Diapositiva",
        "spinner_text": "Analizando la diapositiva con gemini-1.5-flash (OCR, gráficos y fuentes)...",
        "section_key_concept": "💡 Concepto Clave",
        "section_main_points": "📌 Puntos Principales",
        "section_sources": "📚 Fuentes Citadas",
        "section_ocr": "🔍 OCR Completo (Texto, Números y Gráficos)",
        "no_key_concept": "Ningún concepto clave detectado.",
        "no_main_points": "No se extrajeron puntos principales.",
        "no_sources": "No se detectaron fuentes bibliográficas ni notas en la diapositiva.",
        "no_ocr": "No se extrajo texto OCR.",
        "error_missing_key": (
            "No se encontró la variable de entorno `GEMINI_API_KEY`. "
            "Configúrala en tu entorno (`export GEMINI_API_KEY=...`), en el archivo `.env` "
            "o introdúcela en la configuración avanzada abajo."
        ),
        "api_expander": "⚙️ Configuración de API Key (opcional)",
        "api_input_label": "GEMINI_API_KEY (déjalo vacío para usar la variable de entorno)",
        "error_analysis": "Ocurrió un error durante el análisis de la diapositiva",
        "download_btn": "📥 Descargar Apuntes (.md)",
    },
}


def build_system_prompt(lang_code: str) -> str:
    """Costruisce il system prompt istruito per rispondere nella lingua selezionata."""
    target_language = LANGUAGES.get(lang_code, LANGUAGES["it"])["name"]
    return f"""Sei un assistente esperto nell'analisi di slide presentate a conferenze scientifiche, mediche, tecnologiche e congressi professionali.
Analizza attentamente l'immagine della slide fornita ed esegui i seguenti compiti:
1. Esegui l'OCR completo ed accurato di tutto il testo visibile, inclusi numeri, tabelle, assi, etichette e andamenti dei grafici.
2. Rintraccia ed elenca tutte le fonti bibliografiche, citazioni (es. Autore et al., anno, rivista, DOI, link) o note a piè di pagina presenti nella slide.
3. Genera un riassunto chiaro, rigoroso e sintetico dei concetti chiave espressi nella slide.

IMPORTANTE: Scrivi il riassunto ("concetto_chiave"), i punti principali ("punti_principali") e la descrizione dei grafici in lingua: {target_language}.

Rispondi ESCLUSIVAMENTE con un oggetto JSON valido (senza blocchi markdown ```json) con questa esatta struttura:
{{
  "concetto_chiave": "Sintesi chiara e diretta (2-3 frasi) in {target_language} del messaggio principale e della conclusione centrale della slide.",
  "punti_principali": [
    "Punto chiave 1 in {target_language} (includendo eventuali dati numerici o evidenze dai grafici)",
    "Punto chiave 2 in {target_language}",
    "Punto chiave 3 in {target_language}"
  ],
  "fonti_citate": [
    "Fonte bibliografica 1 o nota a piè di pagina esattamente come riportata nella slide"
  ],
  "ocr_completo": "Trascrizione completa e strutturata di tutto il testo, numeri, tabelle e descrizione dettagliata dei dati presenti nei grafici."
}}
Se nella slide non è presente alcuna fonte bibliografica o nota, restituisci una lista vuota [] per "fonti_citate"."""
