import pandas as pd
import json

from rule_based_method import (
    get_clean_name,
    predict_label
)

# Load datasets
df = pd.read_parquet("../data/project_a_samples.parquet")

with open("../data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

correct = 0
total = 0

for i in range(len(golden_data)):

    current = get_clean_name(df.iloc[i]["names"])
    base = get_clean_name(df.iloc[i]["base_names"])

    prediction = predict_label(current, base)

    actual = golden_data[i]["labels"]["name"]

    if prediction == actual:
        correct += 1

    total += 1

accuracy = correct / total

print("\nRule-Based Model Results")
print("------------------------")
print("Correct:", correct)
print("Total:", total)
print("Accuracy:", round(accuracy, 4))