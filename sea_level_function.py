#!/usr/bin/env python3
import pandas as pd
import sys
import numpy as np


#input_sea = .5                                           #This is the value that the user will select Range -1000 to 10000  0 to -1
#elev = [[50,60,60,50,50], [60,10,1,2,60], [60,8,9,10,80],[60,8,7,6,80],[80,70,90,60,80,]]                      # Arbitratry numbers to make a 3x3 dataframe as data input for determining sea level.

#elev_df = pd.DataFrame(elev)      # This is the data fram generated based on elevation innput, will get this from Meike    
#print(elev_df)

def sea_level(elev_df,waterlev):


# working out ratios to make sea

    elevation_np = elev_df.to_numpy(copy=True)
#print(elevation_np)

    max_elev = elevation_np.max()
#print(max_elev)
    min_elev = elevation_np.min()
#print(min_elev)

    elev_norm_df = elev_df.apply(lambda x: (x/ max_elev))
#print('elev_norm_df',elev_norm_df)

# This works to show oceans

    sea_lev_df = elev_norm_df.apply(lambda x: x -input_sea)          # Makes a sea level dataframe by taking the input sea level set by the user and substracting from the elevation dataframe. In the following steps if values are <0 then the coordinate is below sea level and the value is set to 0, if the value is >0 the coordinate is above sea level and the value of the coordinate is set to 1. 
#print(sea_lev_df)

    water_level = []                                             #Makes an empty list to store the water level values
    for x in range(sea_lev_df.shape[0]):                        # Itereate over rows of sea_lev_df 
        for y in range(sea_lev_df.shape[1]):                    # Iterate over columns of sea_lev_df to identify the if and else statements   
            if sea_lev_df.at[x,y] < 0:                          # If values are <0 then the coordinate is below sea level and the value is set to 0   
                water_level.append(0)                            #Adds the value of the coordinate to the water_level list  
            else:
                water_level.append(1)                            #Adds the value of the coordinate to the water_list
#print(water_level)

    n = 100                                                        #number of colums we want in the water_level_matrix dataframe
    water_level_matrix = [water_level[x:x +n] for x in range(0, len(water_level), n)]  #Breakes single list of water_level into separete lists depending on the number of datapoints and columns (n) we want/have in the dataframe.
    #print(water_level_matrix)

    water_level_df = pd.DataFrame(water_level_matrix)             #Generates water_level_df from the segmented list above
    #print(water_level_df)


#This is for making lakes
    elevation_np = elev_df.to_numpy(copy=True)
#print(elevation_np)
    loc_min = []
    rows = elevation_np.shape[0]
    cols = elevation_np.shape[1]

    for ix in range(0, rows - 1):
        for iy in range(0, cols - 1):
    #        print(f' x{ix} y{iy} elevation{elevation_np[ix, iy]}')
            if elevation_np[ix, iy] < elevation_np[ix, iy + 1] and elevation_np[ix, iy] < elevation_np[ix, iy - 1] and \
           elevation_np[ix, iy] < elevation_np[ix + 1, iy] and elevation_np[ix, iy] < elevation_np[ix + 1, iy - 1] and \
           elevation_np[ix, iy] < elevation_np[ix + 1, iy + 1] and elevation_np[ix, iy] < elevation_np[ix - 1, iy] and \
           elevation_np[ix, iy] < elevation_np[ix - 1, iy - 1] and elevation_np[ix, iy] < elevation_np[ix - 1, iy + 1]:
                 temp_pos = (ix, iy)
                 loc_min.append(temp_pos)
#                print('minimun') 
#print(loc_min)

    for coords in loc_min:
    #    print(coords)

        x,y = coords
    #    print(land_level_df.iloc[x,y]) 
   
        water_level_df.iloc[x,y] = 0
    #    print(land_level_df.iloc[x,y])

    return water_level_df


#xyz = sea_level(elev_df,input_sea)
#print(xyz)  
