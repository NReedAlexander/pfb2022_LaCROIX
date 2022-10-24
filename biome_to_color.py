#!/usr/bin/env python3 

#this script converts biome information to colors 

#input comes from Irene's biome array 

import pandas as pd 
pd.set_option('display.max_rows', 100) 

import numpy as np


#array = [['desert', 'med_water', 'frozen_water', 'temp_forest'],['rain_forest', 'taiga', 'tundra', 'grassland'], ['cold_water', 'polar', 'grassland', 'rain_forest']]
#test_df = pd.DataFrame(array)
#print(test_df)

#Biomes color relationship
#desert= (245,222,179) 'wheat' 
#grassland= (218,165,32) golden rod
#tundra= (189,183,107) dark khaki
#rain_forest= (34,139,34) forest green
#temp_forest= (154,205,50) yellow green 
#taiga= (85,107,47) dark olive green 
#polar= (250,250,250) snow
#frozen_water= (244,255,255) azure
#cold_water= (135,206,250) light sky blue 
#med_water= (0,0,255) blue 

#biomes_df = test_df
#print(biomes_df) 



#biomes_df.replace({'desert': (255,215,0)})
#print(biomes_df)




def biome_colors(biomes_df):
	for i in range(biomes_df.shape[0]):
		for j in range(biomes_df.shape[1]): 
			value1 = biomes_df.at[i,j]
			for value in biomes_df: 
				if value1 == 'desert': 
#					biomes_df = biomes_df.replace(to_replace=['desert'], value=['(255,215,0)'])
					biomes_df.loc[i].at[j] = (245,222,179)
				elif value1 == 'grassland': 
#					biomes_df = biomes_df.replace(to_replace=['grassland'], value=['(218,165,32)'])
					biomes_df.loc[i].at[j] = (218,165,32)
				elif value1 == 'tundra': 
#					biomes_df = biomes_df.replace(to_replace=['tundra'], value=['(189,183,107)'])
					biomes_df.loc[i].at[j] = (189,183,107)
				elif value1 == 'rain_forest': 
#					biomes_df = biomes_df.replace(to_replace=['rain_forest'], value=['(34,139,34)'])
					biomes_df.loc[i].at[j] = (34,139,34)
				elif value1 == 'temp_forest': 
#					biomes_df = biomes_df.replace(to_replace=['temp_forest'], value=['(154,205,50)'])
					biomes_df.loc[i].at[j] = (154,205,50)
				elif value1 == 'taiga': 
#					biomes_df = biomes_df.replace(to_replace=['taiga'], value=['(85,107,47)'])
					biomes_df.loc[i].at[j] = (85,107,47)
				elif value1 == 'polar': 
#					biomes_df = biomes_df.replace(to_replace=['polar'], value=['(250,250,250)'])
					biomes_df.loc[i].at[j] = (250,250,250)
				elif value1 == 'frozen_water': 
#					biomes_df = biomes_df.replace(to_replace=['frozen_water'], value=['(244,255,255)'])
					biomes_df.loc[i].at[j] = (244,255,255)
				elif value1 == 'cold_water': 
#					biomes_df = biomes_df.replace(to_replace=['cold_water'], value=['(135,206,250)'])
					biomes_df.loc[i].at[j] = (135,206,250)
				elif value1 == 'med_water':
 					biomes_df.loc[i].at[j] = (0,0,255)
#					biomes_df = biomes_df.replace(to_replace=['med_water'], value='(0,0,255)')


#print(biomes_df,'\n') 

#convert string to touples
#for i in range(biomes_df.shape[0]):
#	for j in range(biomes_df.shape[1]): 
#		value1 = biomes_df.at[i,j]
#		for value in biomes_df: 
#			my_tuple = eval(value1)
#			print(my_tuple)

#convert df to numpy array 
	pixel_map = np.array(biomes_df)
#biomes_np2 = tuple(map(int, biomes_np1))
#print(biomes_np1)
	return pixel_map

#a = biome_colors(test_df)
#print(a)
#print(a[0][2][0])
