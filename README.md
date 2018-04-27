

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

### 그림을 그려보자
#### 4X4의 0과 1로만 이루어진 행렬
```python
list = [[1, 0, 0, 1], [0, 1, 1, 1], [1, 1, 0, 1], [1, 0, 0, 1]]
a = np.array(list, dtype='float32')
plt.imshow(a)
plt.show()
```
![img](https://github.com/jis1218/Python-matplotlib-prac/blob/master/img/FIG2.png)

#### 4X5의 0-1사이의 float 형식인 행렬
```python
list = [[1, 0, 0, 1, 0.5], [0, 1, 1, 1, 0.7], [1, 1, 0, 1, 0.3], [1, 0, 0, 1, 1.5]]
a = np.array(reshaped, dtype='float32')
plt.imshow(a)
plt.show()
```
![img](https://github.com/jis1218/Python-matplotlib-prac/blob/master/img/FIG3.png)

#### MNIST 데이터
```python
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)
batch_xs, batch_ys = mnist.train.next_batch(100)
print(np.shape(batch_xs))
reshaped = np.reshape(batch_xs[10], [28, 28])
plt.imshow(a)
plt.show()
```
![img](https://github.com/jis1218/Python-matplotlib-prac/blob/master/img/FIG4.png)