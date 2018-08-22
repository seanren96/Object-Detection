from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", default = 'train_val_googlenet.prototxt',
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", default = 'googlenet_finetune_web_car_iter_10000.caffemodel' ,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
    image = cv2.imread("000001.jpg")
cv2.destroyAllWindows()