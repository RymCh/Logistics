    # -*- coding: utf-8 -*-
    """
    Created on Tue Nov 22 10:25:09 2022

    @author: Elève
    """

    import sys
    from scipy.integrate import quad
    from scipy.stats import poisson
    from scipy.optimize import fmin
    import math
    import matplotlib.pyplot as plt
    import numpy as np

    # Distribution poisson
    def f(x):
        mu = 15

        return poisson.pmf(x, mu)

    # Fonction de répartition de poisson

    def fprime(x, Q):
        mu = 15
        return (Q-x)*poisson.pmf(x, mu)



    def range_generator(start, end):
        current = start
        while current < end:
            yield current
            current += 1
    
    def G(Q):
        h = 1  # (c0 = h)
        p = 9  # (cu = p)
    
        a = 0
        for x in range_generator(0, Q + 1):
            a += fprime(x, Q)
        a = h * a
        
        b = 0
        for x in range_generator(Q, 10000):
            b += fprime(x, Q)
        b = p * b
    
        return a - b


    def m(j):
        if j == 0:
            return 1 / (1 - f(x=0))
        else:
            result = 0
            for i in range(1, j+1):
                result += f(x=i) * m(j - i)
                return result
            
    def M(j):
        if j == 0:
            return 0
        else:
            result = 0
            for i in range(1, j):
                result += f(x=i) * M(j - i)
            return 1 + result
    def C(s, S):
        K = 24
        if s == S:
            return 0
        else:
            result = 0
            for j in range(0, S - s):
                result += m(j) * G(S - j)
            return (K + result) / M(S - s)
        

    
    def main () :
       # print (np.iinfo(np.intp).max)
    
      
        # print(f(x))
        # Fonction inverse de F appliquée à Q*
        # est le point critique (minimum de G)
        # F étant la fonction de répartition de la distribution de poisson. 
        
    # Step0    
        h=1
        p=9
        v=p/(h+p)
        # v= 0.9 , d'apres la courbe des répartition.. ymin=15. (tableau article)
        ymin=14

       
        s=ymin
        S0=ymin
        while True:
           s -= 1
           print(s)
           if C(s, S0) <= G(s):
               break
        s0=s
        c0=C(s0,S0)
        print("first c0",c0)
        
        Szero=S0
        S = Szero + 1
        while G(S) <= c0:
            if C(s, S) < c0:
                Szero = S
                while C(s, Szero) <=G(s+1):
                    s += 1
                    print("s; ",s)
                c0 = C(s, Szero)
                print("c0=", c0)  
            print("S",S)
            S += 1
        #final results
        print("S*",S)
        print("Szero", Szero)
    
        
      
        
    if __name__=="__main__":
        main()