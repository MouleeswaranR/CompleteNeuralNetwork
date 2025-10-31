import numpy as np
#batch of inputs(x1,x2,x3,x4) each row is a separate input
inputs = [[1, 2, 3, 2.5],
          [2., 5., -1., 2],
          [-1.5, 2.7, 3.3, -0.8]]
inputs=np.array(inputs)
# weights from neurons of hidden layer 1 each row is a weight from a hidden layer 1's neuron to the inputs
weights = [[0.2, 0.8, -0.5, 1],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
weights=np.array(weights)

biases = [2, 3, 0.5]
biases=np.array(biases)
# weights from neurons of hidden layer 2 each row is a weight from a neuron of hidden layer 2 to the hidden layer 1's neurons

weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]
weights2=np.array(weights2)

biases2 = [-1, 2, -0.5]
biases2=np.array(biases2)

#output from  neurons of hidden layer 1 input will be from given inputs matrix where each row is a separate input
layer_output1=np.dot(inputs,weights.T)+biases


#output from  neurons of hidden layer 2 input will be from previous hidden layer(hidden layer 1)'s output where each row is a separate input
layer_output2=np.dot(layer_output1,weights2.T)+biases2

print(layer_output2)