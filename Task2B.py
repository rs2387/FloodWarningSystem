from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)

tol = 0.8
total = stations_level_over_threshold(stations, tol)

if len(total) == 1:
    print(total[0])

for x in range(len(total)-1,0, -1):
    print(total[x])







