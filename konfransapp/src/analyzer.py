"""
Modulo per l'integrazione con Google Gemini API (modello gemini-2.0-flash).
Legge la variabile d'ambiente GEMINI_API_KEY e analizza l'immagine della slide.
"""

import json
import os
import re
from typing import Any, Dict, Optional

import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

from src.i18n import LANGUAGES, build_system_prompt

load_dotenv()

MODEL_NAME = "gemini-1.5-flash"

def get_api_key(override_key: Optional[str] = None) -> Optional[str]:
    """Recupera la chiave API da override manuale, variabile d'ambiente GEMINI_API_KEY o st.secrets."""
    if override_key and override_key.strip():
        return override_key.strip()

    env_key = os.environ.get("GEMINI_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip()

    try:
        import streamlit as st

        if "GEMINI_API_KEY" in st.secrets:
            return str(st.secrets["GEMINI_API_KEY"]).strip()
    except Exception:
        pass

    return None


def analyze_slide_image(
    image: Image.Image,
    lang_code: str = "it",
    api_key_override: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Invia l'immagine della slide al modello gemini-2.0-flash con il system prompt
    per eseguire OCR completo, estrarre le fonti bibliografiche e sintetizzare i concetti chiave.
    """
    api_key = get_api_key(api_key_override)
    if not api_key:
        raise ValueError("MISSING_API_KEY")

    genai.configure(api_key=api_key)

    system_prompt = build_system_prompt(lang_code)
    target_language = LANGUAGES.get(lang_code, LANGUAGES["it"])["name"]

    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=system_prompt,
        generation_config=genai.GenerationConfig(
            temperature=0.2,
            response_mime_type="application/json",
        ),
    )

    user_prompt = (
        f"Analizza questa foto di una slide scattata a una conferenza. "
        f"Esegui l'OCR completo (testo, numeri, grafici), rintraccia tutte le fonti "
        f"bibliografiche o note presenti e genera il riassunto strutturato in lingua {target_language}."
    )

    response = model.generate_content([user_prompt, image])
    raw_text = response.text or "{}"

    return _parse_gemini_json(raw_text)


def _parse_gemini_json(raw_text: str) -> Dict[str, Any]:
    """Effettua il parsing sicuro della risposta JSON restituita da Gemini."""
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw_text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)

    try:
        data = json.loads(cleaned)
        return {
            "concetto_chiave": data.get("concetto_chiave") or "",
            "punti_principali": (
                data.get("punti_principali")
                if isinstance(data.get("punti_principali"), list)
                else []
            ),
            "fonti_citate": (
                data.get("fonti_citate")
                if isinstance(data.get("fonti_citate"), list)
                else []
            ),
            "ocr_completo": data.get("ocr_completo") or "",
        }
    except json.JSONDecodeError:
        return {
            "concetto_chiave": cleaned,
            "punti_principali": [],
            "fonti_citate": [],
            "ocr_completo": cleaned,
        }
