import pandas as pd
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',100)
pd.set_option('display.width',1000)

canadian_youtube = pd.read_csv("CAvideos.csv").rese
british_youtube = pd.read_csv("GBvideos.csv")
print(canadian_youtube.head(5))

join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')

# concat_data= pd.concat([canadian_youtube, british_youtube],axis=1) #columns
# print(concat_data.shape)
# left = canadian_youtube.set_index(['title', 'trending_date'])
# right = british_youtube.set_index(['title', 'trending_date'])
# join_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')
# print(join_data.head(5))
