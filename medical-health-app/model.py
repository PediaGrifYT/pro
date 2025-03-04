import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("symptoms_dataset.csv")  # Ensure this dataset is available

# Encode categorical values
le = LabelEncoder()
df['Disease'] = le.fit_transform(df['Disease'])

# Prepare training data
X = df.drop(columns=['Disease'])
y = df['Disease']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model and encoder
with open("health_model.pkl", "wb") as file:
    pickle.dump(model, file)

with open("label_encoder.pkl", "wb") as file:
    pickle.dump(le, file)

print("Model trained and saved successfully!")
