import matplotlib.pyplot as pit

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

pit.style.use('seaborn')
fig, ax = pit.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

## Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

pit.show()