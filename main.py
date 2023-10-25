import pandas as pd

data = pd.read_csv('dataset.csv')

# print(data)
clean_data = data.dropna()
clean_data = clean_data.drop_duplicates()
# clean_data = pd.to_datetime(clean_data['Date'])

print(clean_data)
