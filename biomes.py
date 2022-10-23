#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

## Take in dictionary contaning: 1) dataframe filled w avg temp, 2) dataframe of rainfall amts, 
##   3) dataframe of underwater True/False 4) dataframe of elevations


def make_biome_df(mainframe):
    # unpack dictionary of dataframes
    rain_df = mainframe['rain']
    temp_df = mainframe['temp']
    elev_df = mainframe['elev']
    water_df = mainframe['water']

    # get dataframe dimensions
    nrows = rain_df.shape[0]
    ncols = rain_df.shape[1]

    # set thresholds
    rain_thresh = 50
    elev_thresh = elev_df.quantile(0.8).mean()
    print(elev_thresh)

    ## SPLIT LATITUDE COORDINATES INTO FIVE ZONES ##
    lat_splits = np.linspace(0, nrows, num = 6) # requires rows to be divisible by 5
    zones = ['np', 'nt', 'eq', 'st', 'sp'] # north pole, north temperate, equator, south temperate, south pole
    zone_slices = {}
    for i in range(len(lat_splits)-1):
        zone_slices[zones[i]] = [lat_splits[i], lat_splits[i+1]]
        i += 1


    ## CREATE LOOKUP TABLE OF TEMPS ##
    # assign hot, mid, or cold to each latitude zone based on average global temp
    avgtemp = temp_df.iloc[0,0]
    if avgtemp > 60:
        temp_zones = {'np':'hot', 'nt':'hot', 'eq':'hot', 'st':'hot', 'sp':'hot'}
    elif avgtemp > 30:
        temp_zones = {'np':'mid', 'nt':'hot', 'eq':'hot', 'st':'hot', 'sp':'mid'}
    elif avgtemp > 0:
        temp_zones = {'np':'cold', 'nt':'mid', 'eq':'hot', 'st':'mid', 'sp':'cold'}
    elif avgtemp > -30:
        temp_zones = {'np':'frozen', 'nt':'cold', 'eq':'mid', 'st':'cold', 'sp':'frozen'}
    elif avgtemp > -60:
        temp_zones = {'np':'frozen', 'nt':'frozen', 'eq':'cold', 'st':'frozen', 'sp':'frozen'}
    else:
        temp_zones = {'np':'frozen', 'nt':'frozen', 'eq':'frozen', 'st':'frozen', 'sp':'frozen'}


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

            # set water biomes for underwater cells, skip rest of loop
            if water_df.loc[row,col] == True:
                if (temp == 'hot' or temp == 'mid'):
                    biome_df.loc[row,col] = 'med_water'
                elif temp == 'cold':
                    biome_df.loc[row,col] = 'cold_water'
                else:
                    biome_df.loc[row,col] = 'frozen_water'
                continue

            # in mountain regions, make the temp one step cooler
            if elev_df.loc[row,col] > elev_thresh:
                if temp == 'hot':
                    temp = 'mid'
                elif temp == 'mid':
                    temp = 'cold'
                elif temp == 'cold':
                    temp = 'frozen'

            # set biome labels based rain levels and temps
            if rain > rain_thresh:
                if temp == 'hot':
                    biome_df.loc[row,col] = 'rain_forest'
                elif temp == 'mid':
                    biome_df.loc[row,col] = 'temp_forest'
                elif temp == 'cold':
                    biome_df.loc[row,col] = 'taiga'
                elif temp == 'frozen':
                    biome_df.loc[row,col] = 'polar'
            else:
                if temp == 'hot':
                    biome_df.loc[row,col] = 'desert'
                elif temp == 'mid':
                    biome_df.loc[row,col] = 'grassland'
                elif temp == 'cold':
                    biome_df.loc[row,col] = 'tundra'
                elif temp == 'frozen':
                    biome_df.loc[row,col] = 'polar'

    mainframe['biomes'] = biome_df
    return mainframe

def main():
    # make test dataframes
    temp_df = pd.DataFrame(0, index=range(5), columns = range(5))
    rain_df = pd.DataFrame([[60, 60, 90, 60, 50], [90, 60, 10, 20, 60], [50, 60, 40, 30, 20], [10, 0, 50, 60, 70], [70, 90, 60, 30, 60]])
    water_df = pd.DataFrame([[True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False], [True, False, False, False, False]]) 
    elev_df = pd.DataFrame([[0, 60, 60, 60, 30], [0, 50, 30, 20, 60], [0, 50, 40, 30, 90], [0, 80, 20, 80, 20], [0, 50, 20, 20, 50]])
    print(f'water\n{water_df}')
    print(f'elevation\n{elev_df}')
    print(f'rain\n{rain_df}')
    
    dfdict = {'rain':rain_df, 'water':water_df, 'elev':elev_df, 'temp':temp_df}
    print(make_biome_df(dfdict)['biomes'])

if __name__ == '__main__':
    main()
