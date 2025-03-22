import pandas as pd
import time

from ai_models.ai_text_editor import generate_updated_text
from ai_models.ai_humanizer import humanize_text
from ai_models.ai_detector_exporter import extract_ai_generated_text
from ai_models.ai_detection_runner import detect_ai_generated_text_from_file

# Podesivi parametri
MAX_ATTEMPTS = 3
LANGUAGE = "srpski"
KEYWORD = "seo strategija"

def generate_text_from_title(title: str, subtitle: str = "") -> str:
    # Dummy generacija, zameniti GPT pozivom
    return f"<!-- AI_START -->\nOvo je automatski tekst za: {title}. {subtitle}\n<!-- AI_END -->"

def evaluate_ai_score(text: str) -> float:
    result = detect_ai_generated_text_from_file(text)
    if isinstance(result, list) and "score" in result[0]:
        return result[0]["score"]
    return 1.0  # fallback - smatra se AI

def process_row(title, subtitle=""):
    original_text = generate_text_from_title(title, subtitle)
    ai_text = extract_ai_generated_text(original_text)

    for attempt in range(MAX_ATTEMPTS):
        print(f"🔁 Humanizacija pokušaj {attempt + 1}...")
        humanized = humanize_text(ai_text, language=LANGUAGE)
        full_text = f"{original_text}\n\n<!-- AI_START -->\n{humanized}\n<!-- AI_END -->"

        with open("temp_humanized.txt", "w", encoding="utf-8") as f:
            f.write(full_text)

        score = evaluate_ai_score("temp_humanized.txt")
        print(f"🎯 AI score: {score:.2f}")

        if score < 0.4:  # zadovoljava kriterijum
            print("✅ Humanizovano uspešno.")
            return full_text, "success"

    print("❌ Nije humanizovano dovoljno nakon više pokušaja.")
    return full_text, "failed"

def run_pipeline_from_excel(path="tekstovi.xls"):
    df = pd.read_excel(path)
    results = []

    for idx, row in df.iterrows():
        title = row.get("Naslov", "")
        subtitle = row.get("Podnaslov", "")
        if not title:
            continue

        print(f"🚀 Obrada: {title}")
        text, status = process_row(title, subtitle)
        results.append({
            "title": title,
            "status": status,
            "text": text
        })

        time.sleep(2)  # pauza između obrada

    print("📦 Završeno. Rezultati:", results)
