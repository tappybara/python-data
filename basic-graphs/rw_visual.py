import matplotlib.pyplot as pit

from random_walk import RandomWalk

# Make a random walk
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot points
    pit.style.use('classic')
    fig, ax = pit.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=pit.cm.Blues, edgecolors='none', s=1)
    
    # Emphasize starting and ending pointsn
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    pit.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
