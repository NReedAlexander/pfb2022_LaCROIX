#!/usr/bin/env python3
import sys, random
import pandas as pd

nrows = 25
ncols = 25
rain_in = pd.DataFrame(100, index=range(nrows), columns=range(ncols))
seed_frac = 0.5 #fraction of rows and columns to be set with random seeds
avg_rain = rain_in.loc[0,0]

# set N random seeds
rain_df = rain_in
n_seeds = int(rain_in.shape[0]*seed_frac)
for seed in range(n_seeds):
    # pick a random row and column
    rand_row = random.randrange(0, nrows)
    rand_col = random.randrange(0, ncols)

    # at the random seed, set the rain amount randomly around average +- average
    rain_df.loc[rand_row, rand_col] = random.randrange(0, 2*avg_rain)

    # spread the same value in a random radius with a max of half the number of seeds
    clust_spread = random.randrange(0,n_seeds/2)
    for i in range(rand_row - clust_spread, rand_row + clust_spread):
        for j in range(rand_col - clust_spread, rand_row + clust_spread):
            if (i in range(nrows) and j in range(ncols)):
                rain_df.loc[i,j] = rain_df.loc[rand_row, rand_col]


print(rain_df)


