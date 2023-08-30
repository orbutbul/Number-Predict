import os
import cv2 #computer vision for understanding what the drawing is
import numpy as np #numpy number arrays
import matplotlib.pyplot as plt #visualization of the digits
import tensorflow as tf #machine learning


# used to grab the data set. loads directly from tensorflow so we dont have to generate a model
# The MNIST dataset consists of a large collection of grayscale images, each of which represents a handwritten digit (0 through 9).
#  It was created by modifying a subset of the original NIST (National Institute of Standards and Technology) database,
#  which contained handwritten digits from American Census Bureau employees and American high school students.


# we split it into training data and testing data
    # all the data has been labeled, the training data is to train the model
    # the testing model tests to see how well the model is performing
mnist = tf.keras.datasets.mnist
(x_train,y_train) , (x_test,y_test) = mnist.load_data
#x_train data is pixel data, y_train data is the classification
# mnist.load_data actually loads the 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images

# now normalize the data, since the image is grayscale, the luminance will range from 0-25,
# scaling it to 0-1 makes processing more understandable and makes it easier for the neural net to do calculations
x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)

# This was all preprocessing, now we can create the neural net model


model = tf.keras.models.Sequential()

# add layers to the model
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# this flattens the layer, instead of having a grid of 28 by 28 pixels we have one flat line of 784px

# now we add a dense layer, this is the most basic layer, where each neuron is connected to each other neuron in the previous layers
model.add(tf.keras.layers.Dense(128,activation='relu'))
# the first parameter is the units for the Neural net layer, these are the amount of neurons in the layer
# the second parameter 'activation="relu"' refers to the activation function to be usedin the layer 
    # activation layers differentiate the input data so we can differentiate between the images in this case
# relu takes the input and re-maps it from its past relationship to where values below the threshold map to zero,
# inputs above the threshold map to a linear relationship


model.add(tf.keras.layers.Dense(128,activation='relu'))
# the second layer is just to reclassify and differentiate again


model.add(tf.keras.layers.Dense(10,activation='softmax'))
# the last layer is the output layer, this layer will classify all the data into each of their respective digits
# the unit size of 10 is the amount of possible digits, like how each image could be a number 0-9
# the softmax activation function makes it so that all neurons add up to 1, this can be interpreted as the confidence the NN has on
# that image being that certain digit
    # the softmax function looks like a sigmoid, but its used for multi-class specification, meaning
    # that each of the neurons compete for the highest confidence value, all of the neurons softmax values add up to 1
