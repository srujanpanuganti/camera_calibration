# Calibrating a camera using opencv

These steps can be comfortably used to calibrate Arducam IMX219 fisheye lens for Raspberry Pi 4 and Nvidia Jetson Nano

Steps to calibrate a camera

* Print out the 7x8 chess board image attached in `images/chessboards_7x8.png` on an A4 size sheet

* Use the camera_calibration.py to generate images of chess_board in several different angles.
This script will generate 100 raw samples to raw_samples folder. Except few good images, delete all other images from the folder.
Ideally, keep between 10-14 raw samples. 

* Now run the distortion_coeff.py to generate the distortion coefficients. These coefficients are saved to config/config.pkl file
* now run the undistort.py to see the results of calibraton from raw image to undistorted image

Here are the results:

<img src="figures/predict.png" width="540">


These steps are followed from OpenCV Python Tutorials. https://opencv-python-tutroals.readthedocs.io
