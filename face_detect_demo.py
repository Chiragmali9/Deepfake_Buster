import cv2
import glob
import cv2 as cv


# Read the input image
# img = cv2.imread('frame0.jpg')

# Convert into grayscale

path = glob.glob("E:\deepfake buster\practice code/*.jpg")
cv_img = []
for img in path:
    imgs = cv2.imread(img)

    gray = cv2.cvtColor(imgs, cv2.COLOR_BGR2GRAY)

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    count = 0

    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(imgs, (x, y), (x + w, y + h), (0, 0, 255), 2)
        faces = imgs[y:y + h, x:x + w]
        # cv2.imshow("face", faces)
        cv2.imwrite('face%d.jpg' % count, faces)
        count += 1

    n = cv.imread(img)
    cv_img.append(n)


# # Display the output
# cv2.imwrite('detcted.jpg', img)
# cv2.imshow('img', img)
# cv2.waitKey()
