# Machine Learning Model Scoring Service

This project provides a service for scoring text inputs using a trained machine learning model to predict whether the input text is spam or not. The scoring is based on a pre-defined threshold, and the service returns both the binary prediction (spam or not) and the propensity score indicating the likelihood of the text being spam. The project includes a Python scoring function, unit tests, a Flask API endpoint for scoring texts via HTTP POST requests, and integration tests for the Flask application.

## Overview

- `score.py` contains the main logic for scoring text inputs with a trained sklearn model.
- `test.py` includes both unit and integration tests for the scoring function and Flask application.
- `app.py` is a Flask application that provides an HTTP endpoint for scoring text inputs.
- `train.ipynb` is a Jupyter notebook used for training the model. The best model from the experiments is saved in joblib/pkl format for use in scoring.
- `coverage.txt` provides the coverage report output of the unit and integration tests.

## Features

- **Scoring Function**: Takes a text input, a trained model, and a threshold to return a binary prediction and propensity score.
- **Unit Tests**: Tests the scoring function for reliability, accuracy, and edge cases.
- **Flask Endpoint**: A REST API endpoint for scoring texts via POST requests.
- **Integration Tests**: Ensures the Flask application behaves as expected when launched and accessed through HTTP.
- **Coverage Report**: A coverage report for the unit and integration tests, ensuring thorough testing of the codebase.

## Setup

To run this project, ensure you have Python 3.6+ and Flask installed. You can install the necessary dependencies using:

```bash
pip install -r requirements.txt
```
