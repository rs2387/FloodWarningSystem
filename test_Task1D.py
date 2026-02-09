from floodsystem.geo import rivers_with_station, stations_by_river
from test_Task1C import test_station


# Tests with duplicates, none value and more than one different river
def test_rivers_with_station():
    stations = [test_station("Kings Cross", "London", (7,10), "River 1"),
                test_station("Johnny Railway", "Cambridge", (0.0001,0.0001), "River 2"),
                test_station("High Cross", "London", (7,10), None),
                test_station("Cambridge Railway", "Cambridge", (0.0001,0.0001), "River 1")]
    assert rivers_with_station(stations) == ["River 1", "River 2"]

# Tests if the station objects at each key river are assigned correctly in the dictionary
def test_stations_by_river():
    stations = [test_station("Kings Cross", "London", (7,10), "River 1"),
                test_station("Johnny Railway", "Cambridge", (0.0001,0.0001), "River 2"),
                test_station("High Cross", "London", (7,10), None),
                test_station("Cambridge Railway", "Cambridge", (0.0001,0.0001), "River 1")]
    assert stations_by_river(stations)["River 1"] == [stations[0], stations[3]]
    assert stations_by_river(stations)["River 2"] == [stations[1]]