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

# This was all preprocessing, now we cna create the model