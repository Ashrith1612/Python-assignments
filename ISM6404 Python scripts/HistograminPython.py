# histogram of random numbers

import numpy as np

ListOfNormalRandomNums = np.random.normal(100,20,500)
print (ListOfNormalRandomNums)

import matplotlib.pyplot as plt
plt.hist(ListOfNormalRandomNums, bins=10)
plt.show()
