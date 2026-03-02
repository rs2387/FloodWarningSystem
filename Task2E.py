from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import datetime
from floodsystem.stationdata import update_water_levels

from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()

stations = stations_highest_rel_level(stations, 5)
update_water_levels(stations)
for station in stations:

    dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(days=10))
    plot_water_levels(station, dates, levels)
