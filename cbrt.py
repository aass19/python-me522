def cbrt(x):
    print('function for finding cuberoot using newton raphson method.')
   # print('function for finding cuberoot using newton raphson method.')
    
    
    g = 3
    for i in range(10):
        g = (1/3)*(2*g+x/(g*g))
        k=g
        if(abs(k-g)<10e-8):
            break
        
        
    print(g)
    
