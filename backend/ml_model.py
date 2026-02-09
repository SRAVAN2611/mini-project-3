import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import os

class PropulsionPredictor:
    def __init__(self):
        self.model = None
        self.dataset_path = os.path.join(os.getcwd(), '..', 'datasets', 'propulsion.csv')
        self._train_model()

    def _train_model(self):
        try:
            if not os.path.exists(self.dataset_path):
                print(f"Dataset not found at {self.dataset_path}")
                return

            df = pd.read_csv(self.dataset_path)
            # Simple preprocessing
            # Convert categorical 'fuel_type' to numeric
            df['fuel_type_code'] = df['fuel_type'].astype('category').cat.codes
            
            X = df[['fuel_type_code', 'thrust_output', 'heat_dissipation']]
            y = df['efficiency_rating']
            
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X, y)
            print("Model trained successfully.")
            
        except Exception as e:
            print(f"Error training model: {e}")

    def predict(self, fuel_type_code, thrust, heat):
        if not self.model:
            return 0.0
        
        try:
            # simple mock prediction logic if fuel_type_code is string, handle it
            # For simplicity, we assume valid inputs or random generation in tasks
            prediction = self.model.predict([[fuel_type_code, thrust, heat]])
            return float(prediction[0])
        except Exception as e:
            print(f"Prediction error: {e}")
            return 0.0
