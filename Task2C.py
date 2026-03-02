from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

stations = build_station_list()

stations = stations_highest_rel_level(stations, 10)

for station in stations:
        print(station.name, station.relative_water_level())