import os
import cv2  # computer vision for understanding what the drawing is
import numpy as np  # numpy number arrays
import tensorflow as tf  # machine learning
import matplotlib.pyplot as plt  # visualization of the digits


# used to grab the data set. loads directly from tensorflow so we dont have to generate a model
# The MNIST dataset consists of a large collection of grayscale images, each of which represents a handwritten digit (0 through 9).
#  It was created by modifying a subset of the original NIST (National Institute of Standards and Technology) database,
#  which contained handwritten digits from American Census Bureau employees and American high school students.


# we split it into training data and testing data
# all the data has been labeled, the training data is to train the model
# the testing model tests to see how well the model is performing
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
# x_train data is pixel data, y_train data is the classification
# mnist.load_data actually loads the 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images

# now normalize the data, since the image is grayscale, the luminance will range from 0-25,
# scaling it to 0-1 makes processing more understandable and makes it easier for the neural net to do calculations
X_train = tf.keras.utils.normalize(X_train, axis=1)
X_test = tf.keras.utils.normalize(X_test, axis=1)

# This was all preprocessing, now we can create the neural net model


model = tf.keras.models.Sequential()

# add layers to the model
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
# this flattens the layer, instead of having a grid of 28 by 28 pixels we have one flat line of 784px

# now we add a dense layer, this is the most basic layer, where each neuron is connected to each other neuron in the previous layers
model.add(tf.keras.layers.Dense(128, activation='relu'))
# the first parameter is the units for the Neural net layer, these are the amount of neurons in the layer
# the second parameter 'activation="relu"' refers to the activation function to be usedin the layer
# activation layers differentiate the input data so we can differentiate between the images in this case
# relu takes the input and re-maps it from its past relationship to where values below the threshold map to zero,
# inputs above the threshold map to a linear relationship


model.add(tf.keras.layers.Dense(128, activation='relu'))
# the second layer is just to reclassify and differentiate again


model.add(tf.keras.layers.Dense(10, activation='softmax'))
# the last layer is the output layer, this layer will classify all the data into each of their respective digits
# the unit size of 10 is the amount of possible digits, like how each image could be a number 0-9
# the softmax activation function makes it so that all neurons add up to 1, this can be interpreted as the confidence the NN has on
# that image being that certain digit
# the softmax function looks like a sigmoid, but its used for multi-class specification, meaning
# that each of the neurons compete for the highest confidence value, all of the neurons softmax values add up to 1

# now the model has to be compiled
# compiling the model involves many different things to make sure that the model processes the data how you want it
# the first important part of compiling is the optimization.
# optimization changes the weight of the neurons when they process the data so that data loss does not happen

# the second part of compiling is the loss function. the function focuses on the error the NN has
# between its predictions and the truth.

# lastly, we can add things like gpu acceleration or metrics to incorporate parallelism, or get key attributes like
# accuracy or precision

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# the adam (Adaptive Moment Estimation) optimizer is used to make sure the data is being classified optimally
# adam uses the concept of momentum to speed up the accuracy of the neurons.
# it does this by looking at highly changing pieces of information in the loss data set by keeping track of a moving average
# the moving average can help adjust the neurons so their parameters are more tuned to classify test data

# the gradient descent process is the process of adjusting the weights of the neurons to make them more accurate to data in the future
# the concept of momentum helps speed up this process

# adam also uses an adaptive learning rate on each parameter so that they change or stagnate relative
# to their historical gradients

# next is the sparse_categorical_crossentropy function
# the function measures the dissimilarity between the true values and the training data
# using this specific loss function is important for classification problems
# the loss function is in a feedback loop with the optimizer and constantly updates the neurons to make sure they are being updated accordingly


# now we can train the data set using the fit function
model.fit(X_train, y_train, epochs=3)

model.save('handwritten.model')