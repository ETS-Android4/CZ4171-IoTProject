import os

import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
from skimage import transform


model = keras.models.load_model("./money.h5")
note_classes = ['fiftydollars', 'fivedollars', 'tendollars', 'twodollars']

# load the image
from PIL import Image
import io

#transform data
# poop = tf.keras.Sequential(
#     [
#     tf.keras.layers.Rescaling(1./255),
#     tf.keras.layers.Conv2D(32, 3, activation="relu"),
#     tf.keras.layers.MaxPooling2D(),
#     tf.keras.layers.Conv2D(32, 3, activation="relu"),
#     tf.keras.layers.MaxPooling2D(),
#     tf.keras.layers.Conv2D(32, 3, activation="relu"),
#     tf.keras.layers.MaxPooling2D(),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation="relu"),
#     tf.keras.layers.Dense(4)
#     ]
# )

# f =  open('fifty.jpg', 'rb')
# path =  (os.path.realpath(f.name))
#
# img = tf.keras.utils.load_img(
#     path, target_size=(32, 32))
#
# img_array = tf.keras.utils.img_to_array(img)
# img_array = tf.expand_dims(img_array, 0) # Create a batch

# load the image
from PIL import Image
import io
with open('fifty.jpg', 'rb') as file:
    image_bytes = file.read()
    pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')



# transform image, same as for training!
data = np.asarray(pillow_img)
data = data / 255.0
data = data[np.newaxis, ..., np.newaxis]
# --> [1, x, y, 1]
data = tf.image.resize(data, [32, 32])
print(data.shape)

predictions =  model.predict(data)
print (predictions)
pred0 = predictions[0]
label0 = np.argmax(pred0)
print(label0)
# important part is this (bc it prints the classification)
print(note_classes[predictions.argmax()])


# data = poop(pillow_img)
#
# model.predict(data)
# predict
# predictions = model(data)
# predictions = tf.nn.softmax(predictions)
# print (predictions)
# pred0 = predictions[0]
# label0 = np.argmax(pred0)
# print(label0)