#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

## Take in dictionary contaning: 1) dataframe filled w avg temp, 2) dataframe of rainfall amts, 
##   3) dataframe of underwater True/False 4) dataframe of elevations


def make_biome_df(elev_df, water_df, rain_df, avgtemp):
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


    ## MAKE DATAFRAME OF BIOME LABELS ##
    biome_df = pd.DataFrame()
    realtemp_df = pd.DataFrame()
    for col in range(ncols):
        for row in range(nrows):
            # save temp and rain level for each cell
            temp = temp_df.loc[row,col]
            rain = rain_df.loc[row,col]

            # set water biomes for underwater cells, skip rest of loop
            if water_df.loc[row,col] == 0:
                if (temp == 'hot' or temp == 'mid'):
                    biome_df.loc[row,col] = 'med_water'
                    realtemp_df.loc[row,col] = 25
                elif temp == 'cold':
                    biome_df.loc[row,col] = 'cold_water'
                    realtemp_df.loc[row,col] = 10
                else:
                    biome_df.loc[row,col] = 'frozen_water'
                    realtemp_df.loc[row,col] = 0
                continue

            # in mountain regions, make the temp one step cooler
            if elev_df.loc[row,col] > elev_thresh:
                if temp == 'hot':
                    temp = 'mid'
                elif temp == 'mid':
                    temp = 'cold'
                elif temp == 'cold':
                    temp = 'frozen'

            # set biome labels based rain levels and temps, populate realtemp df
            if rain > rain_thresh:
                if temp == 'hot':
                    biome_df.loc[row,col] = 'rain_forest'
                    realtemp_df.loc[row,col] = 30
                elif temp == 'mid':
                    biome_df.loc[row,col] = 'temp_forest'
                    realtemp_df.loc[row,col] = 15
                elif temp == 'cold':
                    biome_df.loc[row,col] = 'taiga'
                    realtemp_df.loc[row,col] = 0
                elif temp == 'frozen':
                    biome_df.loc[row,col] = 'polar'
                    realtemp_df.loc[row,col] = -50
            else:
                if temp == 'hot':
                    biome_df.loc[row,col] = 'desert'
                    realtemp_df.loc[row,col] = 50
                elif temp == 'mid':
                    biome_df.loc[row,col] = 'grassland'
                    realtemp_df.loc[row,col] = 20
                elif temp == 'cold':
                    biome_df.loc[row,col] = 'tundra'
                    realtemp_df.loc[row,col] = -15
                elif temp == 'frozen':
                    biome_df.loc[row,col] = 'polar'
                    realtemp_df.loc[row,col] = -30

    return biome_df, realtemp_df

def main():
    # make test dataframes
    temp = 20
    rain_df = pd.DataFrame([[60, 60, 90, 60, 50], [90, 60, 10, 20, 60], [50, 60, 40, 30, 20], [10, 0, 50, 60, 70], [70, 90, 60, 30, 60]])
    water_df = pd.DataFrame([[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1]])
    elev_df = pd.DataFrame([[0, 60, 60, 60, 30], [0, 50, 30, 20, 60], [0, 50, 40, 30, 90], [0, 80, 20, 80, 20], [0, 50, 20, 20, 50]])
    print(f'water\n{water_df}')
    print(f'elevation\n{elev_df}')
    print(f'rain\n{rain_df}')
    
    print(make_biome_df(elev_df, water_df, rain_df, temp))

if __name__ == '__main__':
    main()
