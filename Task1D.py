from floodsystem.stationdata import build_station_list

from floodsystem.geo import rivers_with_station, stations_by_river


stations = build_station_list()
rivers = sorted(rivers_with_station(stations))

print(rivers[:10], len(rivers))

river_dict = stations_by_river(stations)
for key in river_dict:
    river_station_names = []
    for station in river_dict[key]:
        river_station_names.append(station.name)
    river_dict[key] = sorted(river_station_names)


print("River Aire: ", river_dict["River Aire"])
print("River Cam: ", river_dict["River Cam"])
print("River Thames: ", river_dict["River Thames"])

