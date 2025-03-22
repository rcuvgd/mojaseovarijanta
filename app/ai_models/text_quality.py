import textstat

def analyze_text_quality(text: str) -> dict:
    result = {
        "flesch_reading_ease": round(textstat.flesch_reading_ease(text), 2),
        "flesch_kincaid_grade": round(textstat.flesch_kincaid_grade(text), 2),
        "gunning_fog": round(textstat.gunning_fog(text), 2),
        "smog_index": round(textstat.smog_index(text), 2),
        "automated_readability_index": round(textstat.automated_readability_index(text), 2),
        "coleman_liau_index": round(textstat.coleman_liau_index(text), 2),
        "linsear_write_formula": round(textstat.linsear_write_formula(text), 2),
        "dale_chall_score": round(textstat.dale_chall_readability_score(text), 2),
        "difficult_words": textstat.difficult_words(text),
        "syllable_count": textstat.syllable_count(text),
        "sentence_count": textstat.sentence_count(text),
        "avg_sentence_length": round(len(text.split()) / max(1, textstat.sentence_count(text)), 2),
        "word_count": textstat.lexicon_count(text, removepunct=True),
    "avg_word_length": round(sum(len(w) for w in text.split()) / max(1, len(text.split())), 2)
    }

    # Rezervisana mesta za druge biblioteke
    result["writegood_flags"] = "TODO"  # stil greške (engleski)
    result["spacy_nlp_flags"] = "TODO"  # NLP analiza

    return result
