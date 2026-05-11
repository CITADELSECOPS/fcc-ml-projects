"""FCC Linear Regression Health Costs Calculator.

Target: Mean Absolute Error < 3500 USD on test data.
"""
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

dataset = pd.read_csv("insurance.csv")
# Encode categorical
dataset = pd.get_dummies(dataset, columns=["sex", "smoker", "region"], drop_first=True)
# Cast boolean dummies to int
dataset = dataset.astype({c: "int64" for c in dataset.columns if dataset[c].dtype == bool})

# Split 80/20
train = dataset.sample(frac=0.8, random_state=42)
test = dataset.drop(train.index)
train_labels = train.pop("expenses")
test_labels = test.pop("expenses")

# Normalize using training stats
normalizer = layers.Normalization(axis=-1)
normalizer.adapt(np.array(train))

model = keras.Sequential([
    normalizer,
    layers.Dense(64, activation="relu"),
    layers.Dense(64, activation="relu"),
    layers.Dense(1),
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.05),
    loss="mae",
    metrics=["mae", "mse"],
)
model.fit(train, train_labels, epochs=100, validation_split=0.2, verbose=0)
loss, mae, mse = model.evaluate(test, test_labels, verbose=2)
print(f"Test MAE = {mae:.2f}")
assert mae < 3500, f"MAE {mae} > 3500 — needs more tuning"
