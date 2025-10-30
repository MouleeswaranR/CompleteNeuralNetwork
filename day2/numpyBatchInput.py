import numpy as np

inputs = [[1.0, 2.0, 3.0, 2.5], 
          [2.0, 5.0, -1.0, 2.0], 
          [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]

#in inputs each row is  a separet input ans in weights each row is a weight from a neuron
#to multiply all inputs in each row(batch) with each neuron's weight we take transpose of weights
layer_output=np.dot(inputs,np.array(weights).T)+biases

print(layer_output)