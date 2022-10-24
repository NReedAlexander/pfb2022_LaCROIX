#!/usr/bin/env python3
import pandas as pd
import random
from sea_level_function import *
from biomes import *
from random_rain import *
import ASCIIoverlay

pd.set_option('display.max_rows',100)

nrow = 100
elev_df = pd.DataFrame()
for row in range(nrow):
    for col in range(nrow):
        elev_df.loc[row,col] = random.randrange(0,100)
temp = 20
rain_val = 200 
water_level = 0.5

rain_df = randomize_rain(rain_val)
water_df = sea_level(elev_df, water_level)
biome_df, temp_df = make_biome_df(elev_df, water_df, rain_df, temp)

ASCIIoverlay.overlayASCII('Test Planet', rain_df, elev_df, biome_df, temp_df, water_df)

