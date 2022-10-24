#!/usr/bin/env python3

import numpy as np
import sys

## method: resize_map(array)
##
##
## accepts array and resizes
## 
## hard coded scaling factor

def resize_map(input_array):

    scaling_factor = 8 
    input_array = np.array(input_array)
    larger_map = np.repeat(np.repeat(input_array, scaling_factor, axis = 1), scaling_factor, axis = 0)

    return larger_map


def main():

    test_array = np.array([
        [(130,0,255),(0,0,255)],
        [(0,20,130),(130,0,130)],
        [(50,4,55),(200,26,255)]
        ])
    col1, row1, rgb1 = test_array.shape
    print(f'test array has {col1} columns and {row1}')

    larger_map = resize_map(test_array)
    col2, row2, rgb2 = larger_map.shape
    print(f'resized array has {col2} columns and {row2} rows')

    return(larger_map)

if __name__== "__main__":
    main()


