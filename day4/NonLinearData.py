
import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()
import matplotlib.pyplot as plt


X,Y=spiral_data(samples=100,classes=3)
plt.scatter(X[:,0],X[:,1])
plt.show()