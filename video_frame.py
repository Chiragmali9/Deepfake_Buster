import cv2
import os
vidcap = cv2.VideoCapture('intro.mp4')
success,image = vidcap.read()
count = 0
path = 'E:/deepfake buster/practice code/face_detected_images'
while success:
  cv2.imwrite(os.path.join(path,"frame%d.jpg" % count), image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1