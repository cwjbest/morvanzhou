# coding:UTF-8
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# 完整构建神经网络
# 添加神经层
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    # tensorboard，要显示哪个元素，就用tf.name_scope('name')包裹起来
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            weights = tf.Variable(tf.random_normal([in_size, out_size]), name='w')
            # 在histogram中显示轨迹
            tf.summary.histogram(layer_name + '/weights', weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
        with tf.name_scope('wx_plus_b'):
            tf.summary.histogram(layer_name + '/biases', biases)
            wx_plus_b = tf.matmul(inputs, weights) + biases
        if activation_function is None:
            outputs = wx_plus_b
            tf.summary.histogram(layer_name + '/outputs', outputs)
        else:
            outputs = activation_function(wx_plus_b)
        return outputs


# 定义数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# 输入层，None表示，给多少都行
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# 隐藏层
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)

# 输出层
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

# 误差, 单个误差的平方，求和，再平均
with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    # events中显示loss的轨迹
    tf.summary.scalar('loss', loss)

# 优化器，减小误差
with tf.name_scope('train'):
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 激活变量
init = tf.global_variables_initializer()

# 显存设置0.7，不然有时会出现显存溢出的问题
sess_config = tf.ConfigProto(allow_soft_placement=True)
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.7)
sess_config.gpu_options.allow_growth = True
sess = tf.Session(config=sess_config)

# 将所有可视化的框架加到这个log里面
# writer = tf.train.SummaryWriter("logs/", sess.graph) 这个是新版本的写法，旧版本用下面这种
# 打包所有视图到logs中
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("logs/", sess.graph)

sess.run(init)

for i in range(1000):
    sess.run(train, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # merged也是需要run的
        result = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(result, i)
