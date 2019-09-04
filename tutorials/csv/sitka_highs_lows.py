import csv
import matplotlib.pyplot as pit

from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

pit.style.use('seaborn')
fig, ax = pit.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
pit.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

pit.title("Daily high and low temperatures, 2018", fontsize=24)
pit.xlabel('', fontsize=16)
fig.autofmt_xdate()
pit.ylabel("Temperature (F)", fontsize=16)
pit.tick_params(axis='both', which='major', labelsize=16)

pit.show()
