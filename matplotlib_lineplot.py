# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
pop = [2.519,3.692, 5.263,6.972]
# Print the last item from year and pop
print(year[-1])
print(pop[-1])

#Set chart face background colour
ax = plt.gca()
ax.set_facecolor('xkcd:lightgreen')

# Make a line plot: year on the x-axis, pop on the y-axis
#Add marker and colour
plt.plot(year,pop,marker = 'o',color = 'darkblue')
# Display Title, set font size
plt.title('World Population Chart',fontsize=25)
# Display X and Y label
plt.xlabel('Year', fontsize=16) , plt.ylabel('Population\n (B)',fontsize=16)
# Display the plot with plt.show()
plt.show()
