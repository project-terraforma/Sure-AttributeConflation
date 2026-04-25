import pandas as pd
import json


df = pd.read_parquet("data/project_a_samples.parquet")

print("RAW DATA SAMPLE:")
print(df[['names', 'phones', 'websites']].head())


with open("data/golden_dataset_sample.json") as f:
    golden_data = json.load(f)

print("\nGOLDEN DATA SIZE:")
print(len(golden_data))

print("\nFIRST 5 GOLDEN RECORDS:")
for i in range(5):
    print(golden_data[i])

print("\nLABELS ONLY:")
for i in range(5):
    print(golden_data[i]['labels'])

def get_primary_name(name_str):
    try:
        name_dict = json.loads(name_str)  # convert string → dict
        return name_dict.get("primary", "")
    except:
        return ""
    
print("\nCLEAN NAMES:")
for i in range(5):
    name = df.iloc[i]['names']
    print(get_primary_name(name))