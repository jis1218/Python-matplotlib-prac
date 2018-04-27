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

    y5 = 1+x*0

    plt.plot(x, y5)  
    plt.plot(x, y1)
    plt.plot(x, y2)   

    plt.show()

    pass