import matplotlib.pyplot as plt
# pyplot contains a number of functions that help generate charts and plots.

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# The plot() function will try to plot the numbers in a meaningful way.
# The linewidth parameter controls the thickness of the lne that plot() generates.
# The plot() function assumes the first data point corresponds to an x-coordinate value of 0.
# By giving plot() both the input and output values used to calculate the squares.
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
# The title() function sets a title for the chart.
# The fontsize parameters control the size of the text on the chart.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
# The tick_params function styles the tick marks.
# The arguments shown here affect the tick marks on both the x- and y-axes (axes='both')
# and set the font size of the tick mark labels to 14 (labelsize=14).
plt.tick_params(axis='both', labelsize=14)

# The show() function opens matplotlib's viewer and displays the plot.
plt.show()

