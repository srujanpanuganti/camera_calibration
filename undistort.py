import pickle
import cv2
import time
import sys

with open("config.pkl",'rb') as config:
    data = pickle.load(config)

mtx = data['mtx']
dist = data['dist']

video = cv2.VideoCapture(0)
print('[INFO] : video started')

## letting the camera warm up
time.sleep(2.0)


if not video.isOpened():
    print("[ERROR] : Could not open video, camera isn't working")
    sys.exit()


while True:
    ok,img = video.read()
    if not ok:
        break

    h,  w = img.shape[:2]
    newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    cv2.imshow('distorted image', img)
    cv2.imshow('undistorted image', dst)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
