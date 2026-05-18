import pandas as pd
from rule_based_method import get_clean_name, pick_longest_name

df = pd.read_parquet("data/project_a_samples.parquet")
print("\nRule-Based Predictions:")
grouped = df.groupby("base_id")
count = 0
for base_id, group in grouped:
    names = []
    for _, row in group.iterrows():
        clean_name = get_clean_name(row["names"])
        if clean_name:
            names.append(clean_name)
    best_name = pick_longest_name(names)

    print(f"\nBase ID: {base_id}")
    print("Names:", names)
    print("Predicted Best:", best_name)

    count += 1
    if count == 5:
        break