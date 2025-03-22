import re

def extract_ai_generated_text(text: str) -> str:
    match = re.search(r"<!-- AI_START -->(.*?)<!-- AI_END -->", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def extract_from_file(input_path: str, output_path: str = "ai_models/ai_generated_fragment.txt") -> bool:
    try:
        with open(input_path, "r", encoding="utf-8") as file:
            full_text = file.read()
        ai_text = extract_ai_generated_text(full_text)
        if ai_text:
            with open(output_path, "w", encoding="utf-8") as out_file:
                out_file.write(ai_text)
            print(f"✅ AI tekst izdvojen u: {output_path}")
            return True
        else:
            print("⚠️ Nema AI označenog sadržaja u fajlu.")
            return False
    except Exception as e:
        print(f"❌ Greška: {e}")
        return False
