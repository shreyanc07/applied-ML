import sklearn
import numpy as np
import pandas as pd
import pickle
from typing import Tuple
import numpy as np
from sklearn.pipeline import Pipeline

with open(r"C:\Users\rickc\OneDrive\Desktop\AML_Assignment3\lightgbm_best_model.pkl", 'rb') as file:
    best_model = pickle.load(file)



def score(text:str, model:Pipeline, threshold=0.5) -> Tuple[bool , float]:
   
    """
    Score the provided text using the given model and threshold.

    Parameters:
    text (str): The text to be scored.
    model (model object): A trained model with predict_proba method.
    threshold (float): The threshold for classifying the prediction as True/False.

    Returns:
    Tuple[bool, float]: The predicted class (True/False) and the propensity score.
    """
    # Vectorize the text
    vect_text = model.named_steps['tfidf'].transform([text])
    
    # Get the propensity score for the positive class
    propensity = model.named_steps['clf'].predict_proba(vect_text)[:, 1][0]
    prediction = (propensity >= threshold)
    
    return bool(prediction), propensity

