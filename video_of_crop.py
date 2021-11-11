#
# import cv2
# import numpy as np
# import glob
#
#
#
# img_array = []
# for filename in glob.glob('E:/deepfake buster/practice code/cropped_images/*.jpg'):
#     img = cv2.imread(filename)
#     # height, width, layers = img.shape
#     # size = (width, height)
#     img_array.append(img)
#
#
#
# out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15,(500,480))
#
# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()
#

import ffmpeg


(
    ffmpeg
    .input('E:/deepfake buster/practice code/cropped_images/*.jpg', pattern_type='glob', framerate=25)
    .output('movie.mp4')
    .run()
)




