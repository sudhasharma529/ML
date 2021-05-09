import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from scipy.signal import savgol_filter



values = pd.read_csv(sys.argv[1],header=None)
values_n=np.squeeze(values.to_numpy())
smo_values = savgol_filter(values_n, 17, 3)
ns=np.diff(smo_values)
nsin=np.sign(ns)
nsign=np.diff(nsin)
indxs=np.squeeze(np.argwhere(nsign<0))
newind=np.diff(indxs)
print('Length =',np.median(newind))