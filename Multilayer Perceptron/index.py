from NeuralNetwork import NeuralNetwork
from random import choice

#XOR logic gate
training_data = [
    {
        "inputs": [0,1],
        "targets":[1]
    },
    {
        "inputs": [1,0],
        "targets":[1]
    },
    {
        "inputs": [0,0],
        "targets":[0]
    },
    {
        "inputs": [1,1],
        "targets":[0]
    }
]

def execute(training_data):
    #create a neural network with 2 inputs , 2 hidden layers and 1 output
    nn = NeuralNetwork(2,2,1)

    for i in range(50000):
        data = choice(training_data)
        nn.train(data.get('inputs'),data.get('targets'))

    for data in training_data:
        print(nn.feedfoward(data.get('inputs')))    

if __name__ == "__main__":
    execute(training_data)