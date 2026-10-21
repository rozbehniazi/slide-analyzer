# SlideLens — Analisi Slide per Conferenze e Congressi (Streamlit)

Web app responsive **mobile-first** sviluppata in **Streamlit** per fotografare o caricare slide durante conferenze e congressi ed estrarre automaticamente contenuti strutturati tramite **Google Gemini (`gemini-1.5-flash`)**.

## Struttura del Progetto
```text
konfransapp/
├── .streamlit/
│   └── config.toml        # Tema pulito e configurazione server Streamlit
├── src/
│   ├── __init__.py
│   ├── analyzer.py        # Connessione a Gemini API (gemini-1.5-flash) tramite GEMINI_API_KEY
│   └── i18n.py            # Traduzioni UI e System Prompt (IT, EN, SV, CA, ES)
├── app.py                 # Entrypoint principale dell'applicazione Streamlit
├── requirements.txt       # Dipendenze Python
├── .env.example           # Template per la variabile d'ambiente GEMINI_API_KEY
└── README.md
```

## Funzionalità
- **Selettore Lingua (5 lingue)**: Italiano (`IT`), Inglese (`EN`), Svedese (`SV`), Catalano (`CA`) e Spagnolo (`ES`), che aggiorna sia l'interfaccia sia la lingua di output di Gemini.
- **Upload / Fotocamera Mobile-First**: Schede dedicate `st.file_uploader` (**Carica Immagine**) e `st.camera_input` (**Scatta Foto**).
- **Analisi con `gemini-1.5-flash`**:
  1. Esegue l'**OCR completo** di testo, numeri, tabelle e grafici.
  2. Rintraccia ed elenca le **fonti bibliografiche** o note presenti nella slide.
  3. Genera un **riassunto chiaro e sintetico** dei concetti chiave.
- **Risultati formattati in 3 sezioni chiare**:
  1. **💡 Concetto Chiave**
  2. **📌 Punti Principali**
  3. **📚 Fonti Citate**
  *(più un pannello espandibile per l'**OCR Completo** e il pulsante per scaricare gli appunti in `.md`).*

## Avvio Rapido

1. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
2. Configura la variabile d'ambiente `GEMINI_API_KEY` (oppure copia `.env.example` in `.env`):
   ```bash
   export GEMINI_API_KEY="la_tua_chiave_api"
   ```
3. Avvia l'app Streamlit:
   ```bash
   streamlit run app.py
   ```
