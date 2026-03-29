import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Note: Using underscores to match your dashboard's naming convention
teams = ["Boston_Bruins", "Buffalo_Sabres", "New_Jersey_Devils", "NY_Islanders", "NY_Rangers"]
data = []

# Generate 15 points per team to make the curves look smooth
for i in range(15, 0, -1):
    timestamp = (datetime.now() - timedelta(hours=i*4)).strftime("%Y-%m-%d %H:%M")
    
    for team in teams:
        val = 40 # Starting base
        
        # --- NON-LINEAR PERSONALITIES ---
        if team == "Buffalo_Sabres": 
            val += (np.sin(i * 0.5) * 8) + 10 # 🌊 Wavy Sine Curve
        elif team == "NY_Islanders": 
            val += (1.5 ** (15-i)) / 10 # 🚀 Exponential Growth
        elif team == "New_Jersey_Devils":
            # ⚡ A sudden market spike at point 7, otherwise flat
            val += 20 if i == 7 else 5 
        elif team == "Boston_Bruins":
            val += (i * 0.8) + np.random.normal(0, 2) # 📉 Growth with "Noise"
        else: # NY_Rangers
            val += 12 # Perfectly flat line for comparison
            
        data.append({
            "Timestamp": timestamp,
            "Metric_Name": f"Wins_{team}",
            "Value": round(float(val), 2),
            "Execution_Status": "Success"
        })

df = pd.DataFrame(data)
df.to_csv("warehouse_data.csv", index=False)
print("📈 Volatility Engine complete: Complex data patterns generated!")