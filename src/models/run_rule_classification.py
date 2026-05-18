#purpose: if name long --> predict SAME (usually correct)
# if name short --> predict CURRENT (usually incomplete)

import pandas as pd
import json
from rule_based_method import get_clean_name

df = pd.read_parquet("data/project_a_samples.parquet")

with open("data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

print("\nRule-Based Classification:")
correct = 0
total = 0

for i in range(len(golden_data)):
    label = golden_data[i]['labels']['name']

    if label == "base":
        continue
    row = df.iloc[i]
    name = get_clean_name(row['names'])

    if len(name) > 15:
        prediction = "same"
    else:
        prediction = "current"

    if prediction == label:
        correct += 1

    total += 1
print("Accuracy:", correct/total)