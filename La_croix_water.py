#!/usr/bin/env python3
import pandas as pd
import sys
import numpy as np


input_sea = 5                                           #This is the value that the user will select
elev_df = pd.DataFrame({'Row_A': [4,4,4],'Row_B': [6,6,6],'Row_C': [7,7,7]})      # This is the data fram generated based on elevation innput    
#sea_lev_df =                                            #This is the output sea level

sea_lev_df = elev_df.apply(lambda x:-input_sea) 
print(sea_lev_df)

