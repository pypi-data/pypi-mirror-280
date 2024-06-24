import unittest
import pandas as pd
from electricity_predictor import ElectricityPredictor, read_csv

class TestElectricityPredictor(unittest.TestCase):

    def test_read_csv(self):
        data = read_csv('test_data.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_predictor(self):
        data = pd.DataFrame({'consumption': [100, 200, 300, 400, 500]})
        predictor = ElectricityPredictor()
        predictor.fit(data)
        predictions = predictor.predict(data)
        self.assertEqual(len(predictions), 5)

if __name__ == '__main__':
    unittest.main()
