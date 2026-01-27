# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import math

earth_radius = 6371

def haversine(p, phi1, lambda1):
    phi2, lambda2 = p[0]*math.pi/180, p[1]*math.pi/180
    deltaphi = phi2 - phi1*math.pi/180
    deltalambda = lambda2 - lambda1*math.pi/180
    hav = (1 - math.cos(deltaphi)+ math.cos(phi1*math.pi/180)*math.cos(phi2)*(1-math.cos(deltalambda)))/2
    theta = 2*math.asin((hav)**0.5)
    return earth_radius*theta



def stations_by_distance(stations, p):
    total = []
    for station in stations:
        total.append((station.name, station.town, haversine(p, station.coord[0], station.coord[1])))

    sorted_total = sorted_by_key(total, 2)


    return sorted_total

def stations_within_radius(stations, centre, r):
    y = []
    for station in stations:
        x = float(haversine(centre, station.coord[0], station.coord[1]))
        if x < r:
            y.append(station.name)


    return y

