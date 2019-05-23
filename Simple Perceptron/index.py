from Learn import Learn

if __name__ == "__main__":
    x1 = [0,0,1,1]
    x2 = [0,1,0,1]
    y = [0,0,0,1] # AND Gate
    #y = [1,0,0,0] # NOR Gate
    
    learn = Learn(x1,x2,y)
    learn.printInit()
    learn.solve()
    learn.printValues()