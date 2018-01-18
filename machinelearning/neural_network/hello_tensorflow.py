# coding:UTF-8
import tensorflow as tf
import numpy as np
import time
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 1. create data
x_data = np.random.rand(100).astype(np.float32)
# predicate function model
y_data = x_data * 0.1 + 0.3

# 2. create tensorflow structure
# 一维参数，初始范围在-1.0~1.0
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# 初始为0
biases = tf.Variable(tf.zeros([1]))
y = Weights * x_data + biases
# 计算方差
loss = tf.reduce_mean(tf.square(y - y_data))

# 将误差传播， 用的是梯度下降法更新参数
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

# 3. active structure
sess = tf.Session()
sess.run(init)

# 4. training data
start_time = time.time()
for step in range(1001):
    sess.run(train)
    if step % 20 == 0:
        print (step, sess.run(Weights), sess.run(biases))
end_time = time.time()
print (end_time - start_time)