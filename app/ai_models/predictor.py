import torch
from ai_models.seo_backlink_predictor import SEOBacklinkPredictor, predict_backlinks
from sklearn.preprocessing import StandardScaler
import numpy as np

# Učitaj trenirani model
model = SEOBacklinkPredictor(input_size=7)
model.load_state_dict(torch.load("ai_models/backlink_model.pt"))
model.eval()

# Unesi ulazne vrednosti
# total_score, domain_authority, naslov_jaci_od, opis_duzi_od, keyword_u_naslovu, nas_prosek, prosek_reci_konkurencije
input_data = [88, 25, 4, 3, 5, 732, 750]  # Primer

# Skaliraj input sa istom logikom kao pri treniranju
scaler = StandardScaler()
scaler.fit(np.array([input_data]))  # Pretpostavka: koristiš isti scaler ako ga snimaš kasnije

scaled_input = scaler.transform([input_data])
predictions = predict_backlinks(model, scaled_input[0])

print(f"🔮 Predikcija backlinkova:
- Top 10: {predictions[0]}
- Top 3: {predictions[1]}
- 1. mesto: {predictions[2]}")
