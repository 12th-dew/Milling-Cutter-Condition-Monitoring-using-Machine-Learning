import numpy as np
import os

numbers = range(111,119)

for i in range(8):
    name = str(numbers[i]) + '.csv'
    file = np.loadtxt(name, delimiter= ',')
    split = np.split(ary = file, indices_or_sections= 115)


    if not os.path.exists(str(numbers[i])):
        os.makedirs(str(numbers[i]))
    
    count = 1
    for j in split:
        name = str(numbers[i]) +'/' +  str(numbers[i])+ '_' + str(count)+ ".csv"
        count += 1
        j.tofile(name, sep = ',')