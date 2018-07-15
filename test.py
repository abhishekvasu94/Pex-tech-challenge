import sys
import h5py
from skimage.io import imread
import numpy as np
from skimage.transform import resize
from keras.models import load_model
import warnings
import pdb
import os
import click

@click.command()
@click.option('--img')

#This contains the code to test the model
def cli(img):

	if img is None:
		click.echo("Please insert path to an image")
		exit

	try:
		img = imread(img)

	except IOError:
		click.echo("Please insert the correct path")
		exit

	warnings.filterwarnings("ignore")			#Don't display any unnecessary warnings
	model = load_model(os.path.join('src', '')+'my_model.h5')
	resize_row = 64
	resize_col = 64

	resized_img = resize(img, (resize_row, resize_col))	#resize image
	resized_img = np.expand_dims(resized_img, axis = 0)

	out = model.predict(resized_img)

	if round(out[0]) == 0:
		click.echo("Indoor")

	elif round(out[0]) == 1:
		click.echo("Outdoor")
