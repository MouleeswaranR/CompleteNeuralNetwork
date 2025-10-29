

inputs=[1.0,2.0,3,0,2.5] #x1,x2,x3,x4
weights=[
    [0.2,0.8,-0.5,1],
    [0.5,-0.91,0.26,-0.5],
    [-0.26,-0.27,0.17,0.87]
]

weight1=weights[0]#weight from inputs x1,x2,x3,x4 to first neuron
weight2=weights[1]#weight from inputs x1,x2,x3,x4 to second neuron
weight3=weights[2]#weight from inputs x1,x2,x3,x4  to third neuron

bias1=2
bias2=3
bias3=0.5

output=[
    inputs[0]*weight1[0]+
    inputs[1]*weight1[1]+
    inputs[2]*weight1[2]+
    inputs[3]*weight1[3]+bias1,
     inputs[0]*weight2[0]+
    inputs[1]*weight2[1]+
    inputs[2]*weight2[2]+
    inputs[3]*weight2[3]+bias2,
     inputs[0]*weight3[0]+
    inputs[1]*weight3[1]+
    inputs[2]*weight3[2]+
    inputs[3]*weight3[3]+bias3,
]

print(output)

