import pandas as pd

df = pd.read_parquet("data/project_a_samples.parquet")

#print(df.head())
#print(df.columns)
print(df[['names', 'phones', 'websites']].head())
