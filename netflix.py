import pandas as pd
netflix_data=pd.read_csv("netflix_titles.csv")
print(netflix_data.shape)
#missing_val = netflix_data.isnull().sum()
#print(missing_val)
#new_data= netflix_data.dropna(subset=["rating","data])
#new_data= netflix_data.dropna(subset=["rating"])

#(axis=1) row (axis=0) column
#print(new_data.shape)
new_data= netflix_data.drop_duplicates(subset=["director", "rating","duration"])
print(new_data.shape)