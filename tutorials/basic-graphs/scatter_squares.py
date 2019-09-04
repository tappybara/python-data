import matplotlib.pyplot as pit

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

pit.style.use('seaborn')
fig, ax = pit.subplots()

# Colour map the y values based on value
ax.scatter(x_values, y_values, c=y_values, cmap=pit.cm.Blues, s=100)

# Set chart title and label axies.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=24)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=24)

ax.axis([0, 1100, 0, 1100000])

# Save figure as an image
pit.savefig('squares_plot.png', bbox_inches='tight')

pit.show()

