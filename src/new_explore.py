import pandas as pd
import json
from models.rule_based_method import get_clean_name

df = pd.read_parquet("../data/project_a_samples.parquet")

with open("../data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

same_count = 0
current_count = 0
base_count = 0

for item in golden_data:
    label = item["labels"]["name"]

    if label == "same":
        same_count += 1
    elif label == "current":
        current_count += 1
    elif label == "base":
        base_count += 1

print("same:", same_count)
print("current:", current_count)
print("base:", base_count)