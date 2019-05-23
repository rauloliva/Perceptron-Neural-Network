import math as m
from random import random

class Matrix:
    '''
    This class helps to solve operations with matrixes,
    create a new matrix with a number of rows and columns as well
    '''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = []
        self.initMatrix()

    #Inicializamos la matriz en 0
    def initMatrix(self):
        self.data = [[0 for i in range(self.cols)] for j in range(self.rows)]

    
    def copy(self):
        m = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                m.data[i][j] = self.data[i][j]
        return m
    
    
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = random() * 2 - 1

    
    def Add(self,n):
        if type(n) == type(Matrix(0,0)):
            '''
            solve operations like this
             [1,2,3]
             [4,5,6] + n
             [7,8,9]
            '''
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n.data[i][j]
        else:
            '''
            solve operations like this 
             [1,2,3]   [0,7,2]
             [4,5,6] + [3,2,1]
             [7,8,9]   [2,1,3]
            '''
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += n

    
    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.data[i][j])
        return arr

    
    @staticmethod
    def subtract(a,b):
        #Return a matrix a-b
        result = Matrix(a.rows,b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
        return result

    
    def multiply(self,n):
        if (type(n) == Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= n.data[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    val = self.data[i][j]
                    val = val * n
                    self.data[i][j] = val


    @staticmethod
    def multiplyMatrixes(a, b):
        #hadmard product
        if a.cols == b.rows:
            res = Matrix(a.rows,b.cols)
            sumMatrix = 0
            for i in range(len(a.data)):
                for j in range(len(b.data[0])):
                    for k in range(len(b.data)):
                        sumMatrix += a.data[i][k] * b.data[k][j]
                    res.data[i][j] = sumMatrix 
                    sumMatrix = 0
            
            return res

    @staticmethod
    def fromArray(arr):
        m = Matrix(len(arr),1)
        for i in range(len(arr)):
            m.data[i][0] = arr[i]
        return m

    
    def Map(self,func):
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.data[i][j]
                self.data[i][j] = func(val)

    
    @staticmethod
    def MapStatic(matrix,func):
        result = Matrix(matrix.rows,matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                val = matrix.data[i][j]
                result.data[i][j] = func(val)
        return result

    
    @staticmethod
    def transpose(matrix):
        result = Matrix(matrix.cols,matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.data[j][i] = matrix.data[i][j]
        return result

    #method for testing purposes
    def Print(self):
        print(self.data)


