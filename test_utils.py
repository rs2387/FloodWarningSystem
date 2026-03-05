"""Unit test for the utils module"""

import floodsystem.utils


def test_sort():
    """Test sort container by specific index"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1)
    assert list1[0] == c
    assert list1[1] == b
    assert list1[2] == a

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2)
    assert list1[0] == b
    assert list1[1] == a
    assert list1[2] == c


def test_reverse_sort():
    """Test sort container by specific index (reverse)"""

    a = (10, 3, 3)
    b = (5, 1, -1)
    c = (1, -3, 4)
    list0 = (a, b, c)

    # Test sort on 1st entry
    list1 = floodsystem.utils.sorted_by_key(list0, 0, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 2nd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 1, reverse=True)
    assert list1[0] == a
    assert list1[1] == b
    assert list1[2] == c

    # Test sort on 3rd entry
    list1 = floodsystem.utils.sorted_by_key(list0, 2, reverse=True)
    assert list1[0] == c
    assert list1[1] == a
    assert list1[2] == b

# test cases for all milestone 2 tasks

from floodsystem.station import MonitoringStation

# It has been assumed that the other fields contain no None; this can be refined by going through more entries in database_values_generation.
none = MonitoringStation("station_id_none", "measure_id_none", "label_none", (0,0), None, "river_none", "town_none")

zeroes = MonitoringStation("station_id_zeroes", "measure_id_zeroes", "label_zeroes", (0,0), (0,0), "river_zeroes", "town_zeroes")

zeroes.latest_level = 0

typical1 = MonitoringStation("station_id_typical1", "measure_id_typical1", ["label_typical1", "label_typical1"], (2.5,5), (6,4.2), "river_typical1", "town_typical1")

typical1.latest_level = 5

typical2 = MonitoringStation("station_id_typical2", "measure_id_typical2", ["label_typical2", "label_typical2"], (2.5,5), (2,5.3), "river_typical2", "town_typical2")

typical2.latest_level = 1

typical3 = MonitoringStation("station_id_typical3", "measure_id_typical3", "label_typical3", (0,6), (0,9), "river_typical3", "town_typical3")

typical3.latest_level = 30

case = [none, zeroes, typical1, typical2, typical3]

