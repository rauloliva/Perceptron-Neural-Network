import matrix as m
from math import exp

#Ecuacion o funcion de activacion
def sigmoid(x):
    return 1 / (1 + exp(-x))

def dsigmoid(y):
    return y *(1-y)

class NeuralNetwork:
    def __init__(self,input_nodes,hidden_nodes,output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = m.Matrix(self.hidden_nodes,self.input_nodes)
        self.weights_ho = m.Matrix(self.output_nodes,self.hidden_nodes)
        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = m.Matrix(self.hidden_nodes,1)
        self.bias_o = m.Matrix(self.output_nodes,1)
        self.bias_h.randomize()
        self.bias_o.randomize()
        self.learinig_rate = 0.1

    def feedfoward(self,input_array):
        #Generating the Hidden outputs
        inputs = m.Matrix.fromArray(input_array)
        hidden = m.Matrix.multiplyMatrixes(self.weights_ih,inputs)
        hidden.Add(self.bias_h)

        #Activation function
        hidden.Map(sigmoid)

        #Generating the output's output
        output = m.Matrix.multiplyMatrixes(self.weights_ho,hidden)
        output.Add(self.bias_o)
        output.Map(sigmoid)
        
        #Sending back to the caller
        return output.toArray()

    #entrenamos la neurona
    def train(self,input_array,target_array):
        #Generating the Hidden outputs
        inputs = m.Matrix.fromArray(input_array)
        hidden = m.Matrix.multiplyMatrixes(self.weights_ih,inputs)
        hidden.Add(self.bias_h)

        #Activation function
        hidden.Map(sigmoid)

        #Generating the output's output
        outputs = m.Matrix.multiplyMatrixes(self.weights_ho,hidden)
        outputs.Add(self.bias_o)
        outputs.Map(sigmoid)

        #Convert array to matrix object
        targets = m.Matrix.fromArray(target_array)

        #Calculate the error
        #Error = target - Outputs
        output_errors = m.Matrix.subtract(targets,outputs)
        #gradient = outputs * (1-outputs)
        #Calculate gradient
        gradients = m.Matrix.MapStatic(outputs,dsigmoid)
        gradients.multiply(output_errors)
        gradients.multiply(self.learinig_rate)

        #Calculate Deltas
        hidden_T = m.Matrix.transpose(hidden)
        weights_ho_deltas = m.Matrix.multiplyMatrixes(gradients,hidden_T)

        #Adjust the weights by deltas
        self.weights_ho.Add(weights_ho_deltas)
        #Adjust the bias by its deltas(gradients)
        self.bias_o.Add(gradients)

        #Calculate the hidden layer errors
        who_t = m.Matrix.transpose(self.weights_ho)
        hidden_errors = m.Matrix.multiplyMatrixes(who_t,output_errors)

        #calculate hidden gradient
        hidden_gradient = m.Matrix.MapStatic(hidden,dsigmoid)
        hidden_gradient.multiply(hidden_errors)
        hidden_gradient.multiply(self.learinig_rate)

        #Calculate input to hidden deltas 
        input_T = m.Matrix.transpose(inputs)
        weights_ih_deltas = m.Matrix.multiplyMatrixes(hidden_gradient,input_T)
        
        self.weights_ih.Add(weights_ih_deltas)

        #Adjust the bias by its deltas(gradients)
        self.bias_h.Add(hidden_gradient)