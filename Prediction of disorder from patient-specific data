import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# -----------------------------
# 1. Create synthetic dataset
# -----------------------------
data = {
    "age": [25, 60, 45, 50, 30, 65, 55, 40],
    "heart_rate": [70, 85, 78, 90, 72, 95, 88, 75],
    "blood_pressure": [120, 150, 135, 145, 125, 160, 155, 130],
    "glucose": [90, 180, 140, 160, 95, 200, 170, 110],
    "BMI": [22, 30, 27, 29, 23, 32, 31, 25],
    "disease": ["Healthy", "Diabetes", "Cardio", "Cardio",
                "Healthy", "Diabetes", "Cardio", "Healthy"]
}

df = pd.DataFrame(data)


# -----------------------------
# 2. Split features and labels
# -----------------------------
X = df.drop("disease", axis=1)
y = df["disease"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


# -----------------------------
# 3. Scale features
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# -----------------------------
# 4. Train ML model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_scaled, y_train)


# -----------------------------
# 5. Evaluate model
# -----------------------------
y_pred = model.predict(X_test_scaled)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# -----------------------------
# 6. Predict disease for new patient
# -----------------------------
# Example patient: [age, heart_rate, blood_pressure, glucose, BMI]
new_patient = np.array([[52, 92, 148, 165, 29]])

new_patient_scaled = scaler.transform(new_patient)
prediction = model.predict(new_patient_scaled)

print("Predicted disease for new patient:", prediction[0])
