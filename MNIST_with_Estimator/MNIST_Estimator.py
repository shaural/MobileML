import tensorflow as tf
import numpy as np

mnist_data = tf.contrib.learn.datasets.load_dataset('mnist')
x_train = mnist_data.train.images
y_train  = np.asarray(mnist_data.train.labels, dtype=np.int32)
x_eval = mnist_data.test.images
y_eval = np.asarray(mnist_data.test.labels, dtype=np.int32)


# y = Wx + b
def model_fn(features, labels, mode):
    x = tf.reshape(features['x'], [-1, 784])
    W = tf.get_variable(name='W', shape=[784, 10], dtype=tf.float32)
    b = tf.get_variable(name='b', shape=[10], dtype=tf.float32)
    y = tf.add(tf.matmul(x, W), b)

    one_hot_labels = tf.one_hot(indices=tf.cast(labels, tf.int32), depth=10)
    loss = tf.losses.softmax_cross_entropy(one_hot_labels=one_hot_labels, logits=y)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.005)
    train_step = optimizer.minimize(loss=loss, global_step=tf.train.get_global_step())

    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_step)

