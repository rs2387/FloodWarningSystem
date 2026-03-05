
from floodsystem.flood import stations_level_over_threshold

stations = test_station("Name 1", "City 1", (0,0), "River 1"), test_station("Name 2", "City 2", (0,0), "River 2"), test_station("Name 3", "City 3", (0,0), "River 3"), test_station("Name 4", "City 4", (0,0), "River 4"), test_station("Name 5", "City 5", (0,0), "River 5")

tol = 0.8
total = stations_level_over_threshold(stations, tol)

for x in range(len(total)-1,0, -1):
    print(total[x])




