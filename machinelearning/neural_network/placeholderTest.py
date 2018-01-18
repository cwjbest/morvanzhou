# coding:UTF-8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# placeholder是tensorflow中的占位符，需要外部传入data时，就要用这个,得预定义类型，一般float32即可
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    # placeholder与feed_dict绑定使用，一个占位，一个填充
    print(sess.run(output, feed_dict={input1: [7], input2: [2]}))
