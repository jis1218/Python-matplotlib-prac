

```python
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    x = np.arange(-6, 6, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y5 = 1+x*0 # y=k인 상수 그래프를 그리는 방법
 
    plt.plot(x, y5)  
    plt.plot(x, y1)
    plt.plot(x, y2)
    
    plt.show()
    
    pass
```

![img](https://github.com/jis1218/Python-matplotlib-prac/blob/master/img/FIG.png)