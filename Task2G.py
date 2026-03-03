# factors involved with flood risk: current level, typical levels, recent levels, height of susceptible infrastructure

# Task 2A gives the current level.

# Task 2B gives the current level's ratio to the typical high.

# Task 2C gives the current level - typical level.

# Task 2D gives the level of a station over the previous 10 days.

# Task 2E gives a plot of the levels over time and the typical level for a station

# Task 2F gives lines of best fit for the past two days.

# The level's ratio to the current level is more significant than the absolute difference, but a large absolute difference is also a clear indication of an issue so weighting is used.

from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)

# sets up a structure for scoring each station based on threat

riskScores = []

for station in stations:
    # adds risk due to absolute level
    risk = station.latest_level - station.typical_range[1]
    # adds risk due to ratio, weighted appropriately
    risk += relative_water_level(station)*3
    # adds risk due to recent rates
    risk += 
    riskScores.append((station.name,risk))




