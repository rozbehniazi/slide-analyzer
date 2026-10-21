"""
SlideLens — Web App Streamlit (Mobile-First) per analizzare foto di slide
scattate a conferenze e congressi tramite Google Gemini (gemini-1.5-flash).
"""

import streamlit as st
from PIL import Image

from src.analyzer import analyze_slide_image, get_api_key
from src.i18n import LANGUAGES, TRANSLATIONS

st.set_page_config(
    page_title="SlideLens — Conference Slide Analyzer",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Stile CSS Mobile-First pulito e ad alto contrasto
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 3rem;
        max-width: 700px;
    }
    .app-header-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #ffffff;
        padding: 1.25rem 1.4rem;
        border-radius: 16px;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.12);
    }
    .app-header-card h1 {
        color: #ffffff !important;
        font-size: 1.55rem !important;
        font-weight: 700 !important;
        margin: 0 0 0.25rem 0 !important;
        padding: 0 !important;
    }
    .app-header-card p {
        color: #cbd5e1 !important;
        font-size: 0.92rem !important;
        margin: 0 !important;
    }
    .result-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 1.15rem 1.25rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
    }
    .card-key {
        border-left: 5px solid #f59e0b;
        background: #fffdf7;
    }
    .card-points {
        border-left: 5px solid #2563eb;
    }
    .card-sources {
        border-left: 5px solid #10b981;
    }
    .result-card h3 {
        margin-top: 0 !important;
        margin-bottom: 0.65rem !important;
        font-size: 1.1rem !important;
        color: #0f172a !important;
    }
    .result-card p, .result-card li {
        color: #1e293b;
        font-size: 0.97rem;
        line-height: 1.55;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def format_markdown_report(result: dict, t: dict) -> str:
    """Formatta i risultati in un file Markdown scaricabile."""
    points_md = (
        "\n".join(f"- {p}" for p in result.get("punti_principali", []))
        or f"- _{t['no_main_points']}_"
    )
    sources_md = (
        "\n".join(f"- {s}" for s in result.get("fonti_citate", []))
        or f"- _{t['no_sources']}_"
    )
    return (
        f"# {t['app_title']} — Report\n\n"
        f"## {t['section_key_concept']}\n"
        f"{result.get('concetto_chiave') or t['no_key_concept']}\n\n"
        f"## {t['section_main_points']}\n"
        f"{points_md}\n\n"
        f"## {t['section_sources']}\n"
        f"{sources_md}\n\n"
        f"## {t['section_ocr']}\n"
        f"```text\n{result.get('ocr_completo') or t['no_ocr']}\n```\n"
    )


def main() -> None:
    if "lang" not in st.session_state:
        st.session_state.lang = "it"

    # Barra superiore: Selettore Lingua (IT, EN, SV, CA, ES)
    col_spacer, col_lang = st.columns([2, 1.3])
    with col_lang:
        selected_lang = st.selectbox(
            label=TRANSLATIONS[st.session_state.lang]["lang_selector_label"],
            options=list(LANGUAGES.keys()),
            index=list(LANGUAGES.keys()).index(st.session_state.lang),
            format_func=lambda code: LANGUAGES[code]["label"],
            key="lang_selector",
        )
        if selected_lang != st.session_state.lang:
            st.session_state.lang = selected_lang
            st.rerun()

    t = TRANSLATIONS[st.session_state.lang]

    # Header principale
    st.markdown(
        f"""
        <div class="app-header-card">
            <h1>📊 {t["app_title"]}</h1>
            <p>{t["app_subtitle"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Configurazione opzionale API Key (di default usa la variabile d'ambiente GEMINI_API_KEY)
    api_key_override = None
    if not get_api_key():
        with st.expander(t["api_expander"], expanded=True):
            api_key_override = st.text_input(
                t["api_input_label"],
                type="password",
                placeholder="AIza...",
            )
    else:
        with st.expander(t["api_expander"], expanded=False):
            api_key_override = st.text_input(
                t["api_input_label"],
                type="password",
                placeholder="AIza...",
            )

    # Interfaccia Mobile-First: Carica Immagine oppure Scatta Foto
    tab_upload, tab_camera = st.tabs([t["tab_upload"], t["tab_camera"]])

    uploaded_file = None
    camera_photo = None

    with tab_upload:
        uploaded_file = st.file_uploader(
            t["upload_label"],
            type=["jpg", "jpeg", "png", "webp"],
        )

    with tab_camera:
        camera_photo = st.camera_input(t["camera_label"])

    image_source = camera_photo if camera_photo is not None else uploaded_file

    if image_source is not None:
        image = Image.open(image_source)
        st.image(image, caption=t["preview_caption"], use_container_width=True)

        if st.button(t["analyze_btn"], type="primary", use_container_width=True):
            with st.spinner(t["spinner_text"]):
                try:
                    result = analyze_slide_image(
                        image=image,
                        lang_code=st.session_state.lang,
                        api_key_override=api_key_override,
                    )
                    st.session_state.last_result = result
                except ValueError as err:
                    if str(err) == "MISSING_API_KEY":
                        st.error(t["error_missing_key"])
                    else:
                        st.error(f"{t['error_analysis']}: {err}")
                except Exception as exc:
                    st.error(f"{t['error_analysis']}: {exc}")

    # Visualizzazione dei risultati in 3 sezioni chiare:
    # 1. Concetto Chiave | 2. Punti Principali | 3. Fonti Citate
    if "last_result" in st.session_state and image_source is not None:
        res = st.session_state.last_result
        st.divider()

        # 1. CONCETTO CHIAVE
        concetto = res.get("concetto_chiave") or t["no_key_concept"]
        st.markdown(
            f"""
            <div class="result-card card-key">
                <h3>{t["section_key_concept"]}</h3>
                <p>{concetto}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 2. PUNTI PRINCIPALI
        punti = res.get("punti_principali") or []
        if punti:
            items_html = "".join(f"<li>{p}</li>" for p in punti)
            points_body = f"<ul>{items_html}</ul>"
        else:
            points_body = f"<p><em>{t['no_main_points']}</em></p>"

        st.markdown(
            f"""
            <div class="result-card card-points">
                <h3>{t["section_main_points"]}</h3>
                {points_body}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 3. FONTI CITATE
        fonti = res.get("fonti_citate") or []
        if fonti:
            sources_html = "".join(f"<li>{s}</li>" for s in fonti)
            sources_body = f"<ul>{sources_html}</ul>"
        else:
            sources_body = f"<p><em>{t['no_sources']}</em></p>"

        st.markdown(
            f"""
            <div class="result-card card-sources">
                <h3>{t["section_sources"]}</h3>
                {sources_body}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Dettaglio espandibile OCR Completo (Testo, Numeri e Grafici)
        with st.expander(t["section_ocr"]):
            st.text(res.get("ocr_completo") or t["no_ocr"])

        # Pulsante per scaricare gli appunti in Markdown
        md_report = format_markdown_report(res, t)
        st.download_button(
            label=t["download_btn"],
            data=md_report,
            file_name="slidelens_notes.md",
            mime="text/markdown",
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
