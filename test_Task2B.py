
from floodsystem.flood import stations_level_over_threshold

from floodsystem.station import MonitoringStation

nones = [MonitoringStation("station_id", "measure_id", "label", (0,0), (0,0), "river", "town")]

zeroes = [MonitoringStation("station_id", "measure_id", "label", (0,0), (0,0), "river", "town")]

typical = [MonitoringStation("station_id", "measure_id", "label", (0,0), (0,0), "river", "town")]

cases = [nones, zeroes, typical]

for case in cases:

    tol = 0.8
    total = stations_level_over_threshold(case, tol)

    for x in range(len(total)-1,0, -1):
        print(total[x])




