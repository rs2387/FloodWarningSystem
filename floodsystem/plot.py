import matplotlib.pyplot as plt
import matplotlib
from .analysis import polyfit

# Task 2F, plotting the least squares fit 
def plot_water_level_with_fit(station, dates, levels, p):

    x, y = matplotlib.dates.date2num(dates), levels
      
    poly, xat0 = polyfit(dates, levels, p)

    plt.plot(x, y, '.')
    plt.plot(dates, poly(x - xat0))
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.plot(xat0, poly)

    plt.show()

# Task 2E, plotting water level against time including typical low and high levels
def plot_water_levels(station, dates, levels):

    x, y = matplotlib.dates.date2num(dates), levels


    plt.plot(x,y, ".", color="b")
    plt.axhline(station.typical_range[0], color="green", label="Typical low")
    plt.axhline(station.typical_range[1], color="red", label="Typical high")
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()

    plt.show()