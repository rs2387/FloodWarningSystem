from floodsystem.geo import stations_within_radius

from floodsystem.geo import haversine

#making simple station objects to test against the functions in geo.py
class test_station:
    def __init__(self, name, town, coord):
        self.name = name
        self.town = town
        self.coord = coord


def test_haversine():
    #should stay at 0 since at the same point
    p, phi1, lambda1 = (0,0), 0, 0 
    assert haversine(p, phi1, lambda1) == 0

def test_stations_within_radius():
    #makes two fake stations and only set one of them very close to the centre 
    stations, centre, r = [test_station("Kings Cross", "London", (7,10)),
                           test_station("Cambridge Railway", "Cambridge", (0.0001,0.0001))], (0, 0), 5
    assert stations_within_radius(stations, centre, r) == ["Cambridge Railway"]
