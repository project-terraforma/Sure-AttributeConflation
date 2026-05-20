import json
import matplotlib.pyplot as plt
from collections import Counter

with open("data/golden_dataset_sample.json") as f:
    data = json.load(f)

labels = [item['labels']['name'] for item in data]
counts = Counter(labels)

plt.figure()
plt.bar(counts.keys(), counts.values())
plt.title("Label Distribution")
plt.xlabel("Label")
plt.ylabel("Count")

plt.show()

methods = ["Rule-Based"]
accuracy = [0.41]

plt.figure()
plt.bar(methods, accuracy)
plt.title("Model Accuracy")
plt.ylabel("Accuracy")

plt.ylim(0, 1)

plt.show()