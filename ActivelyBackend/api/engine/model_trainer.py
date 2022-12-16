import random
from typing import Dict, List
from .database import Fake_Database


import pandas as pd
from sklearn import ensemble, linear_model, neural_network

MODEL_TYPES = [
    linear_model.LogisticRegression,
    neural_network.MLPClassifier,
    ensemble.RandomForestClassifier,
]

def train_and_store_model(
    dataset: pd.DataFrame,
    output: str,
    inputs: List[str],
    database_instance: Fake_Database
) -> float:  # probability of output being `True` for hypothetical input

    print(dataset)
    
    assert dataset[output].dtype in (bool,)
    assert all(dataset[input].dtype in (float, int) for input in inputs)

    X = dataset[inputs]
    y = dataset[output]

    model = random.choice(MODEL_TYPES)()
    model.fit(X, y)

    model_id = database_instance.store_model(model)
    

    return model_id

def make_prediction(
    input: List[str],
    modelID: int,
    database_instance: Fake_Database
) -> float:  # probability of output being `True` for hypothetical input

    print(input)
    model = database_instance.get_model(modelID)

    return model.predict_proba(input)[0][1]