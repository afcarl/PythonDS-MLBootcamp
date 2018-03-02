import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
mnist.train.images.shape

# so the images are stored as vectors
mnist.train.images[2].shape

mnist.train.images[2].reshape(28,28)

# these values range from 0-1 and denote how dark the pixel is.
# note 28*28 = 784, so we simply reshape these back into their original 28x28 form

sample = mnist.train.images[2].reshape(28,28)

import matplotlib.pyplot as plt

plt.imshow(sample, cmap='Greys')
# This appears to be the number 4

# how quickly we adjust the cost function
learning_rate = 0.001
training_epochs = 100
batch_size = 100

# network params
n_classes = 10
n_samples = mnist.train.num_examples
n_input = 784

# the more layers we add, the more accurate the model can be, but also the more time it takes to train
n_hidden_1 = 256
n_hidden_2 = 256


def multilayer_perceptron(x, weights, biases):
    '''
    x: placeholder for the data input
    weights: dictionary of weights
    biases: dictionary of bias values
    '''
    # First hidden layer with RELU Activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    # Function on (x * w * b) = RELU --> f(x) = max(0,x)
    layer_1 = tf.nn.relu(layer_1)

    # Second layer
    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)

    # Last output layer
    # could also use tf.add like we did above
    out_layer = tf.matmul(layer_2, weights['out'] + biases['out'])
    return out_layer

weights = {
    # tf.random_normal outputs random values from a normal distribution
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_hidden_2, n_classes]))
    }

biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'out': tf.Variable(tf.random_normal([n_classes]))
    }

x = tf.placeholder('float', [None, n_input])

y = tf.placeholder('float', [None, n_classes])

pred = multilayer_perceptron(x, weights, biases)


cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred,labels=y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

t = mnist.train.next_batch(1)

# here is the real replacement for the long with statement that activates the
# tensorflow session
sess = tf.InteractiveSession()

init = tf.global_variables_initializer()
sess.run(init)

# 15 loops
for epoch in range(training_epochs):
    # cost
    avg_cost = 0.0
    total_batch = int(n_samples/batch_size)

    for i in range(total_batch):

        batch_x, batch_y = mnist.train.next_batch(batch_size)
        _,c = sess.run([optimizer, cost], feed_dict={x:batch_x, y:batch_y})
        avg_cost += c/total_batch
    print("Epoch: {} cost: {:.4f}".format(epoch+1, avg_cost))

print("Model has completed {} Epochs of training".format(training_epochs))


## evaluate the model

correct_predictions = tf.equal(tf.argmax(pred, 1),tf.argmax(y, 1))

correct_predictions = tf.cast(correct_predictions, 'float')
accuracy = tf.reduce_mean(correct_predictions)

accuracy.eval({x:mnist.test.images, y:mnist.test.labels})
