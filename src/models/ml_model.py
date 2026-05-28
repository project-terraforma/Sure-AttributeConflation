import pandas as pd
import json
from rule_based_method import get_clean_name
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load data
df = pd.read_parquet("data/project_a_samples.parquet")

with open("data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

names = []
labels = []
extra_features = []

for i in range(len(golden_data)):
    label = golden_data[i]['labels']['name']

    if label == "base":
        continue

    name = get_clean_name(df.iloc[i]['names'])

    if not name:
        continue

    names.append(name)
    labels.append(1 if label == "same" else 0)

    word_count = len(name.split())
    length = len(name)
    is_short = 1 if (word_count == 1 and length < 6) else 0

    extra_features.append([word_count, length, is_short])

X_train, X_test, y_train, y_test, f_train, f_test = train_test_split(
    names, labels, extra_features, test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer(max_features=3000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

f_train = np.array(f_train)
f_test = np.array(f_test)

from scipy.sparse import hstack
X_train_final = hstack([X_train_vec, f_train])
X_test_final = hstack([X_test_vec, f_test])

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_final, y_train)

preds = model.predict(X_test_final)

accuracy = accuracy_score(y_test, preds)

print("High-Performance ML Accuracy:", accuracy)