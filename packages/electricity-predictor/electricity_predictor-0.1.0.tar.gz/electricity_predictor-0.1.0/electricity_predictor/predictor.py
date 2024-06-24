import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

class ElectricityPredictor:
    def __init__(self):
        #self.model = IsolationForest(contamination=0.1)  # Set contamination to 10%
        self.model = pickle.load(open("pima.pickle.new.dat", "rb"))

    def fit(self, data):
        self.model.fit(data)

    def predict(self, data):
        prediction = self.model.predict(data)
        predictions = [round(value) for value in prediction]
        # Convert predictions to "normal" and "abnormal"
        return ["normal" if pred == 1 else "abnormal" for pred in predictions]

def read_csv(file_path):
    return pd.read_csv(file_path)
