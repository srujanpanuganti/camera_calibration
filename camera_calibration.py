import cv2
import numpy
import time
import sys

video = cv2.VideoCapture(0)
print('[INFO] : video started')

## letting the camera warm up
time.sleep(2.0)

if not video.isOpened():
    print("[ERROR] : Could not open video, camera isn't working")
    sys.exit()

all_imgs = []
count =0
while count < 100:
    count +=1
    ok,frame = video.read()
    if not ok:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # resized = cv2.resize(cropped, (200,200))

    cv2.imshow('image', gray)

    all_imgs.append(gray)
    time.sleep(0.5)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

i = 1
for im in all_imgs:
    cv2.imwrite('./raw_samples/pic{:>05}.jpg'.format(i), im)
    i+=1
print('[INFO] : user has been saved to the database')
