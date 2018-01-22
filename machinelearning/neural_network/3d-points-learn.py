import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import animation

x_data = np.random.normal(0, 0.5, 200)[:, None]
y_data = np.random.normal(0, 0.5, 200)[:, None]
noise = np.random.normal(0, 0.02, x_data.shape)
z_data = np.sqrt(x_data * x_data + y_data * y_data) + noise

x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])
z = tf.placeholder(tf.float32, [None, 1])

Weight_l11 = tf.Variable(tf.random_normal([1, 10]))
Weight_l12 = tf.Variable(tf.random_normal([1, 10]))
biases_L1 = tf.Variable(tf.zeros([1, 10]))
Wx_plus_b_L1 = tf.matmul(x, Weight_l11) + tf.matmul(y, Weight_l12) + biases_L1
L1 = tf.nn.tanh(Wx_plus_b_L1)

Weight_l2 = tf.Variable(tf.random_normal([10, 1]))
biases_L2 = tf.Variable(tf.zeros([1, 1]))
Wx_plus_b_L2 = tf.matmul(L1, Weight_l2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)

loss = tf.reduce_mean(tf.square(z - prediction))

tran_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    ax = Axes3D(plt.figure())
    x_data1 = np.random.normal(0, 0.5, 200)[:, None]
    y_data1 = np.random.normal(0, 0.5, 200)[:, None]
    plt.ion()
    for _i in range(2000):
        sess.run(tran_step, feed_dict={x: x_data, y: y_data, z: z_data})
        if (_i % 50 == 0):
            prediction_value = sess.run(prediction, feed_dict={x: x_data1, y: y_data1})
            ax.scatter(x_data, y_data, z_data, color='g')
            ax.scatter(x_data1, y_data1, prediction_value, color='r')
            plt.pause(0.05)
            plt.cla()
    plt.ioff()
    plt.show()
pass
#
# 	prediction_value=sess.run(prediction,feed_dict={x:x_data})
# 	plt.figure()
# 	plt.scatter(x_data,y_data)
# 	plt.plot(x_data,prediction_value,'r-',lw=5)
# 	plt.show()
# 	x_data1 = np.random.normal(0, 0.5, 200)[:, None]
# 	y_data1 = np.random.normal(0, 0.5, 200)[:, None]
# 	prediction_value = sess.run(prediction, feed_dict={x: x_data1,y:y_data1})
# 	ax = Axes3D(plt.figure())
# 	ax.scatter(x_data, y_data,z_data,color='g')
# 	ax.scatter(x_data1, y_data1, prediction_value,color='r')
# 	# ax.plot_surface(x_data,y_data,z_data,color='b')
# 	# ax.plot_surface(x_data, y_data, prediction_value)
# 	plt.show()
