'''
Created on 2018. 3. 12.

@author: Insup Jung
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    x = np.arange(-6, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
#     y3 = np.arccosh(x)
#     y4 = np.log2(x)
    y5 = 1+x*0
    
#     for i in range(0, 6, 1):
#         if (y1-y2).any():
#            
#             y3 = 1
#             plt.plot(x, y3)
#             print("hello")
#   
    plt.plot(x, y5)  
    plt.plot(x, y1)
    plt.plot(x, y2)
    
    plt.show()
    
    pass