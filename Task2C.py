from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
 
for i in range(0,10):
        print(stations_highest_rel_level(stations, 10))