import numpy as np
import matplotlib


# Task 2F fitting polynomial to water level data
def polyfit(dates, levels, p):

    # Create list of dates numbers and list of water levels
    x = matplotlib.dates.date2num(dates)

    

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], levels, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # returns the polynomial and whatever it was shifted by
    return poly, x[0]
