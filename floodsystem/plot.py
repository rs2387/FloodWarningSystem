import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from analysis import polyfit



def plot_water_level_with_fit(station, dates, levels, p):

    x, y = matplotlib.dates.date2num(dates), levels
      
    poly, xat0 = polyfit(dates, levels, p)

    plt.plot(x, y, '.')
    plt.plot(dates, poly(x - xat0))
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.xticks(rotation=45)
    plt.title(station.name)



    plt.plot(xat0, poly)

    # Display plot
    plt.show()
