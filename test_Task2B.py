
from floodsystem.flood import stations_level_over_threshold

from floodsystem.station import MonitoringStation

# It has been assumed that the other fields contain no None; this can be refined by going through more entries in database_values_generation.
none = MonitoringStation("station_id_none", "measure_id_none", "label_none", (0,0), None, "river_none", "town_none")

zeroes = MonitoringStation("station_id_zeroes", "measure_id_zeroes", "label_zeroes", (0,0), (0,0), "river_zeroes", "town_zeroes")

typical1 = MonitoringStation("station_id_typical1", "measure_id_typical1", ["label_typical1", "label_typical1"], (2.5,5), (6,4.2), "river_typical1", "town_typical1")

typical2 = MonitoringStation("station_id_typical2", "measure_id_typical2", ["label_typical2", "label_typical2"], (2.5,5), (2,5.3), "river_typical2", "town_typical2")

typical3 = MonitoringStation("station_id_typical3", "measure_id_typical3", ["label_typical3", "label_typical3"], (0,6), (9,0), "river_typical3", "town_typical3")

case = [none, zeroes, typical1, typical2, typical3]

tol = 0.8
total = stations_level_over_threshold(case, tol)
for x in range(len(total)-1,0, -1):
    print(total[x])




