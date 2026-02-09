from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    #empty list should return an empty list
    stations, p = [], (0,0)
    assert stations_by_distance(stations, p) == []
