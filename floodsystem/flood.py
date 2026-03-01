
from .utils import sorted_by_key  # noqa

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

    unsortedStationsRelevantData = []
    for station in stations:
        try:
            range = station.typical_range[1]-station.typical_range[0]
            unsortedStationsRelevantData.append((station.name, station.latest_level-range)) # issue here
        except:
            return None

    sortedStationsRelevantData = sorted_by_key(unsortedStationsRelevantData, 1)
    return sortedStationsRelevantData
