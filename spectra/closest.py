import numpy as np

def closest(array,value):
    idx = (np.abs(array-value)).argmin()
    return idx
