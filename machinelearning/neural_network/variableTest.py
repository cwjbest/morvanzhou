# coding:UTF-8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# tensorflow变量的用法，设0为初始值
state = tf.Variable(0, name='counter')
print(state.name)

# 常量的设置
one = tf.constant(1)
new_value = tf.add(state, one)
# 将new_value赋值state
update = tf.assign(state, new_value)
# 初始化所有变量 一定要
init = tf.global_variables_initializer()

with tf.Session() as sess:
    # 激活变量
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))