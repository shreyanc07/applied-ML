import unittest
import pickle
import pandas as pd
import random
import numpy as np
import requests
import subprocess
import time
from score import *

class TestScoreFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the trained model for testing
        with open(r"C:\CMI\Applied ML\applied-ML\ASS_4\src\lightgbm_best_model.pkl", 'rb') as model_file:
            cls.loaded_model = pickle.load(model_file)
        
        # Load input texts from the CSV file
        cls.test_df = pd.read_csv(r"C:\CMI\Applied ML\applied-ML\ASS_4\data\test.csv")

    def test_smoke_test(self):
        # Smoke test: Check if the function runs without crashing
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        result = score(text, self.loaded_model, 0.5)
        self.assertIsNotNone(result)

    def test_format_test(self):
        # Format test: Check if the output formats/types are as expected
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        prediction, propensity = score(text, self.loaded_model, 0.5)
        self.assertIsInstance(prediction, (bool, np.bool_))
        self.assertIsInstance(propensity, float)

    def test_prediction_values(self):
        # Check if prediction values are 0 or 1
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        prediction, _ = score(text, self.loaded_model, 0.5)
        self.assertIn(prediction, [True, False])

    def test_propensity_range(self):
        # Check if propensity score is between 0 and 1
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        _, propensity = score(text, self.loaded_model, 0.5)
        self.assertTrue(0 <= propensity <= 1)

    def test_threshold_zero(self):
        # Test if setting the threshold to 0 always produces prediction as True
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        prediction, _ = score(text, self.loaded_model, 0.0)
        self.assertTrue(prediction)

    def test_threshold_one(self):
        # Test if setting the threshold to 1 always produces prediction as False
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        prediction, _ = score(text, self.loaded_model, 1.0)
        self.assertFalse(prediction)

    def test_obvious_spam_input(self):
        # Test if an obvious spam input text results in prediction as True
        text = self.test_df.iat[2, 0]
        prediction, _ = score(text, self.loaded_model, 0.5)
        self.assertTrue(prediction)

    def test_obvious_non_spam_input(self):
        # Test if an obvious non-spam input text results in prediction as False
        text = self.test_df.iat[3, 0]
       # print(f"{text}")
        prediction, _ = score(text, self.loaded_model, 0.5)
        self.assertFalse(prediction)


# INTEGRATION TEST
class TestFlaskIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Launch Flask app using command line
        cls.flask_process = subprocess.Popen(['python', 'app.py']) 
        time.sleep(10)  # Give some time for the server to start
        # Load input texts from the CSV file
        cls.test_df = pd.read_csv(r"C:\CMI\Applied ML\applied-ML\ASS_4\data\test.csv")      
        


    def test_flask(self):
        # Test the response from the localhost endpoint
        #data = {'text': 'There is a meeting tomorrow. Please be there.'}
        r = random.randint(0, len(self.test_df) - 1)
        text = self.test_df.iat[r, 0]
        data = {'text': text}
        response = requests.post('http://127.0.0.1:5000/score', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json())
        self.assertIn('propensity', response.json())
        
    @classmethod
    def tearDownClass(cls):
        # Close Flask app using command line
        cls.flask_process.terminate()

class TestDocker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Build the Docker image
        subprocess.run(["docker", "build", "-t", "assignment_4", "."], check=True)
        # Run the Docker container
        cls.container_id = subprocess.check_output(
            ["docker", "run", "-d", "-p", "5000:5000", "assignment_4"]
        ).decode("utf-8").strip()
        time.sleep(5)  # Wait for the server to start

    def test_docker(self):
        # Test the /score endpoint
        test_data = {'text': 'sample text'}
        response = requests.post('http://127.0.0.1:5000/score', json=test_data)
        self.assertEqual(response.status_code, 200)
        # You may want to add more assertions here based on your expected response

    @classmethod
    def tearDownClass(cls):
        # Stop and remove the Docker container
        subprocess.run(["docker", "stop", cls.container_id], check=True)
        subprocess.run(["docker", "rm", cls.container_id], check=True)        
if __name__ == '__main__':
    unittest.main()