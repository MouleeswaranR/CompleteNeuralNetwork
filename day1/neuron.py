#neuron with 3 inputs x1,x2,x3, weights=w1,w2,w3 for each of connection between input and a neuron and a bias
inputs=[1.0,2.0,3.0]
weights=[0.2,0.8,-0.5]
bias=2

output=0
for i in range(len(inputs)):
    output+=(inputs[i]*weights[i])


print(output)


#neuron with 4 inputs x1,x2,x3,x4 weights=w1,w2,w3,w4 for each of connection between input and a neuron and a bias
inputs=[1.0,2.0,3.0,2.5]
weights=[0.2,0.8,-0.5,0.3]
bias=2

output=0
for i in range(len(inputs)):
    output+=(inputs[i]*weights[i])


print(output)
