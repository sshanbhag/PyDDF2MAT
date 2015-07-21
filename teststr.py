import sys
import numpy as np

# create numeric list
a = np.asarray([1, 2, 3, 4, 5])

with open('test.txt', 'a') as fp:
    np.savetxt(fp, a, fmt='%.6f', delimiter=',')

