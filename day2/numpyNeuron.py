#single neuron
#A dot product of a vector with vector
import numpy as np

inputs=[1.0,2.0,3.0,2.5]
weights=[0.2,0.8,-0.5,0.3]
bias=2

#calculating the output (summation of weights(w) and input(x)) of a neuron using numpy
#np.dot(w,x)=np.dot(x,w)
output=np.dot(inputs,weights)+bias
print(output)