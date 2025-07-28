import cv2
import numpy as np
from picamera2 import Picamera2
import os

def detectColor(imageName, rangeLow, rangeHigh, wantedColor):

    #reads image from file name
    img = cv2.imread(imageName)
    if img is None:
        print("Error: Image file not found or could not be read.")
        exit()

    print("Image Read")

    #converts BGR scheme to HSV
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    print("Color Scheme successfully changed to HSV")

    #color mask applies
    color_mask = cv2.inRange(hsvFrame, rangeLow, rangeHigh)

    print("Color Mask sucessfully applied")

    #detects how many pixels of "that color" are in the image adjust "7000" to change sensitivty
    white_pixel_count = cv2.countNonZero(color_mask)
    pixel_threshold = 7000
    if white_pixel_count >= pixel_threshold:
        print (f"{wantedColor} Found!!!")#Just put in some boolean value here "correctColor = True" or smth to actually read out if the color is in frame or not.
        print ("There are at least " + str(pixel_threshold) + " correct pixels here")
    else:
        print(f"{wantedColor} not Found!!!")
    return

#camera start up code
picam2 = Picamera2()
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("still")
picam2.start()

picam2.capture_file("tempImage.jpg")#takes picture from the camera and saves it in the "final" folder

#checks if tempImage was actually created
if os.path.exists("tempImage.jpg"):
    print(f"tempImage created")
else:
    print(f"tempImage not created")

#defines color mask range for blue (these ranges might need to be adjusted depending on light conditions)
color_lower_range = np.array([100, 200, 85], np.uint8)
color_upper_range = np.array([122, 255, 255], np.uint8)

detectColor("tempImage.jpg" ,color_lower_range, color_upper_range, "Blue")

#defines color mask range for red
color_lower_range = np.array([0, 155, 149], np.uint8)
color_upper_range = np.array([9, 255, 255], np.uint8)

detectColor("tempImage.jpg", color_lower_range, color_upper_range, "Red")

#defines color mask range for green
color_lower_range = np.array([38, 98, 141], np.uint8)
color_upper_range = np.array([60, 255, 255], np.uint8)

detectColor("tempImage.jpg", color_lower_range, color_upper_range, "Green")

try: #makes sure that tempImage exists before deleting it
    if os.path.exists("tempImage.jpg"):
        os.remove("tempImage.jpg")
        print(f"File tempImage.jpg deleted successfully.")
    else:
            print(f"File tempImage.jpg does not exist.")
except OSError as e:
    print(f"Error deleting file")

