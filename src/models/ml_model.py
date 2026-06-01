import pandas as pd
import json
import numpy as np

from rapidfuzz import fuzz
from rule_based_method import get_clean_name

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from scipy.sparse import hstack

df = pd.read_parquet("../data/project_a_samples.parquet")

with open("../data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

names = []
labels = []
extra_features = []

label_map = {
"same": 0,
"current": 1,
"base": 2
}

for i in range(len(golden_data)):

    label = golden_data[i]["labels"]["name"]

    current = get_clean_name(df.iloc[i]["names"])
    base = get_clean_name(df.iloc[i]["base_names"])

    if not current or not base:
        continue

    names.append(current + " " + base)

    labels.append(label_map[label])

    exact_match = 1 if current == base else 0

    similarity = fuzz.ratio(current, base)

    current_len = len(current)
    base_len = len(base)

    current_words = len(current.split())
    base_words = len(base.split())

    length_diff = current_len - base_len
    word_diff = current_words - base_words

    extra_features.append([
        exact_match,
        similarity,
        current_len,
        base_len,
        length_diff,
        word_diff
])
X_train, X_test, y_train, y_test, f_train, f_test = train_test_split(
names,
labels,
extra_features,
test_size=0.2,
random_state=42,
stratify=labels
)

vectorizer = TfidfVectorizer(max_features=3000)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

f_train = np.array(f_train)
f_test = np.array(f_test)

X_train_final = hstack([X_train_vec, f_train])
X_test_final = hstack([X_test_vec, f_test])

model = RandomForestClassifier(
n_estimators=200,
random_state=42
)

model.fit(X_train_final, y_train)

preds = model.predict(X_test_final)

accuracy = accuracy_score(y_test, preds)

print("ML Model Accuracy:", accuracy)
