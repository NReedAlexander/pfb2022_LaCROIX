#!/usr/bin/env python3
import sys, random
import pandas as pd

def randomize_rain(avg_rain):
    # initialize variables
    nrows = 100
    ncols = 100
    seed_frac = 0.5 #fraction of rows and columns to be set with random seeds

    # set N random seeds
    n_seeds = int(nrows*seed_frac)
    rain_df = pd.DataFrame(avg_rain, index=range(nrows), columns=range(ncols))
    for seed in range(n_seeds):
        # pick a random row and column
        rand_row = random.randrange(0, nrows)
        rand_col = random.randrange(0, ncols)

        # at the random seed, set the rain amount randomly around average +- average
        rain_df.loc[rand_row, rand_col] = random.randrange(0, 2*avg_rain)

        # spread the same value in a random radius with a max of half the number of seeds
        clust_spread = random.randrange(0, n_seeds//2)
        for i in range(rand_row - clust_spread, rand_row + clust_spread):
            for j in range(rand_col - clust_spread, rand_row + clust_spread):
                if (i in range(nrows) and j in range(ncols)):
                    rain_df.loc[i,j] = rain_df.loc[rand_row, rand_col]

    return rain_df

def main():
    nrows = 25
    ncols = nrows
    rain_in = pd.DataFrame(200, index=range(nrows), columns=range(ncols))
    framedict = {'rain':rain_in}
    print(randomize_rain(framedict)['rain'])

if __name__ == '__main__':
    main()
