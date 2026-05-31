import pandas as pd
import json
from models.rule_based_method import get_clean_name

df = pd.read_parquet("../data/project_a_samples.parquet")

with open("../data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

correct = 0

same_correct = 0
same_total = 0

base_correct = 0
base_total = 0

current_correct = 0
current_total = 0

for i in range(len(golden_data)):

    current = get_clean_name(df.iloc[i]["names"])
    base = get_clean_name(df.iloc[i]["base_names"])

    if current == base:
        prediction = "same"
    elif len(base) > len(current):
        prediction = "base"
    else:
        prediction = "current"

    actual = golden_data[i]["labels"]["name"]

    if actual == "same":
        same_total += 1
        if prediction == actual:
            same_correct += 1

    elif actual == "base":
        base_total += 1
        if prediction == actual:
            base_correct += 1

    elif actual == "current":
        current_total += 1
        if prediction == actual:
            current_correct += 1

    if prediction == actual:
        correct += 1

print("Overall:", correct / len(golden_data))
print("Same:", same_correct, "/", same_total)
print("Base:", base_correct, "/", base_total)
print("Current:", current_correct, "/", current_total)