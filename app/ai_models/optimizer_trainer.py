import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from ai_models.optimizer_model import SEOOptimizerModel, train_optimizer_model

# Učitaj dataset
data = pd.read_csv("ai_models/optimizer_training_data.csv")

# Ulazi
X = data[[
    "total_score", "domain_authority", "naslov_jaci_od",
    "opis_duzi_od", "keyword_u_naslovu",
    "nas_prosek", "prosek_reci_konkurencije"
]]

# Izlazi
y = data[[
    "add_words", "adjust_keyword_count", "h2_missing", "alt_missing"
]]

# Skaliranje ulaza
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Podela train/test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Tensor konverzija
X_tensor = torch.tensor(X_train, dtype=torch.float32)
y_tensor = torch.tensor(y_train.values, dtype=torch.float32)

# Treniraj model
model = SEOOptimizerModel(input_size=7)
train_optimizer_model(model, X_tensor, y_tensor, epochs=150)

# Sačuvaj model
torch.save(model.state_dict(), "ai_models/seo_optimizer_model.pt")
print("✅ Optimizer model sačuvan kao seo_optimizer_model.pt")
