# coding:UTF-8
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[3], [3]])

# 矩阵乘法 matrix multiply np.dot(m1, m2)
product = tf.matmul(matrix1, matrix2)

# Session是为了控制，和输出文件的执行语句
# method1
sess = tf.Session()
result = sess.run(product)
print (result)
sess.close()

# method2 with ... as这种写法更优雅，有一些任务，可能事先需要设置，事后做清理工作,这就是with的工作
with tf.Session() as sess:
    print (sess.run(product))


