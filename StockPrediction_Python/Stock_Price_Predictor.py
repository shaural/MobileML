import tensorflow as tf

# [[1, 0], [0, 1]]
def measure_acc(actual, expected):
    num_correct = 0
    for i in range(len(actual)):
        actual_val = actual[i]
        expected_val = expected[i]
        if actual_val[0] >= actual_val[1] and expected_val[0] >= expected_val[1]:
            num_correct += 1
        elif actual_val[0] <= actual_val[1] and expected_val[0] <= expected_val[1]:
            num_correct += 1
        return (num_correct / len(actual)) * 100

# y = Wx + b
x_input = tf.placeholder(dtype=tf.float32, shape=[None, 5], name='x_input')
y_input = tf.placeholder(dtype=tf.float32, shape=[None, 2], name='y_input')

W = tf.Variable(initial_value=tf.ones(shape=[5, 2]))
b = tf.Variable(initial_value=tf.ones(shape=[2]))

y_output = tf.add(tf.matmul(x_input, W), b, name='y_output')

loss = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(labels=y_input, logits=y_output))
optimizer = tf.train.AdamOptimizer(0.01).minimize(loss)