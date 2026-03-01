from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list

stations = build_station_list()

count = 0
stations_to_plot = []
relative_levels =[]
for station in stations:
    if station.relative_water_level > relative_levels[-1]:
        stations_to_plot[-1] = station
        relative_levels= 0