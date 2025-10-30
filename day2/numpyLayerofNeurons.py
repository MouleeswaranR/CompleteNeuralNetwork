import numpy as np

#LIST OF INPUTS
inputs = [1, 2, 3, 2.5]

##LIST OF WEIGHTS
weights = [[0.2, 0.8, -0.5, 1],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]

##LIST OF BIASES
biases = [2, 3, 0.5]


#A dot product of matrix(weights(w)) and vector(inputs(x))
#numpy.dot() function treats matrix as vectors and perform dot product of each of those vectors with input vector
#np.dot(w,x)=np.dot(x,transpose(w)) , np.dot(w,x)!=np.dot(x,w)
output=np.dot(weights,inputs)+biases
print(output)