"""FCC Neural Network SMS Text Classifier.

predict_message(s) -> [probability_spam, "ham"/"spam"].
"""
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

train_df = pd.read_csv("train-data.tsv", sep="\t", header=None, names=["label", "text"])
test_df = pd.read_csv("valid-data.tsv", sep="\t", header=None, names=["label", "text"])

VOCAB = 1000
MAXLEN = 50
EMBED = 16

tok = Tokenizer(num_words=VOCAB, oov_token="<OOV>")
tok.fit_on_texts(train_df["text"])
X_train = pad_sequences(tok.texts_to_sequences(train_df["text"]), maxlen=MAXLEN, padding="post", truncating="post")
X_test = pad_sequences(tok.texts_to_sequences(test_df["text"]), maxlen=MAXLEN, padding="post", truncating="post")
y_train = (train_df["label"] == "spam").astype("int32").values
y_test = (test_df["label"] == "spam").astype("int32").values

model = tf.keras.Sequential([
    layers.Embedding(VOCAB, EMBED, input_length=MAXLEN),
    layers.GlobalAveragePooling1D(),
    layers.Dense(24, activation="relu"),
    layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), verbose=2)


def predict_message(pred_text):
    seq = pad_sequences(tok.texts_to_sequences([pred_text]), maxlen=MAXLEN, padding="post", truncating="post")
    p = float(model.predict(seq, verbose=0).flatten()[0])
    return [p, "spam" if p > 0.5 else "ham"]
