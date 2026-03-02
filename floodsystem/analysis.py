import numpy as np
import matplotlib


# Task 2F fitting polynomial to water level data
def polyfit(dates, levels, p):

    # Create list of dates numbers and list of water levels
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    xat0 = x[0]

    # Makes graph start at 0
    p_coeff = np.polyfit(x-xat0, y, p)

    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)



    return poly, xat0
