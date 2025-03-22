import requests

def humanize_with_undetectable(ai_text: str, api_key: str, language: str = "sr") -> str:
    url = "https://api.undetectable.ai/api/content/humanize"

    payload = {
        "content": ai_text,
        "input_lang": language,
        "output_lang": language,
        "quality": "high",
        "mode": "accurate"
    }

    headers = {
        "Content-Type": "application/json",
        "X-API-KEY": api_key
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("humanized_content", "⚠️ Nema odgovora.")
    except Exception as e:
        return f"❌ Greška prilikom poziva Undetectable.ai: {e}"
