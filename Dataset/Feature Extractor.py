import numpy as np
from numpy.lib.npyio import loadtxt
import pandas as pd
from pandas.core.frame import DataFrame
import scipy.stats as ss
from scipy import stats

numbers = range(111,119)
folder = ''

filelist=[]

wear = ['111_Healthy_', '112_Flank Wear_', '113_Nose Wear_', '114_Notch Wear_', '115_Crater Wear_','116_Edge Fracture_','117_Builtup Edge_', '118_All Wear_']

for i in range(8):
    name = folder + str(numbers[i]) + "/Split/" + str(wear[i])
    sublist = []
    for i in range(1,116):
        fname = name + str(i) + '.csv'
        filelist.append(fname)


def RMS(arr):
    sq_sum = 0
    for i in arr:
        sq_sum += i**2

    mean_sq = sq_sum/len(arr)
    return np.sqrt(mean_sq)



def stat(x):
    xmod = np.abs(x)
    a = np.mean(x)                      # Mean
    b = np.median(x)                    # Median
    c = stats.mode(x).mode[0]           # Mode
    d = ss.kurtosis(x)                  # Kurtosis
    e = ss.skew(x)                      # Skewness
    f = np.std(x)                       # Standard Deviation
    g = np.var(x)                       # Variance
    h = ss.sem(x)                       # Standard Error
    i = np.amax(x)                      # Maximum
    j = np.amin(x)                      # Minimum
    k = np.sum(x)                       # Summation
    l = np.ptp(x)                       # Range
    m = np.percentile(x,50)             # 2nd Ouartile
    n = RMS(x)                          # RMS
    o = x.size                          # Count
    p = n/np.mean(xmod)                 # Shape Factor
    q = np.amax(xmod)/np.mean(xmod)     # Impulse Factor
    r = n/np.amax(xmod)                 # Kfactor
    
    R1 = {"Mean": a, 'Median': b, 'Mode' : c, 'Kurtosis': d, "Skewness": e, 
        "Standard Deviation": f, "Variance": g, "Standard Error": h, 'Max': i, 'Min': j,
        'Sum': k, 'Range':l, '2nd Quartile': m, 'RMS':n, 'Count': o, 
        'Shape Factor': p, 'Impulse Factor': q, 'K Factor': r}

    
    return R1
    

# df = pd.DataFrame(columns=["Mean", 'Median', 'Mode' , 'Kurtosis', "Skewness", 
#                             "Standard Deviation", "Variance", "Standard Error", 'Max', 'Min',
#                             'Sum', 'Range', '2nd Quartile', 'RMS', 'Count', 
#                             'Shape Factor', 'Impulse Factor', 'K Factor'])

biglist = []
for i in filelist:
    arr = np.loadtxt(i, delimiter= ",")
    row = stat(arr)
    biglist.append(row)

df = pd.DataFrame(biglist, index = range(1,len(biglist)+1))

df.to_csv("../Dataset/Features.csv")




