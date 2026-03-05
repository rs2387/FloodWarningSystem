
from floodsystem.station import MonitoringStation

from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()

update_water_levels(stations)

for station in stations[:120]:
    print(station)