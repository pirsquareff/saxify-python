#!/usr/bin/python3

import numpy as np
import pandas as pd
import scipy.stats
import string
import sys, getopt

class SAX:
    def __init__(self, ts_length, sax_length, n_alphabets):
        if (n_alphabets < 3):
            raise ValueError('The alphabet size should be at least 3.')
        
        self.ts_length = ts_length
        self.sax_length = sax_length
        self.n_alphabets = n_alphabets
        self.alphabets = list(string.ascii_uppercase[0:n_alphabets])

        # Given that the normalized time series have highly Gaussian
        # distribution, we can simply determine the "breakpoints" that will
        # produce a equal-sized areas under Gaussian curve
        # Ref: http://www.cs.ucr.edu/~eamonn/SAX.pdf
        breakpoints = []
        breakpoints.append(-np.inf)
        for i in range(1, n_alphabets):
            breakpoints.append(scipy.stats.norm.ppf(i / n_alphabets))
        breakpoints.append(np.inf)
        self.breakpoints = breakpoints
    
    def transform(self, ts):
        ts_normalized = self.__z_normalize(ts)
        ts_paa = self.__reduce_dim_by_paa(ts_normalized)
        ts_discretized = self.__discretize(ts_paa)
        return ''.join(ts_discretized.ravel())
    
    def mindist(self, sax_a, sax_b):
        sax_a_index = np.array([ord(x) - ord('A') for x in list(sax_a)]) + 1
        sax_b_index = np.array([ord(x) - ord('A') for x in list(sax_b)]) + 1
        
        bps = self.breakpoints
        scaling_factor = float(self.ts_length / self.sax_length)
        dists = np.array([0 if np.abs(r - c) <= 1 else bps[np.amax([r, c]) - 1] - bps[np.amin([r, c])] for (r, c) in zip(sax_a_index, sax_b_index)])
        return np.sqrt(scaling_factor * np.sum(dists**2))
    
    def __z_normalize(self, ts):
        return scipy.stats.zscore(ts)
    
    def __reduce_dim_by_paa(self, ts):
        statistic, _, _ = scipy.stats.binned_statistic(np.arange(self.ts_length), ts, statistic='mean', bins=self.sax_length)
        return statistic
    
    def __discretize(self, ts):
        return pd.cut(ts, bins=self.breakpoints, labels=self.alphabets)

def main(argv):
    ts_a_path = ''
    ts_b_path = ''
    x = 7
    y = 5
    z = 6 # Number of alphabet for SAX string
    
    try:
        opts, args = getopt.getopt(argv, 'ha:b:x:y:z:', ['time_series_a=', 'time_series_b=', 'x=', 'y=', 'z='])
    except getopt.GetoptError:
        print('Usage: python3 saxify.py -a <PATH_TO_TIME_SERIES_A> -b <PATH_TO_TIME_SERIES_B> -x <X> -y <Y> -z <Z>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: python3 saxify.py -a <PATH_TO_TIME_SERIES_A> -b <PATH_TO_TIME_SERIES_B> -x <X> -y <Y> -z <Z>')
            sys.exit()
        elif opt in ('-a', '--time_series_a'):
            ts_a_path = arg
        elif opt in ('-b', '--time_series_b'):
            ts_b_path = arg
        elif opt in ('-x'):
            x = int(float(arg))
        elif opt in ('-y'):
            y = int(float(arg))
        elif opt in ('-z'):
            z = int(float(arg))
    if (ts_a_path == '' or ts_b_path == ''):
        print('Usage: python3 saxify.py -a <PATH_TO_TIME_SERIES_A> -b <PATH_TO_TIME_SERIES_B> -x <X> -y <Y> -z <Z>')
        sys.exit(2)
    
    n = 2**x # Time series length
    w = 2**y # SAX string length
    
    TS_A = np.loadtxt(ts_a_path, delimiter=' ')
    TS_B = np.loadtxt(ts_b_path, delimiter=' ')
    
    sax = SAX(ts_length=n, sax_length=w, n_alphabets=z)
    
    SAX_A = sax.transform(TS_A)
    SAX_B = sax.transform(TS_B)
    
    print('SAX_A: {0:s}'.format(SAX_A))
    print('SAX_B: {0:s}'.format(SAX_B))
    
    mindist = np.around(sax.mindist(SAX_A, SAX_B), decimals=2)
    print('Distance between SAX_A and SAX_B: {0:.2f}'.format(mindist))
    
if __name__ == "__main__":
    main(sys.argv[1:])