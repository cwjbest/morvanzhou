# coding:UTF-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 完整构建神经网络
# 添加神经层
def add_layer(inputs, in_size, out_size, activation_function=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    wx_plus_b = tf.matmul(inputs, weights) + biases

    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b)
    return outputs


# 定义数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# None表示，给多少都行
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 隐藏层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)

# 输出层
prediction = add_layer(l1, 10, 1, activation_function=None)

# 误差, 单个误差的平方，求和，再平均
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

# 优化器，减小误差
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 激活变量
init = tf.global_variables_initializer()

# 可视化

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
# plt.ion()
# plt.show(block=False)

sess = tf.Session()
sess.run(init)
for i in range(1000):
    sess.run(train, feed_dict={xs: x_data, ys: y_data})
    if i % 20 == 0:
        # print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=2)
        # ax.lines.remove(lines[0])
        plt.ion()
        plt.show()
        plt.pause(0.1)