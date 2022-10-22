#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

## Take in dictionary contaning: 1) dataframe filled w avg temp, 2) dataframe of rainfall amts, 
##   3) dataframe of underwater True/False 4) dataframe of elevations

#mainframe = sys.argv[1]

# set thresholds for rainy/dry and mountain/lowlands
rain_thresh = 50
elev_thresh = 50

# make test dataframes
testrain = [[60, 60, 90, 60, 50], [90, 60, 10, 20, 60], [50, 60, 40, 30, 20], [10, 0, 50, 60, 70], [70, 90, 60, 30, 60]]
testwater = [[True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False]] 
testelev = [[100, 60, 60, 60, 30], [90, 50, 30, 20, 60], [80, 50, 40, 30, 0], [50, 80, 20, 20, 20], [80, 50, 20, 20, 50]]
rain_df = pd.DataFrame(testrain)
water_df = pd.DataFrame(testwater)
elev_df = pd.DataFrame(testelev)
print(f'water\n{water_df}')
print(f'elevation\n{elev_df}')
print(f'rain\n{rain_df}')

# get dataframe dimensions
nrows = rain_df.shape[0]
ncols = rain_df.shape[1]


## SPLIT LATITUDE COORDINATES INTO FIVE ZONES ##
lat_splits = np.linspace(0, nrows, num = 6) # requires rows to be divisible by 5
zones = ['np', 'nt', 'eq', 'st', 'sp'] # north pole, north temperate, equator, south temperate, south pole
zone_slices = {}
for i in range(len(lat_splits)-1):
    zone_slices[zones[i]] = [lat_splits[i], lat_splits[i+1]]
    i += 1


## CREATE LOOKUP TABLE OF TEMPS ##
# assign hot, mid, or cold to each latitude zone based on average global temp
avgtemp = int(sys.argv[1])
#avgtemp = mainframe['Temp'].iloc[0,0]
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


## MAKE DATAFRAME OF TEMPERATURES ##
temp_df = pd.DataFrame()
for col in range(ncols):
    # iterate through rows within latitude zones and set appropriate temps based on temp_zones LUT
    for zone in zones:
        for row in zone_slices[zone]:
            temp_df.loc[row, col] = temp_zones[zone]
temp_df = temp_df.iloc[:-1,:]
print(temp_df)


## MAKE DATAFRAME OF BIOME LABELS ##
biome_df = pd.DataFrame()
for col in range(ncols):
    for row in range(nrows):
        # save temp and rain level for each cell
        temp = temp_df.loc[row,col]
        rain = rain_df.loc[row,col]

        # set biome as water for underwater cells, skip rest of loop
        if water_df.loc[row,col] == True:
            biome_df.loc[row,col] = 'water'
            continue

        # in mountain regions, make the temp one step cooler
        if elev_df.loc[row,col] > elev_thresh:
            if temp == 'hot':
                temp = 'mid'
            elif temp == 'mid':
                temp = 'cold'

        # set biome labels based rain levels and temps
        if rain > rain_thresh:
            if temp == 'hot':
                biome_df.loc[row,col] = 'rain_forest'
            elif temp == 'mid':
                biome_df.loc[row,col] = 'temp_forest'
            elif temp == 'cold':
                biome_df.loc[row,col] = 'taiga'
        else:
            if temp == 'hot':
                biome_df.loc[row,col] = 'desert'
            elif temp == 'mid':
                biome_df.loc[row,col] = 'grassland'
            elif temp == 'cold':
                biome_df.loc[row,col] = 'tundra'
print(biome_df)

            
