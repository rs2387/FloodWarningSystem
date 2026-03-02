import matplotlib.pyplot as plt
import matplotlib
from .analysis import polyfit

# Task 2F, plotting the least squares fit 
def plot_water_level_with_fit(station, dates, levels, p):

    # normal dates and levels
    x, y = matplotlib.dates.date2num(dates), levels
    
    # polynomial and the x axis shift is given 
    poly, x0 = polyfit(dates, y, p)

    # plot normal water level data 
    plt.plot(x, y, '.')

    # adjusting aesthetics
    plt.xlabel("date")
    plt.ylabel("water level")
    plt.xticks(rotation=45)
    plt.title(station.name)

    # also plot the polynomial making sure to shift to start at 0
    plt.plot(x, poly(x-x0))

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