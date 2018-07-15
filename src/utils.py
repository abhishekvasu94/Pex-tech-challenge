import cv2
import numpy as np
import sys
import os
import glob

#This file is used to create the dataset
#To create the dataset for indoor files, run "python utils.py indoor", and for outdoor files, run "python utils.py outdoor"

def create_frames(filename, count, photo_path):

	#filename: This is the path to a video file
	#count: This is used to write the image to the file name specified by the value in count
	#photo_path: This is the directory in which I want to write the frames
	#This function extracts relevant frames from the video

	cap = cv2.VideoCapture(filename)
	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

	if cap.isOpened() and length > 5:	#Since I am extracting 5 frames, the video should contain at least 5 frames

		i = 0.1			#The reason I start with 0.1 is because the beginning of the video might contain irrelevant frames like credits, logo of channel, intro etc
					#This is the same reason I don't include the final frames of the video

		while i <= 0.9:
			cap.set(1, int(i*length))
			ret, frame = cap.read()
			frame = cv2.resize(frame, (64, 64))			#resize frame to size 64x64 since I am doing this task on my local machine (no GPU)
			cv2.imwrite(photo_path + str(count) + '.png', frame)	#Write image
			count += 1
			i += 0.2

	return count

def procure_files(path, ext):

	#path: path to directory where our files are present
	#ext: extention we are interested in

	files = glob.glob(path + '*' + ext)	#Obtain all files with given extension in given path
	return files



if __name__ == '__main__':


	#All files are of mp4 format
	ext = 'mp4'

	if sys.argv[1] == 'indoor':
		path = os.path.join("..", "data", "indoor_videos", "")
		photo_path = os.path.join("..", "data", "photos", "indoor_photos", "")

	elif sys.argv[1] == 'outdoor':
		path = os.path.join("..", "data", "outdoor_videos", "")
		photo_path = os.path.join("..", "data", "photos", "outdoor_photos", "")

	files = procure_files(path, ext)

	#Used to write image
	count = 1

	#Create frames for each video in our folder
	for i in range(len(files)):

		count = create_frames(files[i], count, photo_path)


