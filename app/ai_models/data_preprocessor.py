import csv
from typing import List, Dict

FEATURE_NAMES = [
    "total_score",
    "domain_authority",
    "naslov_jaci_od",
    "opis_duzi_od",
    "keyword_u_naslovu",
    "nas_prosek",
    "prosek_reci_konkurencije"
]

TARGET_NAMES = ["backlinks_top10", "backlinks_top3", "backlinks_top1"]

def extract_features_from_report(report: Dict, domain_authority: float, targets: List[int]) -> Dict:
    score = report.get("seo_score", {})
    competition = report.get("competition", {})

    features = {
        "total_score": score.get("total_score", 0),
        "domain_authority": domain_authority,
        "naslov_jaci_od": competition.get("naslov_jaci_od", 0),
        "opis_duzi_od": competition.get("opis_duzi_od", 0),
        "keyword_u_naslovu": competition.get("keyword_u_naslovu", 0),
        "nas_prosek": competition.get("nas_prosek", 0),
        "prosek_reci_konkurencije": competition.get("prosek_reci_konkurencije", 0),
        "backlinks_top10": targets[0],
        "backlinks_top3": targets[1],
        "backlinks_top1": targets[2]
    }

    return features

def save_reports_to_csv(data: List[Dict], path: str = "ai_models/train_data.csv"):
    with open(path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FEATURE_NAMES + TARGET_NAMES)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
