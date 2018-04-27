# coding: utf-8
'''
Created on 2018. 3. 12.

@author: Insup Jung
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


if __name__ == '__main__':
    
#     x = np.arange(-6, 6, 0.1)
#     y1 = np.sin(x)
#     y2 = np.cos(x)
# 
#     y5 = 1+x*0
# 
#     plt.plot(x, y5)  
#     plt.plot(x, y1)
#     plt.plot(x, y2)   
# 
#     plt.show()

    mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)
    batch_xs, batch_ys = mnist.train.next_batch(100)
    print(np.shape(batch_xs))
    reshaped = np.reshape(batch_xs[10], [28, 28])


    list = [[1, 0, 0, 1, 0.5], [0, 1, 1, 1, 0.7], [1, 1, 0, 1, 0.3], [1, 0, 0, 1, 1.5]]
    a = np.array(reshaped, dtype='float32')
    
    plt.imshow(a)
    plt.show()
    
    
    
    
#     if epoch == 0 or (epoch+1)%10 ==0:
#                 sample_size = 10
#                 noise = get_noise(sample_size, n_noise)
#                 samples = sess.run(G, feed_dict={Z: noise})
#                 
#                 fig, ax = plt.subplots(1, sample_size, figsize=(sample_size, 1)) #subplots 한 화면에 여러 그래프를 나눠서 그려주는 기능
#                 
#                 for i in range(sample_size):
#                     ax[i].set_axis_off()
#                     ax[i].imshow(np.reshape(samples[i], (28, 28)))
#                     
#                     plt.savefig('samples/{}.png'.format(str(epoch).zfill(3)), bbox_inches='tight')
#                     plt.close(fig)
# 
    pass