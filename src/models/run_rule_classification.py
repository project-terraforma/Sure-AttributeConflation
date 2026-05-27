# purpose: advanced rule-based classification with normalization + fuzzy matching

import pandas as pd
import json
import re
from rapidfuzz import fuzz
from rule_based_method import get_clean_name

# ----------------------------
# Normalization function
# ----------------------------
def normalize(name):
    name = name.lower()
    name = name.replace("&", "and")
    name = re.sub(r"[^\w\s]", "", name)   # remove punctuation
    name = re.sub(r"\s+", " ", name).strip()
    return name

# ----------------------------
# Load datasets
# ----------------------------
df = pd.read_parquet("data/project_a_samples.parquet")

with open("data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

print("\nFinal Rule-Based Classification:")

correct = 0
total = 0

# ----------------------------
# Main loop
# ----------------------------
for i in range(len(golden_data)):
    label = golden_data[i]['labels']['name']

    if label == "base":
        continue

    row = df.iloc[i]
    raw_name = get_clean_name(row['names'])

    if not raw_name:
        continue

    # Normalize
    name = normalize(raw_name)

    # Features
    word_count = len(name.split())
    length = len(name)

    # Subset rule
    short_name = name.split()[0]

    # Fuzzy similarity
    similarity_score = fuzz.ratio(short_name, name)

    # ----------------------------
    # FINAL RULE LOGIC
    # ----------------------------
    if (
        similarity_score > 85 and word_count >= 2   # fuzzy match
        or short_name in name                       # subset match
        or (word_count >= 2 and length > 10)        # structure rule
    ):
        prediction = "same"
    else:
        prediction = "current"

    # Accuracy tracking
    if prediction == label:
        correct += 1

    total += 1

# ----------------------------
# Final result
# ----------------------------
print("Accuracy:", correct / total)