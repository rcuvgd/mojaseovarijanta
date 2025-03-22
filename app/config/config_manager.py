import json
import os

CONFIG_PATH = "config/config.json"

DEFAULT_CONFIG = {
    "output_folder": "output",
    "database_folder": "database",
    "max_humanization_attempts": 3,
    "ai_score_threshold": 0.4,
    "language": "srpski",
    "output_format": "txt",
    "use_chatgpt": True,
    "use_undetectable": False
}

def load_config(path: str = CONFIG_PATH) -> dict:
    if not os.path.exists(path):
        save_config(DEFAULT_CONFIG, path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config: dict, path: str = CONFIG_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
