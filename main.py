import pandas as pd

data = pd.read_csv('dataset.csv')

# print(data)
clean_data = data.dropna()

print(clean_data)
