import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# MNIST data -> images and labels (train and test) in MNIST_data data set
mnist_data = input_data.read_data_sets('MNIST_data', one_hot=True)

# train_image = mnist_data.train.images[0]
# train_label = mnist_data.train.labels[0]
# print(train_image)
# print(train_label)

# y = mx + b
# graph construction
x_input = tf.placeholder(dftype=tf.float, shape=[None, 784], name='x_input')  # 28*28 = 784 (flattened array)
W = tf.Variable(initial_value=tf.zeros(shape=[784, 10]), name='W')
b = tf.Variable(initial_value=tf.zeros(shape=[10]), name='b')
y_actual = tf.add(x=tf.matmul(a=x_input, b=W, name='matmul'), y=b, name='y_actual')
y_expected = tf.placeholder(dtype=tf.float32, shape=[None, 10], name='y_expected')

# loss function -> use cross_entropy loss func because we are using probability
cross_entropy_loss = tf.reduce_mean(
    input_tensor=tf.nn.softmax_cross_entropy_with_logits(labels=y_expected, logits=y_actual),
    name='cross_entropy_loss')

# optimizer function
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)  # low = longer training time, high = low accuracy

train_step = optimizer.minimize(loss=cross_entropy_loss, name='train_step')
