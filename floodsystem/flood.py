
from floodsystem.utils import sorted_by_key  # noqa
from floodsystem.stationdata import update_water_levels

# Task 2B, assessing flood risk by level
def stations_level_over_threshold(stations, tol):
    stations_tuple = []
    for station in stations:
        water_ratio = station.relative_water_level()
        #if the ratio is greater than a certain tolerance, it is at risk
        if not(water_ratio == None) and water_ratio > tol :
            stations_tuple.append((station.name, water_ratio))
    return sorted_by_key(stations_tuple, 1)

# Task 2C, most at risk stations
def stations_highest_rel_level(stations, N):

    update_water_levels(stations)

    stationRelativeLevels = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        else:
            stationRelativeLevels.append((station, station.relative_water_level()))

    
    stationRelativeLevels = sorted_by_key(stationRelativeLevels, 1)

    output = []

    temp = len(stationRelativeLevels)
    print(temp)
    for i in range(1,N+1):
        output.append((stationRelativeLevels[temp-i])[0])
    
    return output
