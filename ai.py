"""Assistant IA de Cap Pro (Groq, API compatible OpenAI).

Clés à définir (secrets Streamlit Cloud ou variables d'environnement) :
  GROQ_API_KEY   obligatoire
  GROQ_MODEL     facultatif (modèle Groq à utiliser)
  DAILY_AI_LIMIT facultatif (questions IA par élève et par jour, 20 par défaut)
"""
import os

import requests
import streamlit as st

import content

API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "llama-3.3-70b-versatile"


def _setting(name, default=""):
    try:
        value = st.secrets.get(name)
    except Exception:  # pas de fichier de secrets
        value = None
    return str(value) if value else os.getenv(name, default)


def daily_limit():
    try:
        return int(_setting("DAILY_AI_LIMIT", "20"))
    except ValueError:
        return 20


def is_configured():
    return bool(_setting("GROQ_API_KEY"))


def ask(mode, history, filiere=""):
    """Retourne (réponse, erreur). `history` = liste de {role, content}."""
    key = _setting("GROQ_API_KEY")
    if not key:
        return None, "L'assistant IA n'est pas encore activé (clé GROQ_API_KEY manquante)."

    system = content.SYSTEM_PROMPTS[mode]
    if filiere:
        system += f" L'élève est dans la filière : {filiere}."
    messages = [{"role": "system", "content": system}] + history[-8:]

    try:
        r = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {key}"},
            json={
                "model": _setting("GROQ_MODEL", DEFAULT_MODEL),
                "messages": messages,
                "max_tokens": 500,
                "temperature": 0.4,
            },
            timeout=30,
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip(), None
    except Exception:
        return None, "Désolé, je n'arrive pas à répondre pour le moment. Réessaie dans un instant."
