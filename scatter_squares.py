import matplotlib.pyplot as pit

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

pit.style.use('seaborn')
fig, ax = pit.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axies.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=24)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=24)

ax.axis([0, 1100, 0, 1100000])

pit.show()