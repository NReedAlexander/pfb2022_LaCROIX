#!/usr/bin/env python3

#Creating a world class that can be passed from one thing to next 

import pandas as pd 
import sys, re 
import random 
import numpy as np 

#create array of pandemic tables 

#mainframe = array from Nick thats empty 
#tect_num = number of tectonic plates input from Reeee

input_m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mainframe = pd.DataFrame(input_m)
tect_num = 5 
n = 9 #size of array 
print(mainframe)

#create a cointoss for growth or shrink for later
def cointoss (): 
	return random.choice(['+', '-']) 


#error message if more tectonic plates than positions on array
if tect_num <= mainframe.shape[0]: 
	print(f"There cannot be more tectonic plates than {mainframe.shape[0]}") 
	exit(1)

#populating table of tectonic plate values
tectonic_plates = pd.DataFrame(index=range(n), columns=range(n))
for i in range(tectonic_plates.shape[0]): 
	for j in range(tectonic_plates.shape[1]):
		value = tectonic_plates.at[i,j]
		for value in tectonic_plates: 
			value = (random.randrange(1, tect_num+1))
			tectonic_plates.at[i,j] = value
print(tectonic_plates)


#sort the random matrix to create fewer tectonic plates 
final_array = pd.DataFrame(index=range(n), columns=range(n))
sort_list = list(range(n))
for x in sort_list: 
	sorted_array = tectonic_plates.sort_values(by=[x])
	print(sorted_array,'\n')
	final_array[x] = sorted_array[x].values
print(final_array)
	
#sort rows after columns 
#done_array = pd.DataFrame(index=range(n), columns=range(n))
#sort_list = list(range(n))
#for x in sort_list: 
#	row_array = final_array.sort_values(by=[x], axis=0)
#	done_array[x:] = row_array[x:].values
#	print(done_array)

#create elevation using neighbor comparison 
tectonic_plates = final_array
for i in range(tectonic_plates.shape[0]): 
	for j in range(tectonic_plates.shape[1]):
		if j+1 > n or i+1 > n:
				next 
		else:
			value1 = tectonic_plates.at[i,j]
			value2 = tectonic_plates.at[i+1,j]
			value3 = tectonic_plates.at[i,j+1] 
			for value in tectonic_plates: 
				if value1 > value2:
						value1 = value1 + random.randrange(1,250)
print(tectonic_plates) 	


