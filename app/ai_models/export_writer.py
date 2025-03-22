import os
import json

def save_text_and_metrics(output_dir: str, title: str, content: str, metrics: dict, status: str = "success"):
    # Napravi folder ako ne postoji
    os.makedirs(output_dir, exist_ok=True)

    # Generiši ime fajla
    safe_title = title.replace(" ", "_").replace("/", "-").lower()
    base_name = f"{safe_title}_{status}"
    txt_path = os.path.join(output_dir, base_name + ".txt")
    json_path = os.path.join(output_dir, base_name + "_metrics.json")

    # Snimi sadržaj
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Snimi metrike
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    return txt_path, json_path
