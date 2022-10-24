#!/usr/bin/env python3

#Creating a world class that can be passed from one thing to next 

import pandas as pd 

pd.set_option('display.max_rows', 100)

import sys, re, os 
import random 
import numpy as np 
#import IPython.display as display

#create array of pandemic tables 

#mainframe = array from Nick thats empty 
#tect_num = number of tectonic plates input from Reeee

#input_m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#mainframe = pd.DataFrame(input_m)
tect_num = 30 
n = 100 #size of array 

#create a cointoss for growth or shrink for later
def cointoss (): 
	return random.choice(['0', '1']) 


#error message if more tectonic plates than positions on array
#if tect_num <= mainframe.shape[0]: 
#	print(f"There cannot be more tectonic plates than {mainframe.shape[0]}") 
#	exit(1)


n=100
#populating table of tectonic plate values
def elevation_generator(tect_num): 
	tectonic_plates = pd.DataFrame(index=range(n), columns=range(n))
	for i in range(tectonic_plates.shape[0]): 
		for j in range(tectonic_plates.shape[1]):
			value = tectonic_plates.at[i,j]
			value = (random.randrange(1, tect_num+1))
			tectonic_plates.at[i,j] = value
#print(tectonic_plates)


#sort the random matrix to create fewer tectonic plates 
	final_array = pd.DataFrame(index=range(n), columns=range(n))
	sort_list = list(range(n))
	for x in sort_list: 
		t = cointoss()
		if t == '1': 
			sorted_array = tectonic_plates.sort_values(by=[x])
			final_array[x] = sorted_array[x].values
		else: 
			sorted_array = tectonic_plates.sort_values(by=[x], ascending=False) 
			final_array[x] = sorted_array[x].values
#print(final_array)
	
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
			value = tectonic_plates.at[i,j]
			if j+1 > n-1 or i+1 > n-1:
					next 
			else:
				value1 = tectonic_plates.at[i,j]
				value2 = tectonic_plates.at[i+1,j]
				value3 = tectonic_plates.at[i,j+1] 
				a = cointoss()
				if value1 < value2:
					if a  == '0':
						valueR = value1 + random.randrange(1,20)
						tectonic_plates = tectonic_plates.replace(value1, valueR)
					else: 
						valueD = value1 - random.randrange(1,20)
						if valueD < 0: 
							tectonic_plates = tectonic_plates.replace(value1, valueD)
				elif value1 < value3: 
					if a == '0': 
						valueR = value1 + random.randrange(1,20)
						tectonic_plates = tectonic_plates.replace(value1, valueR)
					else: 
						valueD = value1 - random.randrange(1,20)
						if valueD < 0: 
							tectonic_plates = tectonic_plates.replace(value1, valueD)
				elif value2 > value3: 
					if a == '0': 
						valueR = value1 + random.randrange(10,200)
						tectonic_plates = tectonic_plates.replace(value1, valueR)
					else: 
						valueD = value1 - random.randrange(10,200)
						if valueD < 0: 
							tectonic_plates = tectonic_plates.replace(value1, valueD)
	elevation_df= tectonic_plates
	#print(elevation_df) 	
	return (elevation_df) 

#tect_num=15
tectonic_plates = pd.DataFrame(index=range(n), columns=range(n))
a = elevation_generator(tect_num) 
print(a)

#makes test data set so you can check if this works 
#def main (): 
#		tectonic_plates = pd.DataFrame(index=range(n), columns=range(n))
#		print(elevation_generator(tectonic_plates) 

#if __name__ == '__main__': 
#	main()
