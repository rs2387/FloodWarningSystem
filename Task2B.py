from floodsystem.stationdata import build_station_list

stations = build_station_list()

for station in stations:
    if station.water_ratio > 0.8:
        print(station.name, station.water_ratio)



