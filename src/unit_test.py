import cv2
import numpy as np
import unittest
from utils import procure_files
import os
from model import model
from keras.models import load_model
import h5py

class utilsTest(unittest.TestCase):

	#Test for the data processing part

	def test_load_files(self):
		#To check whether all the files are being loaded

		path = os.path.join("..", "data", "indoor_videos", "")
		ext = 'mp4'
		self.assertTrue(len(procure_files(path, ext)) > 0)

	def test_images(self):
		#To make sure that the images are not of NoneType

		path = os.path.join("..", "data", "photos", "indoor_photos", "1.png")
		img = cv2.imread(path, 1)
		self.assertTrue(np.mean(img) > 0)

	def test_model(self):
		#To make sure that the loss is never zero, not even for the fake data used here

		model = load_model('my_model.h5')
		inp = np.ones((1,64,64,3))
		test_loss = model.evaluate(inp, np.array([1]))
		self.assertTrue(test_loss != 0)
		
		
		

if __name__ == "__main__":

	unittest.main()


