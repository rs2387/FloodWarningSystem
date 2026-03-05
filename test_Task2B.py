
from floodsystem.flood import stations_level_over_threshold

from floodsystem.station import MonitoringStation

stations = [MonitoringStation("station_id", "measure_id", "label", (0,0), (0,0), "river", "town")]

tol = 0.8
total = stations_level_over_threshold(stations, tol)

for x in range(len(total)-1,0, -1):
    print(total[x])




