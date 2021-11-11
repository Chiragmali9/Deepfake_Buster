import cv2
import glob
import os

path = 'E:/deepfake buster/practice code/cropped_images'
count = 0
for img in glob.glob("E:/deepfake buster/practice code/face_detected_images/*.jpg"):
    image = cv2.imread(str(img))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("[INFO] Found {0} Faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #status = cv2.imwrite('faces_detected%d.jpg' % count, image)

        roi_color = image[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite(os.path.join(path ,'faces_detected%d.jpg' % count), roi_color)

        count += 1
    print(str(img))

    print(count)
    #print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
