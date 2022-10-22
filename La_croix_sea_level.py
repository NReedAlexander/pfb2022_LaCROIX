#!/usr/bin/env python3
import pandas as pd
import sys
import numpy as np


input_sea = 5                                           #This is the value that the user will select
elev = [[1,2,3], [4,5,6], [7,8,9]]                      # Arbitratry numbers to make a 3x3 dataframe as data input for determining sea level.
elev_df = pd.DataFrame(elev)      # This is the data fram generated based on elevation innput, will get this from Meike    
#print(elev_df)

sea_lev_df = elev_df.apply(lambda x: x -input_sea)          # Makes a sea level dataframe by taking the input sea level set by the user and substracting from the elevation dataframe. In the following steps if values are <0 then the coordinate is below sea level and the value is set to 0, if the value is >0 the coordinate is above sea level and the value of the coordinate is set to 1. 
#print(sea_lev_df)

land_level = []                                             #Makes an empty list to store the land level values
for x in range(sea_lev_df.shape[0]):                        # Itereate over rows of sea_lev_df 
    for y in range(sea_lev_df.shape[1]):                    # Iterate over columns of sea_lev_df to identify the if and else statements   
        if sea_lev_df.at[x,y] < 0:                          # If values are <0 then the coordinate is below sea level and the value is set to 0   
            land_level.append(0)                            #Adds the value of the coordinate to the land_level list  
        else:
            land_level.append(1)                            #Adds the value of the coordinate to the land_list
#print(land_level)

n = 3                                                        #number of colums we want in the land_level_matrix dataframe
land_level_matrix = [land_level[x:x +n] for x in range(0, len(land_level), n)]  #Breakes single list of land_level into separete lists depending on the number of datapoints and columns (n) we want/have in the dataframe.
#print(land_level_matrix)

land_level_df = pd.DataFrame(land_level_matrix)             #Generates land_level_df from the segmented list above
print(land_level_df)

