def cbrt(x):
    print('function for finding cuberoot using newton raphson method.')
   # print('function for finding cuberoot using newton raphson method.')
    
    
    g = 3
    k = 0
    for i in range(100):
        g = (1/3)*(2*g+x/(g*g))
        
        
        print("cuberoot after %s iteration is %s" %(i,k))
        if(abs(k-g)<10e-14):
            break
        k=g
        
    return g
    
