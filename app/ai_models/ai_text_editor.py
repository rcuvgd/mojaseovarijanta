import openai

# Postavi svoj API ključ
openai.api_key = "YOUR_API_KEY"

def generate_updated_text(original_text: str, recommendations: dict, keyword: str, language: str = "srpski") -> str:
    instructions = []

    if recommendations.get("add_words", 0) > 0:
        instructions.append(f"Dodaj još {recommendations['add_words']} reči u tekst.")
    if recommendations.get("adjust_keyword_count", 0) != 0:
        delta = recommendations["adjust_keyword_count"]
        if delta > 0:
            instructions.append(f"Uključi ključnu reč '{keyword}' još {delta} puta u sadržaj.")
        else:
            instructions.append(f"Smanji broj ponavljanja ključne reči '{keyword}' za {abs(delta)} puta.")
    if recommendations.get("h2_missing", 0) > 0:
        instructions.append(f"Dodaj još {recommendations['h2_missing']} H2 podnaslova.")
    if recommendations.get("alt_missing", 0) > 0:
        instructions.append(f"Dodaj ALT opise za još {recommendations['alt_missing']} slika.")

    full_instruction = " ".join(instructions)
    prompt = f"Prepravi sledeći tekst na {language}, vodeći računa o SEO preporukama:

{full_instruction}

Originalni tekst:
{original_text}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ti si SEO stručnjak i pisac sadržaja."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    ai_generated_text = response.choices[0].message["content"]

    # Označi dodat tekst za AI detekciju
    wrapped_text = f"{original_text}

<!-- AI_START -->
{ai_generated_text}
<!-- AI_END -->"

    return wrapped_text
