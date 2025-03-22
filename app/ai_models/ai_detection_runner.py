from transformers import pipeline
from ai_models.ai_detector_exporter import extract_from_file

def detect_ai_generated_text_from_file(input_path: str):
    try:
        # Prvo izdvojimo AI tekst
        success = extract_from_file(input_path)
        if not success:
            return "⚠️ AI deo nije pronađen."

        # Učitamo izdvojen tekst
        with open("ai_models/ai_generated_fragment.txt", "r", encoding="utf-8") as f:
            ai_text = f.read()

        # Detektor iz HuggingFace
        detector = pipeline("text-classification", model="roberta-base-openai-detector")
        result = detector(ai_text[:512])  # modeli često ograničeni na 512 tokena

        return result
    except Exception as e:
        return f"❌ Greška u detekciji: {e}"
