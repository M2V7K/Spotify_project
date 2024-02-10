import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

print(tips)

print("\n")

print(tips.columns)

print("\n")

print(tips.info())

print("\n")

print(tips.head(10))

print("\n")

print(tips.describe())

print("\n")

print(tips.shape)

print("\n")

sns.displot(tips["total_bill"])
plt.show()