import openai

# Postavi svoj API ključ
openai.api_key = "YOUR_API_KEY"

def humanize_text(ai_text: str, language: str = "srpski") -> str:
    prompt = (
        f"Prepravi sledeći tekst na način da zvuči prirodnije, kao da ga je pisao čovek, ali zadrži istu poruku. "
        f"Piši na jeziku: {language}.

Tekst:
{ai_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ti si profesionalni urednik koji prepravlja AI tekstove da zvuče ljudski."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message["content"]
