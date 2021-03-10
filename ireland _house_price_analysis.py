# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

import pandas as pd
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',100)
pd.set_option('display.width',1000)

# import CSV flat data into a dataframe
ireland_house_price = pd.read_csv("PPR-ALL.csv",index_col=0)
# Display header of first 5.
print(ireland_house_price.head(20))

print(ireland_house_price.describe())

