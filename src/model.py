import numpy as np
from keras.applications.vgg16 import VGG16
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
import os
from keras.callbacks import History 
from keras import optimizers


#This file contains code to build the deep learning model

def data_generator(dir_name, nrow, ncol, batch_size):
	#dir_name: directory where our data is present (folder containing both classes)
	#nrow, ncol: input dimensions
	#batch_size: mini batch size

	#Normalizing image, doing data augmentation
	#Using 20% of the data for validation
	data = ImageDataGenerator(rescale=1./255, rotation_range=40, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, validation_split=0.2)

	train_generator = data.flow_from_directory(dir_name, target_size=(nrow,ncol), seed = 42, batch_size=batch_size, class_mode='binary', subset = "training")

	validation_generator = data.flow_from_directory(dir_name, target_size=(nrow,ncol), seed = 42, batch_size=batch_size, class_mode='binary', subset = "validation")

	return train_generator, validation_generator

def model(nrow, ncol, nchannel, batch_size, data_dir, n_epochs):
	#nrow, ncol, nchannel: input dimensions
	#batch_size: mini batch size
	#data_dir: directory where our data is present (folder containing both classes)
	#n_epochs: number of epochs to run training for

	#Using pretrained VGG16 models, importing all layers except the fully connected ones
	base_model = VGG16(weights='imagenet', include_top = False, input_shape=(nrow,ncol,nchannel))

	model = Sequential()

	for layer in base_model.layers:
		model.add(layer)

	#Making sure I do not train the layers we import
	for layer in model.layers:
		layer.trainable = False

	#Adding my own layers
	model.add(Flatten())
	model.add(Dense(128, activation = 'relu'))
	model.add(BatchNormalization())
	model.add(Dropout(0.5))
	model.add(Dense(64, activation = 'relu'))
	model.add(BatchNormalization())
	model.add(Dense(1, activation = 'sigmoid'))

	train, val = data_generator(data_dir, nrow, ncol, batch_size)

	model.compile(optimizer=optimizers.Adam(lr=1e-3, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0), loss='binary_crossentropy', metrics=['accuracy'])

	hist = model.fit_generator(train, epochs = n_epochs, validation_data = val)

	return model, hist


if __name__ == '__main__':

	path = os.path.join("..", "data", "photos")
	model, _ = model(nrow = 64, ncol = 64, nchannel = 3, batch_size = 32, data_dir = path, n_epochs = 5)

	model.save('my_model.h5')	#Save model
