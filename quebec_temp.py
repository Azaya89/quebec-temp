import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_temp_data(filename, dates, highs, lows, avgs):
    """Get temperature data from weather files."""
    with open(filename) as f:
        data = csv.reader(f)
        header = next(data)

        date_index = header.index("DATE")
        high_index = header.index("TMAX")
        low_index = header.index("TMIN")
        name_index = header.index("NAME")
        avg_index = header.index("TAVG")
        place_name = ""

        # Get dates, and high and low temperature values from the file.
        for row in data:
            if not place_name:
                place_name = row[name_index]
            # Convert date to datetime object
            current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            try:
                high = int(row[high_index])
                low = int(row[low_index])
                avg = int(row[avg_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
                avgs.append(avg)
    return place_name


# Get data from a weather file
file = "quebec.csv"
dates, highs, lows, avgs = [], [], [], []
get_temp_data(file, dates, highs, lows, avgs)

highest_temp = sorted(highs)
highest_temp = highest_temp[-1]
lowest_temp = sorted(lows)
lowest_temp = lowest_temp[0]

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))
plt.title("Average temperature in Quebec, Canada in 2021", fontsize=20)
fig.autofmt_xdate()
plt.xlabel("")
plt.ylabel("Temperature(F)", fontsize=20)
ax.plot(dates, avgs)
## Plot the high and low temperatures optionally.
# ax.plot(dates, highs, c="red")
# ax.plot(dates, lows, c="blue")
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


plt.show()
