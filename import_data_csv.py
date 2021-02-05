
# Import matplotlib.pyplot as plt
# importing pandas module
import pandas as pd
import matplotlib.pyplot as plt
import csv
import numpy as np
# making data frame
#data = pd.read_csv("Ireland_property.csv", index_col=1)
df = pd.read_csv("world_population.csv")
# Preview the first 10 lines of the loaded data
print(df.head(10))
#Set chart face background colour
ax = plt.gca()
ax.set_facecolor('xkcd:lightgreen')

# Make a line plot: year on the x-axis, pop on the y-axis
#Add marker and colour

#Plot x,y(Year, population)
plt.plot(df['year'],df['pop'],marker = 'o',color = 'darkblue')
# Display Title, set font size
plt.title('World Population Chart',fontsize=25)
# Display X and Y label
plt.xlabel('Year', fontsize=12) , plt.ylabel('Population\n (B)',fontsize=12)
# Display the plot with plt.show()
plt.show()