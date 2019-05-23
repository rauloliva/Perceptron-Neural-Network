class Learn:
    #w1 = .4 w2 = .2 umbral = .3
    def __init__(self, x1, x2 , y,w1=.2,w2=.6,umbral=.4,A=.2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y = y
        self.__umbral = umbral
        self.__A = A
        self.__w1 = w1
        self.__w2 = w2
        self.ciclos = len(x1)
        self.ciclosCompletados = 0

    def solve(self):
        while self.ciclosCompletados < self.ciclos:
            for i, x1, x2, y in zip(range(self.ciclos),self.__x1,self.__x2,self.__y):
                z = (x1 * self.__w1) + (x2 * self.__w2) - self.__umbral
                z = 0 if z <= 0 else 1
                if(z == y):
                    print(f" {z}")
                else:
                    #if the values were changed, we need to start another loop, 
                    #once we have completed the current one
                    self.__fix(i,z)
                    self.ciclosCompletados = 0 
                self.ciclosCompletados += 1
            print("--------------------------")

    def __fix(self,i,z):
        stop = False
        iteraciones = 1
        while not stop: #until we have reached the solution
            e = (self.__y[i] - z)
            tumbral = -(self.__A * e)
            tw1 = (self.__A * e) * self.__x1[i]
            tw2 = (self.__A * e) * self.__x2[i]
            #sum the actual values with the new ones
            self.__umbral = self.__umbral + tumbral
            self.__w1 = self.__w1 + tw1
            self.__w2 = self.__w2 + tw2

            z = (self.__x1[i] * self.__w1) + (self.__x2[i] * self.__w2) - self.__umbral
            z = 0 if z <= 0 else 1
            if(z == self.__y[i]):
                #show the row where the values were changed
                print(f" {z} -> {iteraciones} cambios de valores")
                stop = True
            iteraciones += 1
    
    def printValues(self):
        print("Final Values:")
        print(f"\n w1 = {self.__w1}")
        print(f" w2 = {self.__w2}")
        print(f" umbral = {self.__umbral}")
        print(f" A = {self.__A}")

    def printInit(self):
        print("Initial Values:\n")
        print(f" w1 = {self._Learn__w1}")
        print(f" w2 = {self._Learn__w2}")
        print(f" umbral = {self._Learn__umbral}")
        print(f" A = {self._Learn__A}\n")