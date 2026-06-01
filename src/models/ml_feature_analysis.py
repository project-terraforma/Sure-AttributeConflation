import pandas as pd
import json
from rule_based_method import get_clean_name

df = pd.read_parquet("../data/project_a_samples.parquet")

with open("../data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

same_exact = 0
same_total = 0

for i in range(len(golden_data)):

    label = golden_data[i]["labels"]["name"]

    current = get_clean_name(df.iloc[i]["names"])
    base = get_clean_name(df.iloc[i]["base_names"])

    if label == "same":
        same_total += 1

        if current == base:
            same_exact += 1

print("Same labels:", same_total)
print("Exact matches:", same_exact)
print("Percent:", same_exact / same_total)
