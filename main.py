import pandas as pd

data = pd.read_csv('dataset.csv')

# print(data)
clean_data = data.dropna()
clean_data = clean_data.drop_duplicates()

# print(clean_data)
print(type(clean_data), len(clean_data), type(clean_data.items()))
# clean_data = pd.to_datetime(clean_data['Date'], format='mixed', errors='coerce')
for record in clean_data.items():
    print(record)
    # record['Date'] = pd.to_datetime(clean_data['Date'], format='mixed', errors='coerce')
# print(type(clean_data))
# print(clean_data)
