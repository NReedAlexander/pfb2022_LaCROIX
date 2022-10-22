#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

#mainframe = sys.argv[1]

testtemps = [[60, 60, 60, 60, 60], [60, 60, 60, 60, 60], [60, 60, 60, 60, 60], [60, 60, 60, 60, 60], [60, 60, 60, 60, 60]]
testelevs = [[60, 60, 90, 60, 50], [90, 60, 10, 20, 60], [50, 60, 40, 30, 20], [10, 0, 50, 60, 70], [70, 90, 60, 30, 60]]

tempdf = DataFrame(testtemps)
elevdf = DataFrame(testelevs)

elev_df = mainframe['Elev']
nrows = elev_df.shape[0]
lat_splits = np.linspace(0, nrows, num = 6)
north_pole = [lat_splits[0], lat_splits[1]]
north_temp = [lat_splits[1], lat_splits[2]]
equator = [lat_splits[2], lat_splits[3]]
south_temp = [lat_splits[3], lat_splits[4]]
south_pole = [lat_splits[4], lat_splits[5]]

avgtemp = mainframe['Temp'].loc[0,0]
if avgtemp > 90:
    temp_zones = {'np':'hot', 'nt':'hot', 'eq':'hot', 'st':'hot', 'sp':'hot'}
elif avgtemp > 70:
    temp_zones = {'np':'mid', 'nt':'hot', 'eq':'hot', 'st':'hot', 'sp':'mid'}
elif avgtemp > 50:
    temp_zones = {'np':'cold', 'nt':'mid', 'eq':'hot', 'st':'mid', 'sp':'cold'}
elif avgtemp > 30:
    temp_zones = {'np':'cold', 'nt':'cold', 'eq':'mid', 'st':'cold', 'sp':'cold'}
else:
    temp_zones = {'np':'cold', 'nt':'cold', 'eq':'cold', 'st':'cold', 'sp':'cold'}

water_df = mainframe['Water']
nrows = water_df.shape[0]
ncols = water_df.shape[1]

temps = DataFrame()
zone_keys = {north_pole:'np'
for col in range(ncols):
    for zone in [north_pole, north_temp, equator, south_temp, south_pole]:
        for row in zone:
            temps[row, col] = temp_zones[zone_keys[zone]]


            
