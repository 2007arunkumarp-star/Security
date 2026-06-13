import pandas as pd
from sklearn.ensemble import IsolationForest
from datetime import datetime

# Sample security data
data = {
    "user": ["Admin", "User1", "User2", "Unknown", "Admin"],
    "login_attempts": [2, 1, 3, 15, 2],
    "failed_attempts": [0, 0, 1, 12, 0],
    "time": [9, 10, 14, 2, 11]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features for AI model
features = df[["login_attempts", "failed_attempts", "time"]]

# Train AI anomaly detection model
model = IsolationForest(contamination=0.2, random_state=42)
model.fit(features)

# Predict suspicious activity
df["status"] = model.predict(features)

# Convert prediction values
df["status"] = df["status"].map({1: "Normal", -1: "Suspicious"})

# Alert system
def generate_alert(user, status):
    if status == "Suspicious":
        print("🚨 SECURITY ALERT 🚨")
        print(f"User: {user}")
        print("Threat Detected: Unusual Login Activity")
        print("Action: Verify user and block access if necessary")
        print("Time:", datetime.now())
        print("--------------------------")

# Scan all activities
print("\n--- Security AI Agent Report ---")
for index, row in df.iterrows():
    print(f"{row['user']} : {row['status']}")
    generate_alert(row["user"], row["status"])
