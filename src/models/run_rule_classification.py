# purpose: advanced rule-based classification with normalization + fuzzy matching

import pandas as pd
import json
import re
from rapidfuzz import fuzz
from rule_based_method import get_clean_name

def normalize(name):
    name = name.lower()
    name = name.replace("&", "and")
    name = re.sub(r"[^\w\s]", "", name)  
    name = re.sub(r"\s+", " ", name).strip()
    return name


df = pd.read_parquet("data/project_a_samples.parquet")

with open("data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

print("\nFinal Rule-Based Classification:")

correct = 0
total = 0

for i in range(len(golden_data)):
    label = golden_data[i]['labels']['name']

    if label == "base":
        continue

    row = df.iloc[i]
    raw_name = get_clean_name(row['names'])

    if not raw_name:
        continue

    name = normalize(raw_name)

    word_count = len(name.split())
    length = len(name)

    short_name = name.split()[0]

    similarity_score = fuzz.ratio(short_name, name)

    if (
        similarity_score > 85 and word_count >= 2  
        or short_name in name                       
        or (word_count >= 2 and length > 10)        
    ):
        prediction = "same"
    else:
        prediction = "current"

    if prediction == label:
        correct += 1

    total += 1

print("Accuracy:", correct / total)