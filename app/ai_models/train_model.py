import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ai_models.seo_backlink_predictor import SEOBacklinkPredictor, train_model

# Load CSV
data = pd.read_csv("ai_models/train_data.csv")

# Input i output kolone
X = data[[
    "total_score", "domain_authority", "naslov_jaci_od",
    "opis_duzi_od", "keyword_u_naslovu",
    "nas_prosek", "prosek_reci_konkurencije"
]]
y = data[["backlinks_top10", "backlinks_top3", "backlinks_top1"]]

# Normalizacija
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Podela na train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Pretvori u torch tenzore
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train.values, dtype=torch.float32)

# Inicijalizuj i treniraj model
model = SEOBacklinkPredictor(input_size=7)
train_model(model, X_train_tensor, y_train_tensor, epochs=200)

# Snimi model
torch.save(model.state_dict(), "ai_models/backlink_model.pt")
print("✅ Model sačuvan kao backlink_model.pt")
